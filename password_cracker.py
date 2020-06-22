import random
import string
#Generate Population (아이들 생성= 비밀번호 조합)
password = 'brad1234'
min_len = 2
max_len = 10
# 엄마도 기억력의 한계가 있어서 비밀번호의 최대, 최소 자릿수를 지정해놓았다

def generate_word(length):
    result = ''
    x = ''.join(random.sample(string.ascii_letters + string.digits, k=length))
    return x
    ##random.sample(pop,k): pop에서 랜덤하게 k개 뽑음
    ## 랜덤으로 n개의 비밀번호 집합 생성
def generate_population(size, min_len, max_len):
    population = []
    for i in range(size):
        ##generate words with balanced length(min~max_len)
        length = i % (max_len - min_len + 1) + min_len
        population.append(generate_word(length))
    return population

print(generate_word(length=10))
pop = generate_population(size=100, min_len=min_len, max_len=max_len)
pop
#Fitness Function (아이들 유전자 성능 측정)
def fitness(password, test_word):
    score = 0

    if len(password) != len(test_word):
        return score
    
    len_score = 0.5
    score += len_score

    for i in range(len(password)):
        if password[i] == test_word[i]:
            score += 1

    
    return score / (len(password) + len_score) * 100
#Compute Performance and Select Survivors(똑똑한 아이들 선발)
fitness('abcde', 'abcde')


def compute_performace(population, password):
    performance_list = []
     ##모든 아이들 점수측정후 
    for individual in population:
        score = fitness(password, individual)

        # we can predict length of password
        if score > 0: ##길이는 맞는 상태
            pred_len = len(individual)
        performance_list.append([individual, score])

    population_sorted = sorted(performance_list, key=lambda x: x[1], reverse=True)
     ##sorted(list,key,reverse=True): list를 key기준으로 내림차순 정렬, x[1]: 점수
    return population_sorted, pred_len

def select_survivors(population_sorted, best_sample, lucky_few, password_len):
    ##정해놓은 수만큼 best sample과 운이 좋은 아이들을 살려 다음 세대으로 넘김
    next_generation = []

    for i in range(best_sample):
        if population_sorted[i][1] > 0:
            next_generation.append(population_sorted[i][0])
    ##다음세대로 넘길 아이들을 너무 적게 뽑았다면 아무렇게나 단어를 생성
    lucky_survivors = random.sample(population_sorted, k=lucky_few)
    for l in lucky_survivors:
        next_generation.append(l[0])
    
    # generate new population if next_generation is too small
    while len(next_generation) < best_sample + lucky_few:
        next_generation.append(generate_word(length=password_len))

    random.shuffle(next_generation)
    return next_generation
     ##random.shuffle():랜덤한 순서로 섞는다.

pop_sorted, pred_len = compute_performace(pop, password)
survivors = select_survivors(pop_sorted, best_sample=20, lucky_few=20, password_len=pred_len)
##100명(pop_sorted)의 아이들중 우수한(best_sample) 20명과 운이좋은(lucky_few) 20명을 선발

print('Password length must be %s' % pred_len)
survivors

#Create Children(교배)

def create_child(individual1, individual2):
    child = ''
    min_len_ind = min(len(individual1), len(individual2))
    ##부모중 더 짧은 길이에 맞추어 자식을 생성

    
    for i in range(min_len_ind):
        if (int(100 * random.random()) < 50):
            child += individual1[i]
        else:
            child += individual2[i]
             ##50프로의 확률로 엄마또는 아빠의 유전자를 받음.
    return child

    ##교배할 부모를 짝지어주고 아이를 생성
def create_children(parents, n_child):
    next_population = []
    for i in range(int(len(parents)/2)):
        for j in range(n_child):
            next_population.append(create_child(parents[i], parents[len(parents) - 1 - i]))
            ##부모 100명이면 50쌍, 생성하고 싶은 아이들의수(n_child)만큼
    return next_population

children = create_children(survivors, 5)
    
children
##부모40명(20쌍)이 5명의 아이를 낳으면 100의 아이가 생성

#Mutation(돌연변이 생성)

    ##임의의 index의 key를 random한 문자나 숫자로 변경
def mutate_word(word):
    idx = int(random.random() * len(word))
    if (idx == 0):
        word = random.choice(string.ascii_letters + string.digits) + word[1:]
        ##string.ascii_letters + string.digits: 대소문자+숫자,
    else:
        word = word[:idx] + random.choice(string.ascii_letters + string.digits) + word[idx+1:]
    return word

def mutate_population(population, chance_of_mutation):
    ##원하는 비율(chance_of_mutation)만큼 돌연변이 생성
    for i in range(len(population)):
        if random.random() * 100 < chance_of_mutation:
            population[i] = mutate_word(population[i])
    return population

new_generation = mutate_population(population=children, chance_of_mutation=10)

new_generation
#Test
password = 'bBanGhyONg'
n_generation = 300
population = 100
best_sample = 20
lucky_few = 20
n_child = 5
chance_of_mutation = 10

pop = generate_population(size=population, min_len=min_len, max_len=max_len)

for g in range(n_generation):
    pop_sorted, pred_len = compute_performace(population=pop, password=password)

    if int(pop_sorted[0][1]) == 100:
        print('SUCCESS! The password is %s' % (pop_sorted[0][0]))
        break
    
    survivors = select_survivors(population_sorted=pop_sorted, best_sample=best_sample, lucky_few=lucky_few, password_len=pred_len)
    
    children = create_children(parents=survivors, n_child=n_child)

    new_generation = mutate_population(population=children, chance_of_mutation=10)
    
    pop = new_generation
    
    print('===== %sth Generation =====' % (g + 1))
    print(pop_sorted[0])

    
