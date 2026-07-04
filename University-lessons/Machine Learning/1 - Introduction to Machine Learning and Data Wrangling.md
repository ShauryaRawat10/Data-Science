# Introduction to Machine Learning

### Definition:
A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E,

### AI Research Computer Vision

#### 1. Quantum Materials for Computer Vision
- Traditional cameras use RGB filters, which lose a lot of spectral information.
- Researchers are using **Transition Metal Dichalcogenides (TMDs)** to capture richer optical information without relying only on RGB.
- AI receives a more detailed spectral signature, improving color recognition and object detection.
- Potential applications: autonomous vehicles, satellite imaging, agriculture, industrial inspection, and medical imaging.

**Key takeaway:** Better sensors → Better data → Better AI predictions.

---

#### 2. Neuromorphic & Photonic Computing
- Current AI hardware is limited by data movement and energy consumption.
- Researchers are developing **brain-inspired (neuromorphic)** chips that communicate using **photons (light)** instead of electrical signals.
- Artificial synapses built with **superconducting single-photon detectors** and **Josephson junctions** could enable ultra-fast, energy-efficient AI hardware.
- This technology is still in the research stage but has the potential to transform future AI systems.

**Key takeaway:** Future AI breakthroughs will come from both **better algorithms** and **next-generation hardware**.


### Board Games AlphaGo Notes

- **Go** is one of the oldest and most complex board games, with more possible board configurations than the estimated number of atoms in the universe.
- Traditional AI struggled with Go because brute-force search is impractical.
- **AlphaGo**, developed by **DeepMind**, learned to play using **deep learning** and **reinforcement learning**, rather than relying only on predefined rules.
- In 2016, AlphaGo defeated world champion **Lee Sedol**, marking a historic breakthrough in AI.
- The victory demonstrated that AI can master problems requiring intuition, pattern recognition, and long-term strategic planning.
- AlphaGo's underlying ideas have influenced modern AI research and continue to shape advances in reinforcement learning and decision-making systems.

**Key takeaway:** AlphaGo proved that AI can learn complex strategies through experience, opening the door to solving real-world problems far beyond board games.

### Voice Recognition
- Their voice is compared with a stored voiceprint which captures more than 140 unique physical and behavioural characteristics of a person such as length of the vocal tract and nasal passage, the size and shape of the larynx, pitch, cadence and accent
- Technologies such as Siri and Google Home are examples of this. Siri uses speech recognizer, natural language processing and text-to-speech techniques


***
### Some Studies in Machine Learning Using the Game of Checkers (1959)

#### Techniques Used

#### 1. Minimax Search
- Explores possible future game states.
- Assumes the opponent always plays optimally.
- Chooses the move with the highest worst-case outcome.

#### 2. Look-Ahead Search
- Searches multiple moves (plies) into the future.
- Uses dynamic search depth depending on board complexity.

#### 3. Heuristic Evaluation Function
- Scores board positions using handcrafted features.
- Features include:
  - Piece advantage
  - King advantage
  - Mobility
  - Center control
  - Piece advancement
- Used when full search is computationally infeasible.

#### 4. Rote Learning (Memory-Based Learning)
- Stores previously evaluated board positions.
- Reuses stored evaluations instead of recomputing.
- Improves search efficiency over time.

#### 5. Self-Play
- Program plays against itself.
- Generates training experience without human data.
- Continuously improves through repeated games.

#### 6. Automatic Weight Adjustment
- Learns the importance (weights) of board features.
- Updates evaluation function based on game outcomes.
- Early form of parameter optimization.

#### 7. Generalization
- Instead of memorizing every board state, learns general evaluation rules.
- Selects useful features and discards less useful ones over time.

#### 8. Memory Management
- Stores only valuable board positions.
- Uses aging, refreshing, and forgetting strategies to limit memory usage.

#### Key AI Concepts Introduced
- Adversarial Search
- Heuristic Search
- Self-Learning
- Experience-Based Learning
- Feature Engineering
- Parameter Optimization
- Search + Learning Hybrid

#### Legacy
This work laid the foundation for modern Reinforcement Learning, self-play systems (AlphaGo/AlphaZero), heuristic search, and learning-based game AI.



