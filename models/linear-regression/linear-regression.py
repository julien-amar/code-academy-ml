#####################
# Linear Regression #
#####################

def get_gradient_at_b(x, y, m, b):
  N = len(x)
  diff = 0
  for i in range(N):
    diff += (y[i] - ((m * x[i]) + b))
  return -(2/N) * diff  

def get_gradient_at_m(x, y, m, b):
  N = len(x)
  diff = 0
  for i in range(N):
      diff += x[i] * (y[i] - ((m * x[i]) + b))
  return -(2/N) * diff  

def step_gradient(x, y, m_current, b_current, learning_rate):
    b_gradient = get_gradient_at_b(x, y, m_current, b_current)
    m_gradient = get_gradient_at_m(x, y, m_current, b_current)
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    return [b, m]

def gradient_descent(x, y, learning_rate, num_iterations):
  m = 0
  b = 0
  for i in range(num_iterations):
    b, m = step_gradient(x, y, m, b, learning_rate)
  return [m, b]

def get_loss(x, y, m, b):
  N = len(x)
  loss = 0
  for i in range(N):
      loss += (y[i] - ((m * x[i]) + b)) ** 2
  return loss

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

m, b = gradient_descent(months, revenue, num_iterations=1000, learning_rate=0.01)
best_loss = get_loss(months, revenue, m, b)
print(m, b, best_loss) # 10.463427732364998 49.60215351339813 593.7414927546841
