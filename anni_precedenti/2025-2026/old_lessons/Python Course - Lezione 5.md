Tratto da:
https://towardsdatascience.com/handwritten-digit-mnist-pytorch-977b5338e627

# Ripassino Classi e Metodi


# Reti Neurali

![](attachment/bf758a51a0c0d1017ad1c262f7e0d07d.pdf)

# Classificatore di Numeri Scritti a Mano

## Cosa faremo:

![](attachment/f36756b5769fbc9045bd39f3a2abc830.webp)



![](attachment/75f973032ed8e08288dd8adada25d972.webp)



### Che pacchetti ci servono

```bash
pip install --upgrade pip
pip install numpy
pip install torch
pip install torchvision
pip install matplotlib
```


```python
import numpy as np  
import torch  
import torchvision  
import matplotlib.pyplot as plt  
from time import time  
from torchvision import datasets, transforms  
from torch import nn, optim
```


### L'importanza del dataset
- A cosa serve un buon dataset?

![](attachment/a2d144a3497bd503e86caff5c369fb71.webp)


#### Che trasformazioni ci servono sui dati?
Prima di scaricare i dati applichiamo le seguenti trasformazioni, servono per rendere le immagini omogenee tra loro.

```python
transform = transforms.Compose([transforms.ToTensor(),  
transforms.Normalize((0.5,), (0.5,)),  
])
```

- `transforms.ToTensor()` - Vedi [[transforms.ToTensor()]] per dettagli.
	- Converte immagini PIL o array NumPy in tensori PyTorch
	- Cambia le dimensioni da (Altezza x Larghezza x Canali) a (Canali x Altezza x Larghezza)
	- Scala i valori dei pixel da [0, 255] a [0.0, 1.0] dividendo tutti i valori per 255
	- **In pratica**, il processo trasforma le immagini in numeri creando tre immagini separate per i colori RGB: una per il rosso (Red), una per il verde (Green) e una per il blu (Blue). Questa conversione avviene traducendo l'immagine in un tensore, che è simile a un array di array ma ottimizzato per il calcolo numerico e per il machine learning. È importante non considerare il tensore come un semplice array di array, poiché segue specifiche regole nella sua creazione.
- `transforms.Normalize()` - Serve per effettuare una "[[Mean Normalization]]" dei dati con media $\mu=0.5$ e deviazione standard $\sigma=0.5$. (Reference: [documentation](https://pytorch.org/vision/stable/generated/torchvision.transforms.v2.Normalize.html?highlight=normalize#torchvision.transforms.v2.Normalize))

Ora procederemo finalmente al download dei dataset, che verranno successivamente mescolati e trasformati. Dopo aver scaricato i dataset, li caricheremo in un _DataLoader_. Quest'ultimo è uno strumento che aggrega il dataset e un campionatore, fornendo iteratori che possono operare sia in modalità singolo processo che multiprocesso sui dati.

La [classe `Dataset`]([[Pytorch - Dataset & Data Load]]) è una classe di base astratta utile per rappresentare un dataset. Richiede l'implementazione di due metodi: `__len__()`, che restituisce la dimensione del dataset, e `__getitem__()`, che recupera un campione di dati ad un dato indice. I dataset personalizzati possono essere creati creando una sottoclasse di `Dataset` e definendo questi metodi.


```python
trainset = datasets.MNIST('PATH_TO_STORE_TRAINSET', download=True, train=True, transform=transform)

valset = datasets.MNIST('PATH_TO_STORE_TESTSET', download=True, train=False, transform=transform)

trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

valloader = torch.utils.data.DataLoader(valset, batch_size=64, shuffle=True)
```

- `torch.utils.data.DataLoader()` - crea un *data loader object*  che avvolge un dataset e fornisce un iterabile su di esso. Gestisce il batching, il mescolamento (shuffling) e il caricamento in parallelo dei dati, rendendo più semplice fornire i dati ad un modello durante l'addestramento o la valutazione.

- `batch_size` - è quante immagini vogliamo passare al nostro algoritmo ad ogni giro

## Esploriamo il dataset


```python
dataiter = iter(trainloader)
images, labels = next(dataiter)

print(images.shape)
print(labels.shape)
```

1. **`dataiter = iter(trainloader)`**:
    
    - Questa riga crea un iteratore dal `trainloader`. In PyTorch, un `DataLoader` (come `trainloader`) è utilizzato per caricare i dati a lotti. Chiamando `iter(trainloader)`, crei un iteratore che ti permette di ciclare attraverso i lotti di dati.
2. **`images, labels = next(dataiter)`**:
    - Questa riga recupera il prossimo lotto di dati dall'iteratore. Il metodo `next()` restituisce un singolo lotto di dati, che tipicamente consiste in una tupla contenente le immagini e le loro corrispondenti etichette.
    - `images` conterrà il lotto di dati in ingresso (ad esempio, immagini), e `labels` conterrà le etichette corrispondenti a quelle immagini.
3. **`print(images.shape)`**:
    - Questa riga stampa la forma del tensore `images`. La forma sarà tipicamente nella forma `(batch_size, channels, height, width)`, dove:
        - `batch_size` è il numero di immagini nel lotto.
        - `channels` è il numero di canali colore (ad esempio, 3 per immagini RGB).
        - `height` e `width` sono le dimensioni di ciascuna immagine.
4. **`print(labels.shape)`**:
    - Questa riga stampa la forma del tensore `labels`. La forma è solitamente `(batch_size,)`, indicando che c'è un'etichetta per ogni immagine nel lotto.


```python
plt.imshow(images[0].numpy().squeeze(), cmap='gray_r');
```

1. **`images[0]`**:
    - Questo accede alla prima immagine nel batch di immagini. `images` è un tensore che contiene un batch di immagini, e `images[0]` seleziona la prima immagine da questo batch.
2. **`.numpy()`**:
    - Questo converte il tensore di PyTorch in un array NumPy. I tensori di PyTorch devono essere convertiti in array NumPy per essere compatibili con molte librerie Python, inclusa Matplotlib.
3. **`.squeeze()`**
    - Questo rimuove qualsiasi dimensione singola dall'array. Ad esempio, se l'immagine ha una forma di `(1, altezza, larghezza)`, `squeeze()` la convertirà in `(altezza, larghezza)`. Questo è spesso necessario per le immagini in scala di grigi, che possono avere una dimensione di canale extra.
4. **`plt.imshow(..., cmap='gray_r')`**:
    - `plt.imshow()` è una funzione di Matplotlib utilizzata per visualizzare un'immagine.
    - L'argomento `cmap='gray_r'` specifica la mappa dei colori da utilizzare per visualizzare l'immagine. `'gray_r'` è una mappa dei colori in scala di grigi invertita, il che significa che l'immagine verrà visualizzata in scala di grigi con i colori invertiti (cioè, il nero diventa bianco e viceversa).
5. **`;` (punto e virgola alla fine)**:
    - Nei notebook Jupyter, aggiungere un punto e virgola alla fine di una riga sopprime l'output dell'ultimo comando. In questo contesto, impedisce la visualizzazione di output di testo aggiuntivo quando l'immagine viene mostrata.

```python
figure = plt.figure()  
num_of_images = 60  
for index in range(1, num_of_images + 1):  
	plt.subplot(6, 10, index)  
	plt.axis('off')  
	plt.imshow(images[index].numpy().squeeze(), cmap='gray_r')
```



## Costruiamo la rete neurale

![](attachment/ac0b47992b0a08a7757a7cb5494e0fa8.webp)


```python
input_size = 784  
hidden_sizes = [128, 64]  
output_size = 10  
  
model = nn.Sequential(nn.Linear(input_size, hidden_sizes[0]),  
nn.ReLU(),  
nn.Linear(hidden_sizes[0], hidden_sizes[1]),  
nn.ReLU(),  
nn.Linear(hidden_sizes[1], output_size),  
nn.LogSoftmax(dim=1))  
print(model)
```

1. **Dimensioni di Input e Output**:
    - `input_size = 784`: Questa è la dimensione del livello di input. Suggerisce che ogni campione di input è un'immagine 28x28 appiattita (comune per il dataset MNIST).
    - `hidden_sizes = [128, 64]`: Questa lista definisce le dimensioni di due livelli nascosti. Il primo livello nascosto ha 128 neuroni e il secondo ne ha 64.
    - `output_size = 10`: Questa è la dimensione del livello di output, indicando che il modello è progettato per un compito di classificazione con 10 classi (ad esempio, cifre da 0 a 9).
2. **Definizione del Modello**:
    - `nn.Sequential(...)`: Questo è un modulo contenitore che sequenzia i livelli nell'ordine in cui sono definiti.
3. **Livelli**:
    - `nn.Linear(input_size, hidden_sizes[0])`: Il primo livello è un livello lineare (completamente connesso) che mappa l'input di dimensione 784 al primo livello nascosto di dimensione 128.
    - `nn.ReLU()`: Una funzione di attivazione ReLU (Rectified Linear Unit) viene applicata dopo il primo livello lineare per introdurre non-linearità.
    - `nn.Linear(hidden_sizes[0], hidden_sizes[1])`: Il secondo livello lineare mappa i 128 neuroni dal primo livello nascosto a 64 neuroni nel secondo livello nascosto.
    - `nn.ReLU()`: Un'altra funzione di attivazione ReLU viene applicata dopo il secondo livello lineare.
    - `nn.Linear(hidden_sizes[1], output_size)`: Il terzo livello lineare mappa i 64 neuroni dal secondo livello nascosto al livello di output di dimensione 10.
    - `nn.LogSoftmax(dim=1)`: Questo applica la funzione LogSoftmax al livello di output, che è tipicamente utilizzata per problemi di classificazione multi-classe per produrre log-probabilità.
4. **Stampa del Modello**:
    - `print(model)`: Questo stamperà un riepilogo dell'architettura del modello, mostrando ogni livello in sequenza.


Il `nn.Sequential` raggruppa insieme i livelli della rete. Ci sono tre livelli lineari, ciascuno seguito da un'attivazione ReLU. ReLU è una funzione semplice che lascia passare i valori positivi ma trasforma i valori negativi in zero. L'ultimo livello è un livello lineare con un'attivazione LogSoftmax perché stiamo risolvendo un problema di classificazione.

LogSoftmax è semplicemente il logaritmo della funzione Softmax, usata per gestire più classi.


Utilizziamo la perdita di verosimiglianza negativa (negative log-likelihood loss) per addestrare il modello. Questo è utile per compiti di classificazione con più classi. Insieme, LogSoftmax e NLLLoss funzionano come cross-entropy loss.

Il primo livello ha 784 unità perché appiattiamo ogni immagine prima di inserirla nella rete. Poiché ogni immagine è di 28x28 pixel, appiattendola si ottengono 784 unità (28 x 28 = 784).

```python
criterion = nn.NLLLoss()  
images, labels = next(iter(trainloader))  
images = images.view(images.shape[0], -1)  
  
logps = model(images) #log probabilities  
loss = criterion(logps, labels) #calculate the NLL loss
```
1. **`criterion = nn.NLLLoss()`**:
    
    - This line initializes the loss function. `nn.NLLLoss()` is a negative log likelihood loss function commonly used in classification tasks. It expects the input to be log probabilities.
2. **`images, labels = next(iter(trainloader))`**:
    
    - Here, `trainloader` is an iterator that provides batches of data. `next(iter(trainloader))` retrieves the next batch of images and their corresponding labels from the training data.
3. **`images = images.view(images.shape[0], -1)`**:
    
    - This line reshapes the `images` tensor. `images.shape[0]` is the batch size, and `-1` means the rest of the dimensions are flattened into a single dimension. This is often done to prepare the data for input into a fully connected layer in a neural network.
4. **`logps = model(images)`**:
    
    - The reshaped images are passed through the `model`, which outputs `logps`, the log probabilities of each class for each image in the batch.
5. **`loss = criterion(logps, labels)`**:
    
    - The `criterion` (NLLLoss) is used to calculate the loss between the predicted log probabilities (`logps`) and the true labels (`labels`). This loss value is used to update the model's weights during training.



```python
print('Before backward pass: \n', model[0].weight.grad)
loss.backward()
print('After backward pass: \n', model[0].weight.grad)
```



Nota:
Per mantenere le informazioni e runnare il comando più volte:
- **Error Message**:
    
    - `RuntimeError: Trying to backward through the graph a second time (or directly access saved tensors after they have already been freed).`
- **Cause**:
    
    - This error occurs when you attempt to call `.backward()` on the same computation graph more than once without specifying `retain_graph=True`. By default, PyTorch frees the intermediate values of the computation graph after the first backward pass to save memory.
- **Solution**:
    
    - If you need to perform multiple backward passes on the same graph, you should specify `retain_graph=True` in the first backward call like this: `loss.backward(retain_graph=True)`. This tells PyTorch to retain the computation graph for further backward passes.

## Core Training

This section describes the core process of how your neural network learns from the training data. During each **epoch** (which is one complete pass through the entire training set), the neural network's weights are updated to minimize errors. This updating of weights is done using the `torch.optim` module from PyTorch. This module helps in optimizing the model by performing gradient descent and adjusting the weights accordingly through a method called back-propagation. As a result, you should observe a gradual reduction in the training loss with each epoch, indicating that the model is learning effectively.


```python
optimizer = optim.SGD(model.parameters(), lr=0.003, momentum=0.9)  
time0 = time()  
epochs = 15  
for e in range(epochs):  
    running_loss = 0  
    for images, labels in trainloader:  
        _# Flatten MNIST images into a 784 long vector_  
        images = images.view(images.shape[0], -1)  
      
        _# Training pass_  
        optimizer.zero_grad()  
          
        output = model(images)  
        loss = criterion(output, labels)  
          
        _#This is where the model learns by backpropagating_  
        loss.backward()  
          
        _#And optimizes its weights here_  
        optimizer.step()  
          
        running_loss += loss.item()  
    else:  
        print("Epoch **{}** - Training loss: **{}**".format(e, running_loss/len(trainloader)))

print("**\n**Training Time (in minutes) =",(time()-time0)/60)
```

1. **Optimizer Initialization**:
   ```python
   optimizer = optim.SGD(model.parameters(), lr=0.003, momentum=0.9)
   ```
   - This line initializes the optimizer. `optim.SGD` stands for Stochastic Gradient Descent, a popular optimization algorithm.
   - `model.parameters()` provides the parameters of the model that need to be optimized.
   - `lr=0.003` sets the learning rate, which controls how much to change the model in response to the estimated error each time the model weights are updated.
   - `momentum=0.9` helps accelerate gradients vectors in the right directions, thus leading to faster converging.

2. **Timing and Epochs**:
   ```python
   time0 = time()
   epochs = 15
   ```
   - `time0 = time()` records the start time to later calculate the total training time.
   - `epochs = 15` sets the number of times the entire training dataset will pass through the network.

3. **Training Loop**:
   ```python
   for e in range(epochs):
       running_loss = 0
       for images, labels in trainloader:
           # Flatten MNIST images into a 784 long vector
           images = images.view(images.shape[0], -1)
   ```
   - The outer loop iterates over the number of epochs.
   - `running_loss = 0` initializes the loss for the current epoch.
   - The inner loop iterates over batches of images and labels from `trainloader`.
   - `images = images.view(images.shape[0], -1)` flattens each image in the batch from a 2D 28x28 image into a 1D vector of length 784.

4. **Training Pass**:
   ```python
   optimizer.zero_grad()
   output = model(images)
   loss = criterion(output, labels)
   ```
   - `optimizer.zero_grad()` clears old gradients from the last step (otherwise they would accumulate).
   - `output = model(images)` passes the images through the model to get predictions.
   - `loss = criterion(output, labels)` calculates the loss between the predicted outputs and the actual labels using the loss function defined earlier (`nn.NLLLoss`).

5. **Backpropagation and Optimization**:
   ```python
   loss.backward()
   optimizer.step()
   ```
   - `loss.backward()` computes the gradient of the loss with respect to the model parameters (backpropagation).
   - `optimizer.step()` updates the model parameters based on the computed gradients.

6. **Loss Accumulation and Logging**:
   ```python
   running_loss += loss.item()
   else:
       print("Epoch **{}** - Training loss: **{}**".format(e, running_loss/len(trainloader)))
   ```
   - `running_loss += loss.item()` accumulates the loss for the current epoch.
   - After the inner loop, the average loss for the epoch is printed.

7. **Training Time Calculation**:
   ```python
   print("**\n**Training Time (in minutes) =", (time()-time0)/60)
   ```
   - This line calculates and prints the total training time in minutes by subtracting the start time from the current time and dividing by 60.

## Testing & Evaluation

We are nearly done with our work. The model is ready, but we have to evaluate it first. I created a utility function **view_classify()** to show the image and class probabilities that were predicted. 

```python
def view_classify(img, ps):
    ''' Function for viewing an image and it's predicted classes.
    '''
    ps = ps.data.numpy().squeeze()
    fig, (ax1, ax2) = plt.subplots(figsize=(6,9), ncols=2)
    ax1.imshow(img.resize_(1, 28, 28).numpy().squeeze())
    ax1.axis('off')
    ax2.barh(np.arange(10), ps)
    ax2.set_aspect(0.1)
    ax2.set_yticks(np.arange(10))
    ax2.set_yticklabels(np.arange(10))
    ax2.set_title('Class Probability')
    ax2.set_xlim(0, 1.1)
    plt.tight_layout()
```


I passed an image to the trained model from the validation set that we created earlier, to see how the model works.

```python
images, labels = next(iter(valloader))  
  
img = images[0].view(1, 784)

with torch.no_grad():  
    logps = model(img)  
  
ps = torch.exp(logps)  
probab = list(ps.numpy()[0])  
print("Predicted Digit =", probab.index(max(probab)))
view_classify(img.view(1, 28, 28), ps)
```

Now we iterate through the validation set using a for loop and calculate the total number of correct predictions. This is how we can calculate the accuracy.

```python
correct_count, all_count = 0, 0  
for images, labels in valloader:  
    for i in range(len(labels)):  
        img = images[i].view(1, 784)  
        with torch.no_grad():  
            logps = model(img)  
        
        ps = torch.exp(logps)  
        probab = list(ps.numpy()[0])  
        pred_label = probab.index(max(probab))  
        true_label = labels.numpy()[i]  
        if true_label == pred_label:  
            correct_count += 1  
        all_count += 1  
  
print("Number Of Images Tested =", all_count)  
print("**\n**Model Accuracy =", (correct_count/all_count))
```

#### Explanation:
This code is evaluating the accuracy of a trained model on a validation dataset.
1. **Initialization**:
    - `correct_count` and `all_count` are initialized to 0. These variables will keep track of the number of correct predictions and the total number of images processed, respectively.
2. **Iterating through the validation data**:
    - `for images, labels in valloader:`: This loop iterates over batches of images and their corresponding labels from the `valloader`, which is a DataLoader object containing the validation dataset.
3. **Iterating through each image in the batch**:
    - `for i in range(len(labels)):`: This loop iterates over each image-label pair in the current batch.
4. **Preparing the image**:
    - `img = images[i].view(1, 784)`: Each image is reshaped into a 1D tensor with 784 elements (assuming the images are 28x28 pixels, typical for datasets like MNIST).
5. **Model prediction**:
    - `with torch.no_grad():`: This context manager disables gradient calculation, which is not needed for inference and saves memory.
    - `logps = model(img)`: The model predicts the log probabilities for each class for the given image.
6. **Calculating probabilities**:
    - `ps = torch.exp(logps)`: The log probabilities are converted to probabilities using the exponential function.
7. **Determining the predicted label**:
    - `probab = list(ps.numpy()[0])`: The probabilities are converted to a list.
    - `pred_label = probab.index(max(probab))`: The index of the maximum probability is taken as the predicted label.
8. **Comparing with the true label**:
    - `true_label = labels.numpy()[i]`: The true label for the image is extracted.
    - `if true_label == pred_label:`: If the predicted label matches the true label, `correct_count` is incremented.
9. **Updating the total count**:
    - `all_count += 1`: The total count of images processed is incremented.
10. **Printing results**:
    - `print("Number Of Images Tested =", all_count)`: Outputs the total number of images tested.
    - `print("**\n**Model Accuracy =", (correct_count/all_count))`: Calculates and prints the model's accuracy as the ratio of correct predictions to the total number of images.




Let’s see the result now. This is the most interesting part!
```
Number Of Images Tested = 10000  
Model Accuracy = 0.9751
```

Wow! We got over 97.5% accuracy. That’s something to celebrate. The reason we got such a high accuracy was that our data-set was clean, had a variety of well-shuffled images and a large number of them. This made our model well prepared to recognize a large number of unseen digits.

## Saving the model

Now that we are done with everything, we do not want to lose the trained model. We don’t want to train it every time we use it. For this purpose, we will be saving the model. When we need it in the future, we can load it and use it directly without further training.

```python
torch**.save**(model, './my_mnist_model.pt') 
```

The first parameter is the model object, the second parameter is the path. PyTorch models are generally saved with `.pt` or `.pth` extension.