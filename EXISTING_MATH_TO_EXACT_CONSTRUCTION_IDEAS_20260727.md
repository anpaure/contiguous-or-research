# Existing mathematics suggested by the exact optima

Date: 2026-07-27

## 1. The new internal target

The certified words suggest that the object to construct is not an arbitrary
covering word.  It is a capacity-ordered OR--Pascal tableau whose central row
is an endpoint-rooted middle-levels path, with three coupled decorations:

1. a near-simple Catalan excess design controlling immediate upper colours;
2. a low-discrepancy residence/hazard chronology controlling all deeper
   shadows; and
3. an interval/Hall factor below the central row.

The first and third items now have exact normal forms.  The open part is the
chronological realization.

This note records four concrete interfaces with existing mathematics.  None
is claimed to solve the problem.

## 2. Rotorize the Catalan chronology

For every nonexceptional fixed (t)-set (Q), the one-hole lower-rainbow
path forces

\[
\text{mean length of a (Q)-containing block}=r/t.
\]

Ideal (q)-window shadows ask for residual survival

\[
\frac{\binom{r-q}{t}}{\binom rt}
=\exp(-qt/r+o(1)),
\]

which is the tail of a geometric clock with hazard (t/r).  This is exactly
the sort of random frequency that rotor-router systems derandomize: local
successors are served cyclically, and occupation/hitting discrepancies can be
smaller than for independent sampling.  See Holroyd--Propp,
[Rotor Walks and Markov Chains](https://arxiv.org/abs/0904.4507), and the
functional-router extension of Shiraga--Yamauchi--Kijima--Yamashita,
[Deterministic Random Walks for Rapidly Mixing Chains](https://arxiv.org/abs/1311.3749).

### Ballot rotor: local theorem, global transversal open

At a lower colour (C\in\binom{[2r-1]}{r-1}), a projected middle-levels
edge chooses two points (a,b\notin C): it deletes (a), adds (b), and
has upper colour (C\cup\{a,b\}).  Give each (C) a cyclic rotor order on
its complement, and make the path choose its outgoing pair according to the
current rotor phase.

This local part can now be done exactly.  Higher-block Euler tours of the
ordered queue enumerate every continuation equally often, giving

\[
F_q(Q)=F_0(Q)\frac{\binom{r-q}{t}}{\binom rt}
\]

for every section and depth in one deterministic high-multiplicity system.
A finite-memory version which forbids coordinate reuse inside an \(H\)-window
is regular of degree \((r-H)(r-1-H)\) and has perfectly uniform aggregate
lower and upper shadows through depth \(H\).

The desired *transversal* theorem would initialize and select rotor states so
that simultaneously:

- every lower (C\ne C_*) is used once;
- every central (r)-set is visited once;
- the induced excess design has (O(r)) factorial energy; and
- for every relevant (Q), the deletion hazard of (Q) has bounded prefix
  discrepancy from (t/r).

The exact ballot-start identities show that the total number of entrances is
already correct, and the Euler cover proves that all local statistics are
compatible.  What remains is reducing the cover's huge multiplicity to one.
A full ordered-queue transversal contains the central subset-Ucycle problem;
the finite-memory \(H=\Theta(\sqrt r)\) version is strictly weaker and is the
cleanest current interpretation of “one choice serves all depths.”  The
proof and scope warning are in `MATH_ROTOR_HAZARD_SCHEDULE_20260727.md`.

## 3. Construct the excess design before the path

Complementing immediate upper colours gives a signed weight

\[
w(A)=\mu^+([2r-1]\setminus A)-1,qquad |A|=r-2,
\]

of forced mass (operatorname{Cat}_r-1).  CPCR zero means
(w=\mathbf1_D) for a simple family

\[
D\subseteq\binom{[2r-1]}{r-2},qquad |D|=\operatorname{Cat}_r-1.
\]

This separates a static design problem from Hamilton chronology.

### Static scaffold: cyclic-orbit rounding (proved)

This candidate can in fact be completed.  Choose both endpoints adjacent to
(C_*), and write (B=[2r-1]\setminus(C_*\cup\{a,b\})).  The forced degree
vector becomes (A-\mathbf1_B).  Since

\[
\gcd(2r-1,r-2)\in\{1,3\},
\]

the Catalan remainder modulo (2r-1) has only three possible forms.  Full
translation orbits, together with one explicit partial-orbit gadget in the
order-three case, give exactly

\[
|D|=\operatorname{Cat}_r-1,qquad d_D(x)=A-\mathbf1_{x\in B}.
\]

Sampling the remaining full orbits without replacement preserves these
vertex degrees exactly and makes every inclusion degree through
(t=O(\sqrt r)) have exponentially small *relative* discrepancy.  The proof
is in `STATIC_EXCESS_DESIGN_CYCLIC_ORBIT_THEOREM_20260727.md`.

This still does not realize (D) by a path.  It gives a much sharper inverse
problem:

> Given a simple Catalan-cardinality excess design (D), find an
> endpoint-rooted middle-levels Hamilton path whose edge unions are doubled
> exactly on the complements of (D).

That is a prescribed-multiplicity Hamilton decomposition problem, rather
than an unstructured shadow-covering problem.

## 4. Use symmetric Gray codes as a scaffold, not as the answer

Gregor--Merino--Mütze construct highly compressed Hamilton cycles in Johnson
graphs and obtain balanced/few-track combination Gray codes; see
[The Hamilton compression of highly symmetric graphs](https://arxiv.org/abs/2205.08126).
Their colour statistic is not our intersection/union pair, so the result does
not solve the problem.  It does offer a deterministic schedule with long
periodic tracks.

Two possible uses survive the audit:

1. start with a compressed Johnson cycle as a hazard-balanced chronology and
   perform alternating circuits until its lower intersection colours become
   rainbow; or
2. use one compressed period as the rotor word in Section 2, while the
   endpoint-rooted middle-levels construction supplies exact ownership.

The decisive invariant to monitor is not ordinary transition balance.  It is
the all-order entrance count

\[
\#\{i:b_i\in Q,\ Q\setminus\{b_i\}\subseteq C_i\},
\]

followed by the truncated local-time profile of the resulting (Q)-blocks.

## 5. Decorated cycle joining

The constructive middle-levels proofs have efficient recursive successor
rules; see Mütze--Nummenpalo,
[A constant-time algorithm for middle levels Gray codes](https://arxiv.org/abs/1606.06172).
Recent bounded-weight universal-cycle constructions also organize enormous
families by necklace concatenation and cycle joining; see
Campbell--Janik-Jones--Sawada,
[Universal cycle constructions for k-subsets and k-multisets](https://arxiv.org/abs/2603.11954).

The useful adaptation would enrich each recursive state by:

- the excess-design choice at its boundary;
- rotor phases for the critical section orders; and
- residence counters truncated at (d+1).

One then joins only conjugate states with identical boundary decorations.
This is more constrained than the published cycle-joining settings, but it
matches the exact finite phenomenon: the lower side is forced Catalan
structure, while all freedom is in the order and decoration of its blocks.

## 6. Root-poset and jeu-de-taquin normalization

The physical intervals ([i,j]), ordered by containment, are the positive-root
poset of type (A); restricting to length at most (d) gives its width-(d)
band.  Equality at (B(k)) assigns the entire punctured lower Boolean ideal
injectively to this band, leaving exactly (e) cells unused, and the OR map
is order-preserving on every nested interval chain.

The selected middle witnesses form two noncrossing endpoint paths

\[
a_i=i+\alpha_i,qquad b_i=i+\beta_i,qquad
\alpha_1\le\cdots\le\alpha_W,quad
\beta_1\le\cdots\le\beta_W.
\]

The flat central derivative is the extreme corridor
(\alpha_i=0,\beta_i=d).  This makes the missing normalization theorem look
like a constrained jeu-de-taquin problem:

1. slide the two endpoint paths to the extreme corridor;
2. slide lower labels so each shortest-depth cut is rank-initial; and
3. after every slide, apply the exact full-witness (Z_b)-criterion rather
   than assuming that monotonicity is enough.

The (k=4) counterexample proves that a single cell slide is insufficient.
A plausible move is therefore an alternating *ribbon* of interval cells,
analogous to the nonlocal alternating circuits already forced in the central
Johnson path.  This gives one common language for the lower normalization and
upper chronology gates: both seek a label-preserving alternating circuit in
a highly structured poset.

## 7. The finite (k=11) incarnation

The same philosophy is already exact at (k=11).  After q1-perfect 3-opt
descent, ten disjoint q2 witness intervals remain.  Choosing one cut from
each exposes twenty ends.  A valid next move is a connected perfect matching
whose new seams:

- form a rainbow permutation of the ten removed lower colours;
- retain all immediate upper colours; and
- pass the static seam-residence test.

The first cut vector is rigid, so the next cut vector must expose a
nontrivial rainbow alternating circuit.  This is the smallest finite test of
the general decorated cycle-joining idea.

## 8. Priority order

1. Solve or refute the twenty-end (k=11) alternating-circuit gate.
2. Prove a bounded-discrepancy ballot-rotor lemma without Hamiltonicity.
3. Solve the inverse transition-system problem for the now-explicit cyclic
   excess design, first allowing many cycles and then cycle-joining.
4. Couple that realization to the rotor/hazard schedule and the lower
   interval compiler.

The first step tests the mechanism; the next two isolate its static and
chronological halves.  A direct attack on all three simultaneously would
discard the main lesson of the exact answers.
