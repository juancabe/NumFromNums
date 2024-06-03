import copy

nums = [2, 3, 9, 8, 91]
guess = 531
opDir = {
	0: '+',
	1: '-',
	2: '/',
	3: '*'
}

def find_op_rec(nums, guess, ops, order):
	
	saved_nums = copy.deepcopy(nums)
	saved_ops = copy.deepcopy(ops)
	saved_order = copy.deepcopy(order)

	if(len(nums) < 1):
		print("Error < 1")

	if(len(nums) == 1):
		if(guess == nums[0]):
			return [copy.deepcopy(order),copy.deepcopy(ops)]
		else:
			return False
	elif guess in nums:
		return [copy.deepcopy(order),copy.deepcopy(ops)]

	for x in range(4):
		for i in range(len(nums)):
			for j in range(len(nums)):
				if(i == j):
					continue
				if(nums[i] >= nums[j]):

					if x == 0:
						#print("Nums: " + str(nums))
						#print("Adding: " + str(nums[i]) + " + " + str(nums[j]))
						nums[i] = nums[i]+nums[j]
						
					if x == 1:
						#print("Nums: " + str(nums))
						#print("Substracting: " + str(nums[i]) + " - " + str(nums[j]))
						nums[i] = nums[i]-nums[j]
					if x == 2:
						#print("Nums: " + str(nums))
						#print("Dividing: " + str(nums[i]) + " / " + str(nums[j]))
						if(nums[j] != 0 and nums[i] % nums[j] == 0):
							nums[i] = nums[i] / nums[j]
						else:
							continue
					if x == 3:
						#print("Nums: " + str(nums))
						#print("Multiplying: " + str(nums[i]) + " * " + str(nums[j]))
						nums[i] = nums[i]*nums[j]

					ops[i].append(x)
					order.append([i,j])
					nums.pop(j)

					xd = find_op_rec(nums, guess, ops, order)
					if(xd):
						return xd
					else:
						nums = copy.deepcopy(saved_nums)
						ops = copy.deepcopy(saved_ops)
						order = copy.deepcopy(saved_order)
	
	nums = copy.deepcopy(saved_nums)
	ops = copy.deepcopy(saved_ops)
	order = copy.deepcopy(saved_order)

	return False

def print_op(nums, guess, ops, order):

	operations = ""

	while(len(order) != 0):
		x = order.pop(0)
		op = ops[x[0]].pop(0)
		if(op == 0):
			#print(str(nums[x[0]]) + " + " + str(nums[x[1]]) + " = " + str(nums[x[0]] + nums[x[1]]))
			operations += str(nums[x[0]]) + " + " + str(nums[x[1]]) + " = " + str(nums[x[0]] + nums[x[1]]) + "\n"
			nums[x[0]] = nums[x[0]] + nums[x[1]]
		if(op == 1):
			#print(str(nums[x[0]]) + " - " + str(nums[x[1]]) + " = " + str(nums[x[0]] - nums[x[1]]))
			operations += str(nums[x[0]]) + " - " + str(nums[x[1]]) + " = " + str(nums[x[0]] - nums[x[1]]) + "\n"
			nums[x[0]] = nums[x[0]] - nums[x[1]]
		if(op == 2):
			#print(str(nums[x[0]]) + " / " + str(nums[x[1]]) + " = " + str(nums[x[0]] / nums[x[1]]))
			operations += str(nums[x[0]]) + " / " + str(nums[x[1]]) + " = " + str(nums[x[0]] / nums[x[1]]) + "\n"
			nums[x[0]] = nums[x[0]] / nums[x[1]]
		if(op == 3):
			#print(str(nums[x[0]]) + " * " + str(nums[x[1]]) + " = " + str(nums[x[0]] * nums[x[1]]))
			operations += str(nums[x[0]]) + " * " + str(nums[x[1]]) + " = " + str(nums[x[0]] * nums[x[1]]) + "\n"
			nums[x[0]] = nums[x[0]] * nums[x[1]]
		nums.pop(x[1])

	print("Guess: " + str(guess))
	print("Operations: \n" + operations)

def find_op(nums, guess):
	ops = [[], [], [], [] ,[]]
	order = []
	x = find_op_rec(copy.deepcopy(nums), guess, ops, order)
	if(x):
		order = x[0]
		ops = x[1]
		#print("order: " + str(order))
		#print("ops: " + str(ops))
		print_op(nums, guess, ops, order)
		return True
	else:
		print('Fuck')
		if(find_op(nums, guess-1)):
			return True
		else:
			find_op(nums, guess+1)
		

find_op(nums, guess)
