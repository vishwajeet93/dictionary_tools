import torch
import torch.nn.functional as F

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

batch = {
	'input_ids':torch.unsqueeze(torch.tensor([1,2,3,4,5]),dim=0).to(DEVICE),
	'label':torch.tensor([1]).to(DEVICE),
}

class Model(torch.nn.Module):

	def __init__(self):
		super(Model,self).__init__()
		self.device = None
		self.embed = torch.nn.Embedding(20,10)
		self.classifier = torch.nn.Linear(10, 3)

	def forward(self,batch):
		batch['input_ids'] = batch['input_ids']
		batch['label'] = batch['label']

		output = self.embed(batch['input_ids'])
		print(output.shape)
		#output1 = output[:,0,:]
		output2 = self.classifier(F.relu(output1))
		return output2

	def to(self, *args, **kwargs):
		self = super().to(*args, **kwargs)
		self.device = args[0]
		self.embed = self.embed.to(*args, **kwargs)
		self.classifier = self.classifier.to(*args, **kwargs)
		return self

model = Model().to(DEVICE)
print (model.device)
optim = torch.optim.SGD(model.parameters(), lr = 0.1)

output2 = model.forward(batch)

for name, param in model.named_parameters():
	print (name, param.grad.data)

optim.zero_grad()

loss = F.cross_entropy(output2, batch['label'])
loss.backward()

for name, param in model.named_parameters():
	print (name, param.grad.data)




