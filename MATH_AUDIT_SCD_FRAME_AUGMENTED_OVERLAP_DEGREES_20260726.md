# Augmented SCD frames: exact overlap degrees and the short-cycle closure barrier

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The \(W^{o(1)}\) frame augmentation has an exact and useful marginal degree
calibration.  If \(J=\lceil4m/p_H\rceil\) global random frames are used, then
every owner has \(\Theta(m)\) successful states, and every admissible choice
for its first lower mate receives \(\Theta(1)\) states in expectation.  Thus
the catalogue is at the natural \(\Theta(\log W)\) degree scale for a random
bipartite perfect matching.

That marginal statement does not touch the principal cut.  After choosing the
arbitrary length-\(H\) extensions used in the frame construction, the ordered
deletion word

\[
 d(X)=(d_1(X),\ldots,d_H(X))                                    \tag{0.1}
\]

is fixed before the frame is chosen.  Its first \(r_X\) letters are forced by
the SCD chain and its remaining letters are the chosen extension.  A frame
only attaches mates to these letters.  Therefore every state above the same
owner projects to the same
de Bruijn arc

\[
 (d_1,\ldots,d_{H-1})\longrightarrow(d_2,\ldots,d_H).             \tag{0.2}
\]

Every union of directed cycles is Eulerian in this projection.  Hence the
prefix/suffix imbalance

\[
 \Delta_{\rm seq}
 ={1\over2}\sum_\theta
 \left|
 \#\{X:(d_1,\ldots,d_{H-1})=\theta\}
 -
 \#\{X:(d_2,\ldots,d_H)=\theta\}
 \right|                                                         \tag{0.3}
\]

is a frame-independent, statewise lower bound on the number of discarded
owners within that fixed extension-based bundling model.  If
\(\Delta_{\rm seq}\not=o(W/H)\), no choice from that augmented catalogue can
prove constant one.  Changing the arbitrary extensions can change
\(\Delta_{\rm seq}\); this remains a design freedom.

There is a second exact cut: the raw SCD-overlap digraph contains every
possible owner transition, independent of frames.  Any catalogue transition
graph is a subgraph, so every Hall deficiency of the raw graph is inherited.

Finally, a random-regular directed-factor heuristic is not a viable substitute
for the required \(2h\)-closure.  A random digraph on \(W=\exp(\Theta(m))\)
vertices with polynomial degree has only an \(o(1)\) fraction of its vertices
on cycles of length \(2h\) whenever \(h=o(m/\log m)\).  The desired short
cycles must therefore be algebraically planted (as in a cube factor), not
obtained from a generic perfect matching.

No cycle-cover theorem is proved.  The exact surviving positive target is:
choose the SCD/flag resolution so that (0.3) and every raw Hall cut are
\(o(W/H)\), then choose common global frames whose planted cube cycles respect
those overlaps.

## 1. Exact distribution of successful frame states

Fix an owner \(X\), and extend its SCD lists to length \(H\) exactly as in the
frame-existence proof.  Write the resulting marked lower deletions as

\[
 a_1,\ldots,a_H\in X                                             \tag{1.1}
\]

and its marked upper additions as

\[
 b_1,\ldots,b_H\in X^c.                                          \tag{1.2}
\]

Put

\[
 A=X\setminus\{a_1,\ldots,a_H\},\qquad
 B=X^c\setminus\{b_1,\ldots,b_H\},\qquad |A|=|B|=m-H.             \tag{1.3}
\]

A successful frame pairs every \(a_i\) to a distinct element \(c_i\in B\)
and every \(b_i\) to a distinct element \(e_i\in A\).  Let

\[
 M_H=(m-H)_{\underline H}.                                       \tag{1.4}
\]

The exact success probability from the flag construction is

\[
 p_H={M_H^2\over\prod_{i=0}^{2H-1}(2m-2i-1)}.                    \tag{1.5}
\]

Let \(\gamma_{m,H}\) be the conditional probability that the resulting owner
type lies in the enlarged balanced band.  The proof of the flag theorem gives

\[
                         {1\over2}\le\gamma_{m,H}\le1.             \tag{1.6}
\]

Write

\[
                         p_H^{\rm bal}=\gamma_{m,H}p_H.           \tag{1.7}
\]

### Lemma 1.1 (uniform collar injections)

Conditional on balanced success, the lower mate injection
\((c_1,\ldots,c_H)\) and the upper mate injection
\((e_1,\ldots,e_H)\) are independent and uniform over the \(M_H\)
possibilities.

#### Proof

After fixing the two injections, \(2H\) cross-pairs have been exposed.  The
remaining \(2m-4H\) vertices carry a uniform perfect matching.  Its two
owner shores both have size \(m-2H\), independent of the names in the fixed
injections.  Consequently the distribution of the remaining number of full
owner pairs, and hence the balanced-type event, is the same for every pair
of injections.  Symmetry proves uniformity and independence. \(\square\)

Now choose \(J\) independent global frames.  For each owner let
\(I_X\subseteq[J]\) be its set of balanced successful frame indices.

### Proposition 1.2 (exact marginal degrees)

For every owner \(X\),

\[
 |I_X|\sim {\rm Bin}(J,p_H^{\rm bal}),\qquad
 2m+o(1)\le {\mathbb E}|I_X|\le4m+o(m)                            \tag{1.8}
\]

when \(J=\lceil4m/p_H\rceil\).

For a prescribed ordered lower prefix
\(\mathbf c=(c_1,\ldots,c_k)\), \(1\le k\le H\),

\[
 \#\{j\in I_X:
      (P_j(a_1),\ldots,P_j(a_k))=\mathbf c\}
 \sim {\rm Bin}\left(J,{p_H^{\rm bal}\over(m-H)_{\underline k}}\right).
                                                                         \tag{1.9}
\]

For prescribed complete lower and upper injections \(\mathbf c,\mathbf e\),

\[
 \#\{j\in I_X:P_j(\mathbf a)=\mathbf c,\ P_j(\mathbf b)=\mathbf e\}
 \sim {\rm Bin}\left(J,{p_H^{\rm bal}\over M_H^2}\right).          \tag{1.10}
\]

#### Proof

The frames are independent in the index \(j\).  Equations (1.8)--(1.10)
follow directly from Lemma 1.1. \(\square\)

In particular, for a prescribed first lower mate,

\[
 {\mathbb E}\#\{j\in I_X:P_j(a_1)=c\}
 ={Jp_H^{\rm bal}\over m-H}
 \in[2+o(1),4+o(1)].                                              \tag{1.11}
\]

Thus the factor \(4m\) in the catalogue size is exactly the scale at which
each of the \(\Theta(m)\) first-successor choices receives constant expected
multiplicity.

The frames are global, so the random variables for different owners are
correlated.  Equations (1.8)--(1.11) are exact owner marginals; they do not
give pair degrees or Hall expansion.

## 2. The frame-independent de Bruijn projection

For every owner, using the chosen length-\(H\) extension, define

\[
 p(X)=(d_1(X),\ldots,d_{H-1}(X)),\qquad
 s(X)=(d_2(X),\ldots,d_H(X)).                                    \tag{2.1}
\]

Let

\[
 b_\theta=\#\{X:p(X)=\theta\},\qquad
 a_\theta=\#\{X:s(X)=\theta\}.                                   \tag{2.2}
\]

Every successful frame state above \(X\) decorates the same directed arc
\(p(X)\to s(X)\).  If one state is selected per owner, the projected in- and
out-degrees are therefore **exactly**

\[
 d^+(\theta)=b_\theta,\qquad d^-(\theta)=a_\theta,                 \tag{2.3}
\]

independent of \(J\), \(p_H\), and the selected frames.

If all successful states are retained as parallel arcs, then

\[
 d^+_{\rm all}(\theta)=\sum_{X:p(X)=\theta}|I_X|,\qquad
 d^-_{\rm all}(\theta)=\sum_{X:s(X)=\theta}|I_X|,                  \tag{2.4}
\]

and hence

\[
 {\mathbb E}d^+_{\rm all}(\theta)
 =Jp_H^{\rm bal}b_\theta,\qquad
 {\mathbb E}d^-_{\rm all}(\theta)
 =Jp_H^{\rm bal}a_\theta.                                        \tag{2.5}
\]

The augmentation multiplies the imbalance in expectation; it never changes
its support.

### Theorem 2.1 (Eulerian signature cut)

Every owner-disjoint union of compatible directed cycles discards at least

\[
 \boxed{\Delta_{\rm seq}={1\over2}\sum_\theta|a_\theta-b_\theta|} \tag{2.6}
\]

owners from the depth-\(H\) active core.

#### Proof

Selected owners form selected arcs \(p(X)\to s(X)\).  A union of directed
cycles has equal selected indegree and outdegree at every signature
\(\theta\).  Initially the imbalance is \(b_\theta-a_\theta\).  Deleting one
owner arc changes the \(\ell_1\)-norm of the imbalance vector by at most two.
To reach zero therefore requires at least half its initial \(\ell_1\)-norm
many deletions. \(\square\)

This is a literal dual cut.  It depends only on the ordered extended deletion
table and survives every frame augmentation, every random choice, and every
cycle absorber required to respect that table.  It does not survive
re-choosing the arbitrary suffixes of chains with \(r_X<H\).

## 3. The raw owner-overlap graph and its Hall cut

The signature balance (2.6) is not the only statewise obstruction.  Define
the raw directed graph \(\mathcal R_H\) on the owners with their chosen
length-\(H\) extensions by \(X\to Y\) when:

1. \(X\) and \(Y\) are Johnson neighbours;
2. \(X\setminus Y=\{d_1(X)\}\); and
3. \(d_i(Y)=d_{i+1}(X)\) for \(1\le i<H\).

Append the analogous upper/backward collar equalities when the two-sided
flag convention requires them.

For a frame \(P_j\), the only possible successor of \(X\) is

\[
 S_j(X)=X-\{d_1(X)\}+\{P_j(d_1(X))\}.                              \tag{3.1}
\]

Hence every legal catalogue transition is an arc of \(\mathcal R_H\).

### Proposition 3.1 (raw Hall cut)

Let \(\Gamma\) be any transition graph obtained by selecting arbitrary
successful frame states from the augmented catalogue.  Then

\[
 N_\Gamma^+(Z)\subseteq N_{\mathcal R_H}^+(Z)
 \quad\text{for every }Z\subseteq\Omega,                           \tag{3.2}
\]

and every cycle packing in \(\Gamma\) leaves at least

\[
 \boxed{
 \Delta_{\rm Hall}(\mathcal R_H)
 =\max_{Z\subseteq\Omega}
   \big(|Z|-|N_{\mathcal R_H}^+(Z)|\big)_+}                        \tag{3.3}
\]

owners.

#### Proof

Equation (3.1) and the deletion-word overlap give (3.2).  A vertex-disjoint
cycle packing is, after splitting tails and heads, a bipartite matching from
every covered owner to a distinct successor.  Hall's deficiency theorem and
(3.2) give (3.3). \(\square\)

For exact catalogue degree bookkeeping, define

\[
 p_{XY}=
 \Pr\left[
 \begin{array}{l}
 P\text{ is balanced-successful at both }X,Y,\\
 S_P(X)=Y,\text{ and all lower/upper overlaps hold}
 \end{array}
 \right].                                                        \tag{3.4}
\]

For \(J\) independent global frames, the number of frame-labelled arcs from
\(X\) to \(Y\) is

\[
                         {\rm Bin}(J,p_{XY}),                      \tag{3.5}
\]

and the exact expected owner degrees are

\[
 {\mathbb E}d_\Gamma^+(X)=J\sum_Yp_{XY},\qquad
 {\mathbb E}d_\Gamma^-(Y)=J\sum_Xp_{XY}.                           \tag{3.6}
\]

Moreover,

\[
 p_{XY}=0\quad\text{unless }X\to Y\text{ in }\mathcal R_H,         \tag{3.7}
\]

and the necessary first-mate event gives the uniform upper bound

\[
 p_{XY}\le {p_H^{\rm bal}\over m-H}.                              \tag{3.8}
\]

Equations (3.4)--(3.8) are exact.  A useful lower bound on \(p_{XY}\) requires
joint information about the two SCD collars; it does not follow from the
one-owner success probability \(p_H\).

## 4. What the marginal degree can and cannot prove

Since

\[
                         \log W=(2\log2+o(1))m,                    \tag{4.1}
\]

the marginal state degree \(\Theta(m)\) is of order \(\log W\), the usual
threshold scale for a random bipartite perfect matching.  This calibration is
real: if the raw graph had linear-in-\(m\) degree, if compatible arcs survived
with comparable probabilities, and if the resulting graph behaved randomly,
one would expect Hall's condition.

None of those italicized properties follows from the SCD flag theorem.
The deterministic cuts (2.6) and (3.3) occur before the random frames.  In
particular, no concentration argument for \(|I_X|\) can repair an imbalanced
deletion-word flow.

There is also a separate closure problem.  A perfect bipartite matching gives
an arbitrary permutation of the owners.  It does not force its components to
have length \(2h\), and it does not force the transition word on a component
to be \(\sigma\sigma\).

## 5. Generic sparse digraphs do not supply the short cycles

The following elementary calculation explains why a random-regular directed
factor is the wrong closure model.

### Proposition 5.1 (short-cycle scarcity)

Let \(D\) be a random directed graph on \(W\) labelled vertices in which every
vertex chooses at most \(d\) independent uniform out-neighbours.  For any
\(\ell\ge2\), the expected number of vertices lying on a directed
\(\ell\)-cycle is at most

\[
                         d^\ell.                                  \tag{5.1}
\]

Consequently, if \(d=m^{O(1)}\), \(W=\exp(\Theta(m))\), and
\(\ell=2h=o(m/\log m)\), then an \(o(1)\) fraction of the vertices lies on
an \(\ell\)-cycle with high probability.

#### Proof

For a fixed vertex \(v\), there are at most \(d^\ell\) directed length-\(\ell\)
choice sequences starting at \(v\).  The terminal vertex of each sequence is
uniform, so the probability that one returns to \(v\) is at most
\(d^\ell/W\).  Thus the expected number of vertices on such a cycle is at
most \(W(d^\ell/W)=d^\ell\).  Markov's inequality proves the last assertion.
\(\square\)

The model in Proposition 5.1 is only a calibration; the global-frame graph is
correlated and may contain planted cube cycles.  Its conclusion is strategic
but sharp: any proof treating the \(\Theta(m)\) successor choices as generic
random edges cannot produce an almost-spanning \(C_{2h}\)-factor in the
mesoscopic range.  The \(2h\)-cycles must come from an algebraic resolution
already present inside the frames.

## 6. The exact positive target

The frame augmentation solves the marginal existence problem:

\[
                         |I_X|=\Theta(m)                            \tag{6.1}
\]

for every owner after the standard union-bound choice.  To turn this into a
cycle theorem, one still needs all of the following.

1. **Euler balance:** \(\Delta_{\rm seq}=o(W/H)\).
2. **Raw Hall expansion:** \(\Delta_{\rm Hall}(\mathcal R_H)=o(W/H)\).
3. **Joint frame degrees:** enough \(p_{XY}\)'s must be comparable to
   \(p_H/m\), uniformly through every relevant residual cut.
4. **Planted closure:** the retained arcs must contain all but \(o(W/H)\)
   owners in algebraic \(2h\)-cycles with word \(\sigma\sigma\).
5. **Upper compatibility:** the backward collar must be satisfied by the
   same cycles and frames.

Items 1 and 2 are properties of the chosen SCD/extended-flag resolution, not
of the augmentation.  Item 3 is a two-owner frame count.  Item 4 cannot be replaced
by a random permutation argument.  Item 5 is the simultaneous two-sided
constraint.

The first exact decision test is therefore (2.6): compute or prove the
prefix/suffix balance of the selected SCD together with its chosen extensions.
If it is not \(o(W/H)\), that fixed augmented-frame lane is impossible without
changing the extension or nested flag resolution.  If it vanishes, the next
exact test is the raw Hall deficiency (3.3), followed by the joint
probabilities (3.4).

## 7. Final verdict

The \(W^{o(1)}\) catalogue is calibrated correctly but solves the wrong
degree by itself.  It supplies \(\Theta(m)\) states per owner and constant
expected multiplicity per first mate, while the de Bruijn in/out degrees are
fixed by the SCD deletion table.  A frame choice decorates an SCD arc; it
does not move it.

The surviving gate is consequently one level earlier than a random cycle
cover: construct an exact nested flag factor whose deletion words are almost
Eulerian and whose raw overlap digraph has an almost-perfect matching, while
retaining an algebraically planted \(C_{2h}\)-resolution.  No such construction
or statewise contradiction is currently proved.
