import copy

nums = [2, 2, 7, 9, 8, 19]
guess = 1323
opDir = {
	0: '+',
	1: '-',
	2: '/',
	3: '*'
}

def find_op_rec(nums, guess, ops, order, branch):
	
	saved_nums = copy.deepcopy(nums)
	saved_ops = copy.deepcopy(ops)
	saved_order = copy.deepcopy(order)
	saved_branch = branch

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

					xd = find_op_rec(nums, guess, ops, order, branch)
					if(xd):
						return xd
					else:
						nums = copy.deepcopy(saved_nums)
						ops = copy.deepcopy(saved_ops)
						order = copy.deepcopy(saved_order)
						branch = saved_branch
	
	nums = copy.deepcopy(saved_nums)
	ops = copy.deepcopy(saved_ops)
	order = copy.deepcopy(saved_order)
	branch = saved_branch

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
	print("Operations: " + operations)

def find_op(nums, guess):
	ops = [[], [], [], [] ,[]]
	order = []
	branch = 0
	x = find_op_rec(copy.deepcopy(nums), guess, ops, order, branch)
	if(x):
		order = x[0]
		ops = x[1]
		#print("order: " + str(order))
		#print("ops: " + str(ops))
		print_op(nums, guess, ops, order)
	else:
		print('Fuck')

find_op(nums, guess)
