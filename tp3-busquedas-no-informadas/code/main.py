from map import Map

map = Map(5, 0.9)
env = map.env

state = env.reset()
print("Posicion inicial del agente:", state[0])
done = truncated = False
while not (done or truncated):
  action = env.action_space.sample() # Accion aleatoria
  next_state, reward, done, truncated, _ = env.step(action)
  print(f"Accion: {action}, Nuevo estado: {next_state}, Recompensa: {reward}")
  print(f"¿Gano? (encontro el objetivo): {done}")
  print(f"¿Freno? (alcanzo el maximo de pasos posible): {truncated}\n")
  state = next_state