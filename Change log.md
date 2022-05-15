# Change log
# 1.make "output" from 1000 to 200
In the function `main_worker`, main.py, 
add 
```
model.fc = nn.Sequential(nn.Linear(in_features=512,out_features=200))
```
after model definition 
```
model = models.__dict__[args.arch](pretrained=True)
```
# 2.image stretch and tailor should be abandoned
In Data loading code, function `main_worker`, main.py, 
`transforms.RandomResizedCrop(224)` and `transforms.RandomHorizontalFlip()`
in `train_dataset` should be masked.
Also, `transforms.Resize(256)` and `transforms.CenterCrop(224)`
in `val_loader` should be masked.
# 3.show loss and accuracy in tensorboard
in the function `train`, add code
```
train_dir = os.path.join('tensorboard1', 'train')
train_writer = SummaryWriter(log_dir=train_dir)
train_writer.add_scalar('Acc@5', acc5, epoch)
train_writer.add_scalar('loss', loss, epoch)
```
also, add code in the function `validate`,
```
val_dir = os.path.join('tensorboard2', 'valid')
val_writer = SummaryWriter(log_dir=val_dir)
val_writer.add_scalar('Acc@5', acc5, epoch)
val_writer.add_scalar('loss', loss, epoch)
```
necessarily, the function `train` and `validate` should add new parameter 'epoch'
# 4.evaluate
load the model and parameters which have been trained well, add code
```
model.load_state_dict(torch.load('model_best.pth.tar')['state_dict'])
```
after `if args.evaluate:` in the `main_worker`
