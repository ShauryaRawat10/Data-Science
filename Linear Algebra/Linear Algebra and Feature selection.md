# Linear Algebra and Feature Selection

## Linear Algebra Essentials

- Why Linear Algebra
  - Understand Theory Dimensionality Reduction
    - Retaining most important feature by tranforming into different space
  - Deal with data using Matrices and Vectors

```
At a cutting-edge tech startup, the engineering team is buzzing. The company’s flagship product — an AI system that predicts
house prices — has hit a snag. The performance of the model has suddenly dropped after integrating a new dataset with hundreds of features.

The boss, Dr. Nova, calls in two of her machine learning engineers:
Alex, who has a strong grasp of linear algebra.
Jamie, who mostly relies on plug-and-play machine learning libraries and avoids anything that sounds like "matrix math".
                                               
“We suspect multicollinearity — too many features are redundant or highly correlated. We need to reduce the dimensionality of the data
without losing predictive power. I want each of you to try and solve it your own way. Let’s meet back in a day.”

Jamie’s Approach: Trial and Error
Jamie opens their favorite Python notebook and starts randomly dropping columns and retraining the model. Maybe “Zip Code” and “City”
are redundant? Maybe “Number of Rooms” and “Size in Sq Ft” are correlated?
Hours go by.....
Jamie tries dozens of combinations but can't seem to improve the performance consistently. There’s no clear strategy.
Eventually, Jamie runs a basic correlation heatmap but struggles to interpret it beyond “red is bad?”

Alex’s Approach: Linear Algebra to the Rescue
Alex knows this problem smells like a job for Principal Component Analysis (PCA), a technique grounded in eigenvectors, eigenvalues, and matrix decomposition — the backbone of linear algebra.

Alex performs the following steps:
- Standardizes the data.
- Computes the covariance matrix of the features.
- Finds the eigenvectors and eigenvalues of the covariance matrix.
- Projects the data into a lower-dimensional space, keeping only the components that capture most of the variance.
- Alex not only reduces the number of features from 300 to 15, but also retains 95% of the information. The model trains faster, and performance improves dramatically.
```

#### Vectors
- One-Dimensional object
- Has magnitude (arrow length) and direction
- Magnitude -> ||v||

<img width="299" height="68" alt="image" src="https://github.com/user-attachments/assets/6b71c730-62c6-436b-9105-b519e9af2903" />

- Two types:
  - Row Vectors
  - Column Vectors
 
<img width="467" height="248" alt="image" src="https://github.com/user-attachments/assets/f4473dc8-b2b5-481a-a1b5-2a6f680923d2" />


- Operations
  - Addition and Substration need vectors of same size
  - Dot product is sum of multiplication of vectors

<img width="521" height="296" alt="image" src="https://github.com/user-attachments/assets/3eb595a3-ef46-4d93-8114-afb6114d88d8" />
<br>
<img width="368" height="201" alt="image" src="https://github.com/user-attachments/assets/053a6293-56ba-4853-91cc-329f938f4c6c" />

It always produces scalar

<img width="229" height="112" alt="image" src="https://github.com/user-attachments/assets/35339e82-8f13-490e-a2e0-97c4e5e673c8" />

#### Matrix
- 2 D
- [ $a_n$ ] -> n represent size
- Addition on smae shape matrix
- Multiplication -> number of columns in A should be equal to number of rows in B

<img width="403" height="204" alt="image" src="https://github.com/user-attachments/assets/1f2edb4e-e98f-4566-97ce-2038fa81da89" />

#### Matrix Transformation
- Rotation Transformation
  - Rotates a vector arounfd origin by θ
- Scaling Transformation
  - Change size of vector while keeping its direction

```
Vectors and Matrices: The Language of Intelligence
In school, vectors and matrices often get introduced with a long list of operations: dot products, transposes, row reductions, and so on.
But what gets missed in all of that?

👉 What they actually mean.

Because when you’re working in machine learning or artificial intelligence, you're not just pushing numbers around.
You're thinking in terms of directions, relationships, and compressed representations of the world.

Let’s take a step back — and look at what vectors and matrices really are, and why they power AI.



🧱 What Is a Vector, Really?
A vector is often written like a list of numbers:


But this isn’t just a random list.

A vector represents:
- A direction in space
- A position from the origin

Or — in machine learning — a set of features describing something

Let’s say we’re building a model that predicts housing prices. For one house, the vector might look like this:

That’s a data point. And in ML, every data point is a vector.

Think of a vector as a snapshot of reality: one object, one moment, one state — captured in numbers.



🧩 What’s a Matrix Then?
Now imagine you have 1,000 houses, each with their own vector. What do you get?

A matrix.


Each row is a house → a data point → a vector.
Each column is a feature: size, rooms, distance, etc.

So a matrix in machine learning is usually a dataset. A big, structured table of examples that we want to learn from.

But it’s more than a table.

It’s the foundation for linear transformations — and those are everywhere in AI.



🔄 Vectors and Matrices as Transformations
Let’s say you have an input vector, and you want to transform it — maybe rotate it, scale it, or map it into a new space where it's easier to classify.

That’s what a matrix can do.

If you multiply a vector by a matrix, like this:


You’re changing that vector in a very specific, structured way.

This is exactly what happens in a neural network.

- Each layer of a neural network:
- Takes in a vector (features)
- Multiplies it by a matrix (weights)
- Applies a function (like ReLU or sigmoid)
- Passes the result to the next layer

It’s just vectors flowing through matrices — again and again — until the final output is reached.



🤖 How Does This Relate to Learning?
In machine learning, the goal is often to learn the right matrix.

We have:
- Input vectors (data)
- Output targets (labels or predictions)

And we want to find the weights matrix that transforms the inputs into the correct outputs.

This is where optimization kicks in — adjusting the entries in the matrix to reduce errors. In training, the model updates the numbers in its matrices until it becomes good at mapping inputs to outputs.



🧠 Why This Is Beautiful (and Useful)
Here’s the big idea:
- Vectors represent things (data points, features, directions)
- Matrices represent actions (transformations, relationships, learned behaviors)

Together, they create a language that AI models use to understand patterns, make decisions, and learn from data.
```

#### Transpose of vector or matrices
- Denoted by $X^t$
- Changing rows to columns and vice versa

<img width="307" height="190" alt="image" src="https://github.com/user-attachments/assets/39423501-8458-4652-8865-3ee8aca3e958" />

- Identity Matrix
  - Has 1 in diagonal
  - Multiplying Identity matrix with any matrix with return same matrix 
<img width="292" height="145" alt="image" src="https://github.com/user-attachments/assets/b392a2ff-1e57-408e-b774-9a23e17fa79f" />
<br>
<img width="300" height="179" alt="image" src="https://github.com/user-attachments/assets/60a601e1-18b4-4b97-97ab-56ee10203c07" />

```
Why the Identity Matrix Matters in AI

Here’s where things get really interesting.
In machine learning and neural networks, the identity matrix plays a quiet but crucial role.
Yes, it doesn’t seem to do much. But its real power lies in what it preserves — structure, meaning, stability.

1. 🛠 Initializing Neural Networks
Think of building a neural network like building a robot's brain.
Before the robot learns anything, its brain needs a starting point. Usually, we fill its connections (called weights) with random numbers — like giving it random guesses.
But sometimes, it's better to start with something neutral. That’s where the identity matrix comes in.

Starting with an identity matrix is like saying:

“Okay, don’t change anything yet — just pass the input along as it is.”

It's like giving the robot a blank mind that doesn’t interfere — it simply listens first, and starts learning gradually.

This helps the learning process stay stable, especially in deep networks where many layers are stacked on top of each other.



2. 🔁 Understanding Inverses
In machine learning, we often apply a series of steps (transformations) to data. But sometimes, we need to undo those steps.

Imagine putting on a jacket and then taking it off. The action of taking it off is the inverse of putting it on.

In matrix math, every matrix that has an inverse works the same way:

That means:

"If I do something, and then undo it, I end up back where I started."
The identity matrix is the home position — the original, unchanged state. It helps us define and check if our transformations make sense and can be reversed.



3. 🔄 Gradient Flow in Neural Networks
When an AI learns, it uses a process called backpropagation — a way of sending signals backward through the network to adjust and improve.

But here's the problem: if those signals become too small (or too large), the learning process can break down.

The identity matrix helps keep things steady. In some parts of the learning process, it acts like a clear, direct path for the signal — no twists, no detours.

You can think of it like this:

Imagine you're whispering a message through many people. If each person changes your message even a little, it might be unrecognizable by the end.
But if some people in the chain simply repeat it exactly — like the identity matrix does — the message stays strong.

This helps the AI learn better and faster, especially in deep networks.
```

#### Linear combination of Vectors

<img width="318" height="143" alt="image" src="https://github.com/user-attachments/assets/7bf1f8cf-f5a0-47d8-84a5-7371b73d99c4" />

Lambda can be Integers, Fractions or Zero

<img width="314" height="181" alt="image" src="https://github.com/user-attachments/assets/263f85f3-0af9-4b54-a21f-ff1b4a2afdc5" />

#### Linear Span of Vectors
- Set of all possible combinations of vectors

<img width="312" height="194" alt="image" src="https://github.com/user-attachments/assets/298b3f64-52cd-4aa9-b944-620b9507e664" />

#### Basis vector
- Represented by $e_i$
- Length is 1

<img width="311" height="165" alt="image" src="https://github.com/user-attachments/assets/0f2393a0-ee1a-4cb2-940a-b1b743e34a75" />

<br>
<img width="310" height="171" alt="image" src="https://github.com/user-attachments/assets/123e0784-539e-4968-b500-4567fd25f625" />

<br>

<img width="311" height="207" alt="image" src="https://github.com/user-attachments/assets/1407ec3e-cb45-4e75-b25f-52e9fd348078" />

#### Linear Independence
- A set consists of linearly independent vectors when none of them are in linear span of rest of vectors
- $e_1$ can not be obtained from $e_2$

<img width="308" height="172" alt="image" src="https://github.com/user-attachments/assets/2935c296-4a19-4b8a-91d5-07fdfd4928e2" />

- Linear span of $e_2$ is the set of all vectors multiplied by $e_2$

<img width="306" height="191" alt="image" src="https://github.com/user-attachments/assets/8eb50817-f75c-4b8a-94fb-d327b2bd4713" />

- Linear dependent
  - Set of vectors is linearly dependent if there is linear combination of them with non-zero coefficients that equals zero

<img width="338" height="161" alt="image" src="https://github.com/user-attachments/assets/c576d3ce-9d9f-48f0-a1bf-8bff57af31b5" />

- Linear independent : when no mu holds for vectors
<img width="346" height="95" alt="image" src="https://github.com/user-attachments/assets/85c7796e-cbe9-4259-b8bd-93ff032205d9" />


```
Smart Features, Smarter Models: Why Linear Independence Fuels AI
🔗 Linear Span and Linear Independence:
How AI Knows What’s Useful and What’s Not

When we work with vectors in machine learning, we often deal with lots of data — sometimes hundreds or thousands of features at once.

But not all vectors are equally useful. Some are unique and bring new information. Others just repeat what we already know in a different form.

This is where the two powerful ideas from linear algebra come in:
- Linear span — what vectors can build
- Linear independence — whether a vector is truly new

Let’s break it down.


🧱 Linear Span: What Can These Vectors Build?
Imagine you have two LEGO bricks — a red one and a blue one.

If those bricks are long enough, you can combine them to build a purple wall — by stacking some red and some blue.

That’s the idea of span.

The span of a set of vectors is all the things you can build by mixing them together.

In math, mixing means taking combinations of the vectors — scaling them (multiplying by numbers) and adding them together.

For example:
- The span of two 2D vectors might cover the whole flat plane.
- But the span of just one vector can only reach points along its direction — a line.

In AI, this is important because it tells us:

“What space of possibilities can my features represent?”

If your features span a large space, your model has more flexibility to learn. If they only span a small space, it might miss important patterns in the data.



✂️ Linear Independence: Are These Vectors Saying the Same Thing?
Now let’s say you have three LEGO bricks — red, blue, and purple.

But wait… the purple one is just a mix of the red and blue. It’s not really new — you could’ve built it from what you already had.

That’s linear dependence.

A set of vectors is linearly independent if none of them can be built by combining the others.

If one can be written using the others, it’s dependent — and kind of redundant.

In machine learning, linear independence helps us avoid duplicated or useless features. It helps answer questions like:
- Do I really need all these features?
- Am I just repeating the same information in different forms?
- Can I compress my data without losing power?

Techniques like PCA (Principal Component Analysis) are all about finding the smallest number of independent vectors that can still span the space of your data. We'll talk more about PCA in the lessons to come. :) 



🤖 Why It Matters in Machine Learning
Let’s connect this to AI in a simple way:
- The span tells you how much your features can express — what patterns your model can potentially learn.
- Independence tells you how much of your data is actually useful — and not just noise or repetition.

In real-world machine learning:
- We want features that are independent, so they each bring new information.
- We want a large span, so our model has room to learn complex things.
- And sometimes, we want to reduce features — but keep the same span — by removing redundant ones.
```

#### Vector Space
- A set of vectors that can be added and substracted together, as well as multiplied by numbers called scalars

<img width="310" height="194" alt="image" src="https://github.com/user-attachments/assets/946bc1d8-0eec-405a-a1aa-c636c4badf89" />

#### Basis of Vector space
- A set of vectors whose number equals the dimension of that space
- A set of vectors that are linearly independent of each other. Their linear span is the entirety of vector space
- Think it of, smallest set of vectors that generates the vector space

Lets check linear independent $e_1$ and $e_2$  

<img width="311" height="125" alt="image" src="https://github.com/user-attachments/assets/29cc1fdb-7395-48c3-afb8-f33287029428" />

- we can see that $e_1$ and $e_2$ can span this vector and also whole dimensional space
- $e_1$ and $e_2$ form a basis


#### Determinant of a Matrix
- A number obtained from any square matrix
- Identifies whether it is invertible or not (Not all matrix can be inverted)

<img width="300" height="46" alt="image" src="https://github.com/user-attachments/assets/f39b82e1-2956-45b7-93bb-bdb18fbec49b" />

<br>
- A matrix is invertible if it is Square matrix and its determinant is not equals zero

<img width="305" height="181" alt="image" src="https://github.com/user-attachments/assets/3bfda2b2-3561-4b20-8719-1813c3029940" />

<br>

<img width="308" height="115" alt="image" src="https://github.com/user-attachments/assets/1334124a-1ed2-47fd-b56c-82e27c8092f8" />

#### Inverse of Matrix
<img width="346" height="187" alt="image" src="https://github.com/user-attachments/assets/e4f4993a-8092-4b34-b90b-f36b4bb37d68" />

<br>

<img width="347" height="182" alt="image" src="https://github.com/user-attachments/assets/d845df14-5586-4149-8e90-227fef338c31" />
<br>

<img width="350" height="196" alt="image" src="https://github.com/user-attachments/assets/0ceaff56-5348-44cb-aeae-caad759da6bd" />


```
Basis, Determinant, and Inverse — The Backbone of Machine Learning Math
If AI models were buildings, then vectors and matrices would be the bricks and beams. But how those bricks are arranged, how stable the structure is, and whether you can reverse-engineer it — that’s what these three ideas tell us:

- Basis – the essential building blocks
- Determinant – the stability check
- Inverse – the undo button

Let’s take them one by one — and show how they quietly shape what machines can understand and do.



🧱 1. Basis: The Smallest Set That Builds Everything
Imagine you’re designing a LEGO set. You want the fewest bricks possible, but you still want to build anything in the set's theme.

That’s what a basis is in a vector space.

A basis is the minimum set of independent vectors you need to build everything else in the space — just by scaling and adding them.

In 2D, two independent vectors (not pointing in the same direction) can form a basis. Together, they can generate any point on the plane. In 3D, you need three such vectors.

In AI:
- A basis tells us the dimension of the feature space (how many truly unique features we have).
- Finding a smaller basis means we can compress data without losing its structure — just like reducing a sentence to its key ideas.
- This is the idea behind dimensionality reduction methods like PCA, which help models focus only on what really matters.



📏 2. Determinant: A Test for Volume — and Stability
The determinant sounds intimidating, but it’s really just a number that answers one big question:

“Does this matrix squash space down to zero — or does it keep space open and usable?”

In geometric terms, the determinant tells you the volume scaling of a matrix transformation.

If the determinant is 0, it means your matrix collapses space — everything lies flat, and you lose a dimension.

If the determinant is non-zero, you’re good — the space is preserved (just stretched or rotated).

In AI:
- A determinant of zero means some features are redundant or linearly dependent — there’s no unique solution to a system.
- It helps us detect when a matrix is invertible — which leads us to the next concept.



🔄 3. Inverse: Undoing a Transformation
Ever wish you could hit Undo on something? In linear algebra, the inverse of a matrix does exactly that.

If matrix A transforms a vector in a certain way, the inverse of A brings it back to where it started. (That I is the identity matrix — our do-nothing hero from earlier.)

But not all matrices have inverses. A matrix only has an inverse if:
- Its determinant isn’t zero
- Its columns are linearly independent
- It’s a square matrix (same number of rows and columns)

In AI:

We use matrix inverses to solve systems of equations, especially in linear regression (eq below):

```
$\hat{w}=(X^{T}X)^{-1}X^{T}y$


#### Solving equation of form Ax=b
<img width="300" height="133" alt="image" src="https://github.com/user-attachments/assets/9c308fd4-4b91-4b22-84f5-d87e543cb528" />

#### The Gauss Method

<img width="311" height="125" alt="image" src="https://github.com/user-attachments/assets/11405eff-43a4-4828-993f-bfe8e780da41" />
<br>

- Scaling 2nd matrix by 5
<img width="350" height="122" alt="image" src="https://github.com/user-attachments/assets/383e1d3b-021b-4148-83f1-aa05f6cb99d9" />
<br> 

- main aim is to get as many zeros as we can
- for the final augmneted matrix, system of equations will be

<img width="348" height="189" alt="image" src="https://github.com/user-attachments/assets/807ffc33-81c1-4667-a702-407b4a700e0c" />
<br>

<img width="326" height="202" alt="image" src="https://github.com/user-attachments/assets/842588c9-2d1d-4eda-9c18-e2cc7941117c" />

<br>

<img width="308" height="189" alt="image" src="https://github.com/user-attachments/assets/c1790e2e-8553-4c28-8334-d1ff7947f663" />

#### Linear Independence of Random set of variables
- It is linearly indepedent when lamba is 0
<img width="306" height="125" alt="image" src="https://github.com/user-attachments/assets/2f74aa49-f16c-469b-b263-1f374e079a5b" />

<br>
<img width="304" height="86" alt="image" src="https://github.com/user-attachments/assets/f5c3a34f-812f-4dd4-ba8d-7f33003197b0" />
<br>
<img width="292" height="87" alt="image" src="https://github.com/user-attachments/assets/353c1c86-ee1e-4b93-9079-45be365c202f" />
<br>
<img width="302" height="140" alt="image" src="https://github.com/user-attachments/assets/7afa4ba0-e679-4770-8cc0-24abce2672b1" />
<br>
<img width="305" height="122" alt="image" src="https://github.com/user-attachments/assets/71976278-e4a5-4508-a8cb-74deececfe76" />
<br>
<img width="290" height="140" alt="image" src="https://github.com/user-attachments/assets/6c52cfc0-7ad6-48fe-b873-8a3beb2db747" />
<br>
<img width="301" height="134" alt="image" src="https://github.com/user-attachments/assets/383b97b2-9fd4-46a1-bba1-9d2817b3ab87" />
- lambda's came as 0

<hr>

## Eigenvalues and Eigenvectors

<img width="348" height="187" alt="image" src="https://github.com/user-attachments/assets/6c4fc490-bc59-4126-af14-a2edc65f3187" />
<br>
<img width="349" height="184" alt="image" src="https://github.com/user-attachments/assets/182dd585-a1ff-4461-bd28-b79e30085b08" />

- **Eigenvalue**
  - A scalar with one or multiple eigenvectors
  - Any time we define eigenvector, we must specify its eigenvalue as well
  - Single eigenvalue can have many eigenvectors


























