import matplotlib.pyplot as plt

from channel import PoissonChannel
from receiver import MAPReceiver
from source import UniformSource

alphabet = ["0", "1"]
lambdas = [1.5, 15]

s = UniformSource(alphabet)
c = PoissonChannel(s, lambdas)
r = MAPReceiver(source=s, channel=c)

s.generate_messages(1000)
plt.hist(c.output, 50, density=True)
plt.savefig("channel")
plt.clf()

print(f"Receiver real error rate: {r.real_error(s.output)}")
