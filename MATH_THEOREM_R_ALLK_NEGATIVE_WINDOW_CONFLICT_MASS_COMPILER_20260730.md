# Negative-window conflict hypergraphs and a bounded-augmentation compiler theorem

Date: 2026-07-30  
Lane: R, all-`k` compiler/Hall route  
Status: unconditional fixed-chronology theorems.  The main result gives an
exact independent-transversal obstruction for unrestricted `COMP_d(T)` and
a rigorous `B(k)+C` sufficient theorem from conflict mass at most `C`.  It
does **not** prove that the required carrier or bounded-mass distribution
exists uniformly in `k`.

## 0. Verdict

Put

\[
 r=\lceil k/2\rceil,
 \qquad W={k\choose r},
 \qquad \Lambda=\sum_{s=1}^{r-1}{k\choose s},
\]

and let

\[
 d=d(k)=\min\left\{j\ge0:jW+{j+1\choose2}\ge\Lambda\right\},
 \qquad B(k)=W+d.
\]

For a fixed linearly `d`-resident rank-`r` chronology `T`, unrestricted
`COMP_d(T)` is not an ordinary matching problem: two witness intervals which
use different physical cells can jointly delete the last two occurrences of
one coordinate from a required middle window.  The exact replacement is a
finite **negative-window conflict hypergraph**.  Its vertices are proposed
target/witness-interval pairs, and its hyperedges are the inclusion-minimal
families which kill a middle coordinate, kill a positive coordinate of one
selected target, or empty one source position.

The hypergraph has rank at most

\[
 \rho(T)=\max\left\{d+1,\max_p|P_p|\right\},             \tag{0.1}
\]

and hence at most `r` when `d<r`.  Its independent-transversal deficiency
`tau(T)` is exactly the minimum number of lower masks missed by any nonzero
antecedent `A` with `D^dA=T`.  Thus

\[
 \boxed{\quad \operatorname{COMP}_d(T)\text{ is feasible}
        \iff \tau(T)=0.\quad}                            \tag{0.2}
\]

If `T` is also upper-complete, then appending the `tau(T)` missing masks as
literal letters gives

\[
                         \nu(k)\le B(k)+\tau(T).          \tag{0.3}
\]

There is a useful probabilistic/weighted form.  Choose one candidate
interval for each nonexceptional lower target independently.  If `Psi` is
the sum, over all conflict hyperedges, of the product of their selected
vertex probabilities, then

\[
 \boxed{\quad
 \nu(k)\le B(k)+|O|+\lfloor\Psi\rfloor,
 \quad}                                                  \tag{0.4}
\]

where `O` is any target family omitted before sampling.  In particular,
`Psi<1` and `O=emptyset` prove the sharp formula, while
`|O|+Psi=O(1)` proves `B(k)+O(1)`.

This is a reusable theorem, not a completed all-`k` construction.  The
precise remaining assertion is now either

\[
 \tau(T_k)=O(1)                                         \tag{0.5}
\]

for one upper-complete resident chronology in every dimension, or the
stronger checkable product-distribution estimate

\[
 |O_k|+\Psi(T_k;O_k,\pi_k)=O(1).                        \tag{0.6}
\]

The Pascal flag transports and bounded seam count alone do not imply
(0.5): a single separated seam has exactly `binom(d,2)` crossing short
intervals.  The exact missing seam condition is that all but `O(1)` of the
targets whose internal providers were removed are reproduced by the new
cross-seam interval ledger.

## 1. Fixed chronology and maximal erosion

The case `d=0` has no lower target burden and is immediate.  Throughout
Sections 1--7 assume

\[
                         1\le d<r.                       \tag{1.1}
\]

Let

\[
 T=(T_0,\ldots,T_{W-1})
\]

list every rank-`r` mask exactly once.  Put `n=W+d`, `J={0,...,n-1}`, and
define the maximal erosion

\[
 P_p=\bigcap_{i=\max(0,p-d)}^{\min(p,W-1)}T_i
 \qquad(p\in J).                                        \tag{1.2}
\]

Assume `T` is linearly `d`-resident.  The residence theorem then gives

\[
                         D^dP=T,                         \tag{1.3}
\]

and every `P_p` is nonempty.  Every antecedent `A` with `D^dA=T` obeys

\[
                         \varnothing\ne A_p\subseteq P_p.\tag{1.4}
\]

For later pruning, let `F_p` be any certified mandatory core contained in
every such `A_p`.  On every flat interior controller position one may take

\[
 F_p=(P_p\setminus P_{p-1})\cup(P_p\setminus P_{p+1}), \tag{1.5}
\]

and take `F_p=\varnothing` where this displayed interior formula is not
applicable.  The run-boundary pair lemma proves `F_p\subseteq A_p`.

Let `I_d` be the family of all nonempty source intervals of length at most
`d`.  For `I in I_d`, write

\[
 P(I)=\bigcup_{p\in I}P_p,
 \qquad F(I)=\bigcup_{p\in I}F_p.                       \tag{1.6}
\]

If `I` witnesses a target `S`, then necessarily

\[
                         F(I)\subseteq S\subseteq P(I). \tag{1.7}
\]

Thus (1.7) is an exact safe pruning rule for candidate intervals.  It is
not sufficient by itself.

## 2. Deadline slack equals compulsory short-window waste

The number of source intervals of lengths one through `d` is

\[
 M_d(n)=\sum_{j=1}^d(n-j+1)
       =dn-{d\choose2}
       =dW+{d+1\choose2}.                              \tag{2.1}
\]

Define the exact deadline slack

\[
 \sigma= M_d(n)-\Lambda
        =dW+{d+1\choose2}-\Lambda\ge0.                 \tag{2.2}
\]

For a nonzero antecedent `A` with `D^dA=T`, let

\[
 \mu_A(S)=\#\left\{I\in\mathcal I_d:
                    \bigcup_{p\in I}A_p=S\right\}.     \tag{2.3}
\]

Let `h(A)` be the number of nonempty masks of rank below `r` with
`mu_A(S)=0`, let

\[
 C_<(A)=\sum_{1\le |S|<r}(\mu_A(S)-1)^+,              \tag{2.4}
\]

and let

\[
 R_=(A)=\sum_{|U|=r}\mu_A(U).                          \tag{2.5}
\]

Here `C_<` is the lower duplicate excess and `R_=` counts every short
interval whose union already has middle rank.

### Theorem 2.1 (exact deadline/collision identity)

For every such `A`,

\[
 \boxed{\quad h(A)=C_<(A)+R_=(A)-\sigma.\quad}          \tag{2.6}
\]

Consequently `C_<(A)+R_=(A)>=sigma`, with equality if and only if `A`
covers every lower target.

#### Proof

Every interval in `I_d` is contained in at least one source window of
length `d+1`.  Its union is therefore contained in the corresponding
rank-`r` set `T_i`, and so has rank at most `r`.  Among the `Lambda` lower
targets, exactly `Lambda-h(A)` occur.  Hence

\[
 \sum_{1\le|S|<r}\mu_A(S)=\Lambda-h(A)+C_<(A).
\]

Adding the rank-`r` occurrence mass (2.5) counts every one of the
`M_d(n)` short intervals exactly once.  Using (2.2) and rearranging gives
(2.6).  QED.

### Corollary 2.2 (collision-excess upper bound)

Assume in addition that every target of rank greater than `r` is the union
of a consecutive interval of `T`.  Then

\[
 \nu(k)\le B(k)+C_<(A)+R_=(A)-\sigma.                  \tag{2.7}
\]

In particular, a family with

\[
 C_<(A)+R_=(A)\le\sigma+C                              \tag{2.8}
\]

proves `nu(k)<=B(k)+C`.

#### Proof

The equation `D^dA=T` supplies the middle layer.  Upper completeness of
`T` supplies every upper target, since

\[
 \bigcup_{i=a}^bT_i=\bigcup_{p=a}^{b+d}A_p.
\]

An interval of at least `d+1` source letters contains a full middle window,
so no lower target has a witness longer than `d`; therefore precisely
`h(A)` lower masks are missing.  Append those distinct masks as literal
nonzero letters.  All old witnesses remain contiguous and the appended
letters supply all holes.  The resulting universal word has length
`B(k)+h(A)`.  Apply Theorem 2.1.  QED.

This corollary is the exact carrier/compiler factorization: the carrier
proves middle and upper coverage, and one scalar short-window excess gives
the number of literal augmentation cells needed for the lower compiler.

## 3. The partial negative-window atlas

Let

\[
 \mathcal L=\{S\subseteq[k]:1\le|S|<r\}               \tag{3.1}
\]

be the lower target family.  For `x in [k]`, put

\[
 E_x=\{p\in J:x\in P_p\}.                              \tag{3.2}
\]

Let `U\subseteq\mathcal L`.  An interval selector on `U` is a map

\[
 \theta:U\longrightarrow\mathcal I_d.                  \tag{3.3}
\]

Candidates violating the necessary sandwich (1.7) may be deleted in
advance.  Define the negative set and surviving support of coordinate `x`
by

\[
 N_x(\theta)=\bigcup_{\substack{S\in U\\x\notin S}}\theta(S),
 \qquad Q_x(\theta)=E_x\setminus N_x(\theta).           \tag{3.4}
\]

Consider the three conditions

\[
 Q_x(\theta)\cap[i,i+d]\ne\varnothing
 \quad(0\le i<W,\ x\in T_i),                           \tag{3.5}
\]

\[
 Q_x(\theta)\cap\theta(S)\ne\varnothing
 \quad(S\in U,\ x\in S),                              \tag{3.6}
\]

and

\[
 \{x\in P_p:p\in Q_x(\theta)\}\ne\varnothing
 \quad(p\in J).                                        \tag{3.7}
\]

Call `theta` compatible when (3.5)--(3.7) hold.

### Theorem 3.1 (exact partial-atlas criterion)

There is a nonzero antecedent `A` with `D^dA=T` covering every target in
`U` if and only if a compatible selector on `U` exists.  Given a compatible
selector, the coordinatewise maximal word

\[
 A_p(\theta)=\{x\in P_p:p\in Q_x(\theta)\}             \tag{3.8}
\]

works.

#### Proof

Suppose first that `A` exists.  Choose one actual short witness
`theta(S)` for each `S in U`.  If `x notin S`, no source letter on
`theta(S)` contains `x`; hence `A` is coordinatewise contained in (3.8).
The positive parts of the middle equalities, selected target equalities,
and source nonemptiness give (3.5), (3.6), and (3.7), respectively.

Conversely, (3.8) is contained in `P`.  Thus no middle window contains a
coordinate outside its prescribed `T_i`, while (3.5) supplies every
coordinate of `T_i`; hence `D^dA=T`.  On `theta(S)`, definition (3.4)
deletes every coordinate outside `S`, and (3.6) supplies every coordinate
inside `S`, so its union is exactly `S`.  Condition (3.7) makes every
source letter nonempty.  QED.

This is the negative-window closure theorem with an arbitrary retained
subfamily of targets.  Downward closure is important: deleting selected
targets only enlarges every `Q_x`, and therefore cannot destroy
compatibility of the targets that remain.

## 4. The exact conflict hypergraph and its rank

For each `S\in\mathcal L`, let

\[
 V_S=\{(S,I): I\in\mathcal I_d,\ F(I)\subseteq S\subseteq P(I)\}.\tag{4.1}
\]

The sets `V_S` are the target parts.  A vertex family is **transversal** if
it contains at most one vertex from every part.  Interpret a transversal
family as a partial interval selector.

Define `H(T)` to be the hypergraph whose edges are the inclusion-minimal
transversal families which are not compatible in the sense of Theorem 3.1.
Singleton edges are allowed.  Because compatibility is downward closed, a
transversal selector is compatible exactly when it is independent in
`H(T)`.

### Theorem 4.1 (bounded-rank obstruction theorem)

Every edge of `H(T)` has size at most

\[
 \rho(T)=\max\{d+1,\max_{p\in J}|P_p|\}.                \tag{4.2}
\]

In particular, under (1.1), `rank(H(T))<=r`.

#### Proof

Let `X` be a minimal incompatible selector.  It fails at least one of
(3.5)--(3.7).

If (3.5) fails for `(i,x)`, the allowed set

\[
 R=E_x\cap[i,i+d]
\]

is covered by negative intervals selected in `X`.  For every `p in R`,
choose one selected candidate whose label omits `x` and whose interval
contains `p`.  At most `|R|<=d+1` candidates still kill the whole middle
requirement.  Minimality forces this subfamily to be `X`.

If (3.6) fails for the selected vertex `(S,I)` and `x in S`, choose, for
each position in `E_x cap I`, one selected negative interval which covers
it, and retain `(S,I)` itself.  This is an incompatible subfamily of size at
most `|I|+1<=d+1`; again minimality makes it all of `X`.  The case
`E_x cap I=emptyset` gives a singleton edge.

Finally, if (3.7) fails at `p`, then for each `x in P_p` choose one selected
interval containing `p` whose label omits `x`.  These at most `|P_p|`
candidates already empty source position `p`; minimality again gives `X`.

These three cases prove (4.2).  Since `|P_p|<=r` and `d+1<=r` under (1.1),
the final assertion follows.  QED.

The rank bound is genuinely about the decisive common-word interaction.
It does not say that all obstructions are pairwise.  The smallest omitted
case from ordinary Hall is already a two-edge coordinate cover: one pin
deletes the penultimate occurrence of `x` in a middle window and another
pin deletes the last occurrence.  Each is individually admissible and may
use a different physical address; together they form a conflict edge.

## 5. Independent-transversal deficiency is the exact compiler defect

Define

\[
 \tau(T)=\min\left\{|\mathcal L\setminus U|:
 \begin{array}{l}
 \text{there is an independent transversal of `H(T)`}\\
 \text{containing one vertex from `V_S` for every `S in U`}
 \end{array}\right\}.                                  \tag{5.1}
\]

### Theorem 5.1 (exact fixed-chronology defect theorem)

\[
 \boxed{\quad
 \tau(T)=\min\{h(A): A\ne\varnothing,\ D^dA=T\}.
 \quad}                                                  \tag{5.2}
\]

Consequently:

1. unrestricted `COMP_d(T)` is feasible if and only if `tau(T)=0`;
2. if `T` is upper-complete, then `nu(k)<=B(k)+tau(T)`;
3. a failure of ordinary target-to-cell Hall is only one possible witness
   for `tau(T)>0`; the exact countercondition is that every full transversal
   contains a conflict hyperedge.

#### Proof

Let `A` be any antecedent and let `U` be its distinct covered lower targets.
Choose one actual short witness for each member of `U`.  Theorem 3.1 makes
this an independent transversal, so

\[
                         \tau(T)\le h(A).               \tag{5.3}
\]

Conversely, let an independent transversal attain (5.1).  Theorem 3.1
constructs an antecedent covering every target in `U`, and hence missing at
most `|\mathcal L\setminus U|=\tau(T)` targets.  Taking the two minima
proves (5.2).
Item 1 is the full-atlas case, and item 2 follows either by appending the
missing targets or from Corollary 2.2.  Item 3 is merely (5.1) written as a
necessary-and-sufficient obstruction.  QED.

The scope of item 2 is constructive and one-sided.  It does not assert that
every universal word of length `B(k)+c` contains a length-`B(k)` prefix with
the prescribed derivative `T`; positive deadline slack permits other
architectures.

## 6. Conflict mass and a `B(k)+O(1)` theorem

Let `O\subseteq\mathcal L` be an exceptional family to be appended
literally.  For every `S\in\mathcal L\setminus O`, choose a probability
distribution `pi_S` on `V_S`.  Empty parts must be included in `O`.  Write
`E_O` for the
conflict edges of `H(T)` all of whose target parts lie outside `O`, and put

\[
 \Psi(T;O,\pi)
   =\sum_{E\in\mathcal E_O}
      \prod_{(S,I)\in E}\pi_S(I).                      \tag{6.1}
\]

### Theorem 6.1 (product conflict-mass alteration)

If `T` is upper-complete, then

\[
 \boxed{\quad
 \nu(k)\le B(k)+|O|+\lfloor\Psi(T;O,\pi)\rfloor.
 \quad}                                                  \tag{6.2}
\]

In particular:

\[
 O=\varnothing,\quad \Psi<1
 \quad\Longrightarrow\quad \nu(k)=B(k),               \tag{6.3}
\]

and any all-dimensional family satisfying

\[
 |O_k|+\Psi(T_k;O_k,\pi_k)\le C                         \tag{6.4}
\]

for one absolute constant `C` proves

\[
                         \nu(k)\le B(k)+C.              \tag{6.5}
\]

#### Proof

Independently sample one candidate from every nonexceptional target part.
Let `Z` count conflict edges wholly contained in the sampled transversal.
Every edge is transversal, so independence across its distinct target parts
gives

\[
                         \mathbb E Z=\Psi.              \tag{6.6}
\]

Because `Z` is integer-valued, some outcome has `Z<=floor(Psi)`.  For each
conflict edge present in that outcome, delete one of its target parts.  The
union `R` of deleted target parts has size at most `Z` and hits every
conflict edge that was present.  The remaining selector contains no
conflict edge: any incompatible remainder would contain an inclusion-minimal
incompatible family, which was already a present edge before deletion and
therefore was hit.  Theorem 3.1 now gives one nonzero antecedent covering
every target outside `O union R`.

Append the distinct masks in `O union R` as literal letters.  Carrier,
middle, upper, and retained lower witnesses all remain contiguous in the
old prefix.  The final length is at most

\[
 B(k)+|O|+|R|\le B(k)+|O|+\lfloor\Psi\rfloor.
\]

The deadline lower bound supplies equality in (6.3).  QED.

This is an alteration theorem, not an independence heuristic.  It remains
valid with singleton, pair, and higher conflict edges simultaneously, and
all rounding is integral.  Dirac distributions recover deterministic
selectors.  Thus the theorem loses no logical route; its value is that a
global `B(k)+O(1)` construction may now be proved by one summable bad-event
estimate instead of explicit avoidance of every conflict.

### Corollary 6.2 (zero-mass representation of the exact deficiency)

\[
 \boxed{
 \tau(T)=\min\{|O|:\text{there are distributions on the other parts with }
                         \Psi(T;O,\pi)=0\}.}            \tag{6.7}
\]

#### Proof

If the conflict mass is zero, the sampling/alteration argument in Theorem
6.1 has `Z=0`, independently of upper completeness.  Thus the
nonexceptional parts have an independent transversal and
`tau(T)<=|O|`.  Conversely, take an independent partial transversal
attaining `tau(T)`, put the omitted target parts in `O`, and use the Dirac
distribution on every chosen vertex.  No conflict edge is contained in its
support, so `Psi=0`.  QED.

### Theorem 6.3 (local conflict criterion for an exact compiler)

For every conflict edge `E`, let

\[
 p_E=\prod_{(S,I)\in E}\pi_S(I),                       \tag{6.8}
\]

and let `Gamma(E)` be the other conflict edges sharing at least one target
part with `E`.  Suppose `O=\varnothing` and there are real numbers
`0<=y_E<1` such that

\[
 p_E\le y_E\prod_{F\in\Gamma(E)}(1-y_F)
 \qquad(E\in\mathcal E).                               \tag{6.9}
\]

Then a full compatible interval selector exists.  If `T` is
upper-complete, then

\[
                         \nu(k)=B(k).                  \tag{6.10}
\]

In particular, if every conflict event has probability at most `p`, every
edge has at most `Delta` neighbors in this dependency graph, and

\[
 p\le {\Delta^\Delta\over(\Delta+1)^{\Delta+1}}        \tag{6.11}
\]

for `Delta>=1`, then (6.10) holds.  For `Delta=0`, the sufficient condition
is simply `p<1`.

#### Proof

Let `B_E` be the event that all vertices of `E` are selected.  Events whose
edges share no target part depend on disjoint random variables.  We prove by
induction on `|\mathcal S|` that, for every edge `E` and every family
`\mathcal S\subseteq\mathcal E\setminus\{E\}`,

\[
 \Pr\left(B_E\mid\bigcap_{F\in\mathcal S}\overline{B_F}\right)
 \le y_E.                                               \tag{6.12}
\]

Split `\mathcal S=\mathcal S_1\mathbin{\dot\cup}\mathcal S_2`, where
`\mathcal S_1\subseteq\Gamma(E)` and `\mathcal S_2` contains the
nonneighbors.  The event `B_E` is independent of the joint sigma-field
generated by the events in `\mathcal S_2`.  By the chain rule and the
induction hypothesis, conditioned on avoiding `\mathcal S_2`, the
probability of avoiding all events in `\mathcal S_1` is at least

\[
                         \prod_{F\in\mathcal S_1}(1-y_F).
\]

Consequently

\[
 \Pr\left(B_E\mid\bigcap_{F\in\mathcal S}\overline{B_F}\right)
 \le {p_E\over\prod_{F\in\mathcal S_1}(1-y_F)}
 \le y_E\prod_{F\in\Gamma(E)\setminus\mathcal S_1}(1-y_F)
 \le y_E.
\]

This proves (6.12).  Ordering all conflict events and applying (6.12) once
more gives

\[
 \Pr\left(\bigcap_E\overline{B_E}\right)
 \ge\prod_E(1-y_E)>0.
\]

Thus some full selector contains no conflict edge.  Theorems 3.1 and 5.1
give the exact compiler, and upper completeness plus the deadline lower
bound gives (6.10).

For the symmetric consequence take `y_E=1/(Delta+1)`.  The right side of
(6.9) is at least

\[
 {1\over\Delta+1}\left({\Delta\over\Delta+1}\right)^\Delta
 ={\Delta^\Delta\over(\Delta+1)^{\Delta+1}},
\]

which proves (6.11).  QED.

## 7. Where ordinary Hall is exact, and where it is not

Fix a robust core `C<=P` with `D^dC=T`.  For every protected fixed frame
`(I,R)`, require the full sandwich

\[
             \bigcup_{p\in I}C_p=R=\bigcup_{p\in I}P_p. \tag{7.0}
\]

(Alternatively, intersect the original erosion envelope at each position
with every fixed-pin label whose interval contains that position, call the
result `\widehat P`, and separately verify
`D^d\widehat P=T` and the upper equalities in (7.0); then use
`\widehat P` in place of `P` below.)  Restrict every residual target to a
literal candidate position

\[
 N_C(S)=\{p:C_p\subseteq S\subseteq P_p\}.              \tag{7.1}
\]

If distinct targets use distinct positions, set the matched letter equal to
its target and every unmatched letter equal to `P_p`.  Sandwiching between
`C` and `P` preserves every central equality and, by (7.0), every protected
equality.  Conversely,
distinct literal target values cannot occupy the same position.  Therefore
the robust-core literal subclass has a completion exactly when

\[
 \left|\bigcup_{S\in X}N_C(S)\right|\ge|X|
 \qquad(X\subseteq\mathcal R),                          \tag{7.2}
\]

which is ordinary Hall.  Laminar actual neighborhoods reduce (7.2) to one
cut per laminar node, and the two-prefix boundary graph reduces it to the
known `(d+1)^2` inequalities.

The conflict hypergraph is the exact unrestricted extension of this
picture.  Multi-letter intervals do not consume one literal address; their
negative windows consume coordinate occurrences in several overlapping
requirements.  The common-coordinate cover edges of Theorem 4.1 are the
minimal countercondition which ordinary Hall omits.  The `k=9` optimal word,
whose target `416` is a genuine length-two lower witness, confirms that this
extension is necessary and that one-core Hall is not a normal form for
unrestricted `COMP_d(T)`.

## 8. Exact seam ledger and the shadow-braid gate

Suppose a source word is partitioned into pieces, every piece has at least
`d-1` letters on each side of every relevant join, and distinct joins are
separated by at least `d` letters.  Then every interval of length at most
`d` is either internal to one piece or crosses exactly one seam.  A seam has
exactly

\[
 \sum_{j=2}^d(j-1)={d\choose2}                          \tag{8.1}
\]

crossing short intervals.

For a fixed rethreading `pi`, let `mu_int(S)` count internal short intervals
with union `S`, and let `mu_seam,pi(S)` count the new crossing intervals.
The lower hole family is exactly

\[
 \boxed{\quad
 H(\pi)=\{S\in\mathcal L:
          \mu_{\rm int}(S)=0=\mu_{{\rm seam},\pi}(S)\}.
 \quad}                                                  \tag{8.2}
\]

### Theorem 8.1 (conditional separated shadow-braid compiler bound)

Assume the rethreaded middle chronology is a `d`-resident permutation of
the middle layer and is upper-complete, and assume its physical prefix `A`
satisfies `D^dA=T`.  Then

\[
                         \nu(k)\le B(k)+|H(\pi)|.       \tag{8.3}
\]

If the old piece assembly covered every lower target, and had `s` separated
seams, then every target absent internally had an old seam provider, so

\[
 |\{S:\mu_{\rm int}(S)=0\}|\le s{d\choose2}.            \tag{8.4}
\]

Thus the unconditional seam-count estimate gives only

\[
                         \nu(k)\le B(k)+s{d\choose2},   \tag{8.5}
\]

whereas `B(k)+O(1)` requires the exact signed condition

\[
 \#\{S:\mu_{\rm int}(S)=0=\mu_{{\rm seam},\pi}(S)\}=O(1).\tag{8.6}
\]

#### Proof

The separation hypotheses give the internal/crossing dichotomy and the
count (8.1).  Therefore a lower target occurs if and only if one of the two
multiplicities in (8.2) is positive.  Theorem 8.1 is Corollary 2.2 with the
holes appended.  If the old assembly was lower-complete, every target with
zero internal multiplicity occurred on an old crossing interval; there are
`s binom(d,2)` such interval occurrences, proving (8.4).  Equations
(8.5)--(8.6) follow.  QED.

Equation (8.6), not component count or residence by itself, is the exact
compiler part of a reusable shadow-braid theorem.  Since
`d(k)=Theta(sqrt(k))`, even one unbalanced seam has a raw
`Theta(k)` short-window ledger.  A constant-seam Pascal braid reaches
`B(k)+O(1)` only by transporting or recreating all but constantly many of
those exposed target values.

The seam ledger does not construct `A`.  A purely combinatorial reordering
of middle-owner pieces proves (8.3) only after one common physical prefix
with `D^dA=T` has been supplied.  This is precisely where the unrestricted
negative-window selector or the stronger robust-core Hall interface enters.

If a piece is shorter than `d-1` or seams are closer than `d`, (8.2) remains
true after replacing the one-seam ledger by the literal list of all
multi-seam short intervals; only the closed form (8.1) and bound (8.4) must
be replaced.  No independence across interacting seams is asserted.

## 9. Pascal odd/even interface

The proved facet/union Pascal transducers transport complete lower and upper
flag towers occurrence by occurrence.  In the odd-to-even chart with copied
shore `A_i=T_i` and facet shore
`B_i=\{z\}\cup(T_i\cap T_{i+1})`, and in the reversed-union arm of the
even-to-odd chart, the exact erosion shifts are

\[
 P_d(A)_i=P_d(T)_i,\qquad
 P_d(B)_i=\{z\}\cup P_{d+1}(T)_{i+1},
 \qquad
 P_d^{\rm rev\,U}(U_i)=P_{d-1}(T)_{i+d}                \tag{9.1}
\]

on their stated shores.  Thus they transport the envelope half of (1.7)
exactly.  The event identities likewise determine the mandatory run ports
on each unbraided interior; the complete candidate sandwich must still be
recomputed at the turns and promoted collars.  For `s` braid seams, the
audited protected-core theorem localizes the promoted columns and incident
core equations to at most

\[
                         s(d+2),\qquad s(d+3),          \tag{9.2}
\]

respectively.

Those statements do not bound the unrestricted conflict mass.  A negative
interval meeting a promoted collar can participate in a conflict edge with
other intervals far away along the same coordinate support, and the exact
seam ledger has `binom(d,2)` rather than `O(1)` entries per separated seam.
Thus the minimal additional Pascal theorem is now precise:

> **Pascal conflict-mass gate.**  Construct, in every dimension, one safe
> linear opening of the transported chronology and one set of candidate
> distributions for which the final chronology is resident and
> upper-complete and `|O|+Psi=O(1)` (or, equivalently at the existential
> level, `tau(T)=O(1)`).

The stronger target `Psi<1`, or `tau(T)=0`, proves the exact formula.  This
gate includes the common-core promoted Hall theorem as the literal/singleton
special case but permits the genuinely multi-letter witnesses that are
forced by the `k=9` audit and by the all-odd one-core capacity obstruction.

## 10. Certificate checks and decisive-step audit

1. **Known optimal flat words.**  In each retained exact certificate whose
   `d`th derivative is the complete middle deck (in particular the audited
   `k=11`, `k=13`, and `k=15` words), choose the first actual short witness
   for every lower target.  The resulting full selector satisfies
   (3.5)--(3.7), so it is independent, `tau(T)=0`, and its Dirac product
   distribution has `Psi=0`.  The theorem therefore reproduces the exact
   compiler conclusion without imposing `DA=DP`.

2. **The `k=9` normalization counterexample.**  Its nonliteral target `416`
   gives a length-two vertex in the conflict hypergraph.  The full actual
   selector is nevertheless independent.  Hence Theorem 5.1 correctly says
   `tau(T)=0` while the one-core literal Hall subclass is impossible.

3. **No inference from the `k=16` upper word.**  The authenticated
   length-`12874` word proves `nu(16)<=B(16)+1`, but it does not by itself
   identify a length-`B(16)` prefix with a prescribed flat derivative.
   It is therefore not evidence that `tau(T)=1` for any named chronology.

4. **Audit of Theorem 4.1.**  The only possible failures of a maximal
   negative-window word are exactly (3.5), (3.6), and (3.7).  A minimal
   interval cover of a finite set of source positions uses no more members
   than the number of positions: choose one covering interval per position
   and discard duplicates.  This gives `d+1`, `d+1`, and `|P_p|` in the
   three cases.  No Helly, total-unimodularity, or fractional-rounding claim
   is being smuggled into the rank bound.

5. **Audit of alteration.**  Conflict edges are required to be transversal,
   so the probability of an edge is the product in (6.1).  Removing target
   parts is monotone because it removes negative windows and positive
   obligations simultaneously.  Hitting every conflict edge present before
   deletion therefore leaves an independent selector.  Appended literal
   masks cannot destroy any old contiguous witness.  These facts justify
   every integrality and rounding step in Theorem 6.1.

## 11. Proved boundary

The following statements are proved here.

* The deadline slack/collision identity (2.6) is exact.
* `COMP_d(T)` is exactly a full independent transversal of the bounded-rank
  negative-window conflict hypergraph.
* `tau(T)` is exactly the minimum lower-hole count in one fixed flat
  chronology.
* Conflict mass `Psi` gives the integral upper bound (6.2), including the
  sharp implication `Psi<1 => nu(k)=B(k)`.
* The separated seam ledger is exactly (8.2), with `binom(d,2)` short
  intervals per seam.

The following statements remain unproved.

* There is no proof that `tau(T)=O(1)` for any known all-dimensional PBBS,
  MMM, GMM, or Pascal-recursive carrier family.
* PBBS all-depth occurrence support does not give a conflict-mass bound;
  it may supply only one candidate for a target.
* Constant component or seam count does not imply (8.6).
* The product-distribution theorem does not assert independence of physical
  seam choices; candidate probabilities are used only to select witness
  intervals after one physical chronology has been fixed.
* No claim is made that every length-`B(k)+C` word arises from this flat
  chronology plus `C` appended literals.

Thus the exact all-`k` frontier is narrowed to a concrete, bounded-rank
independent-transversal/alteration problem.  Proving (0.6) for a Pascal or
PBBS chronology gives the requested `B(k)+O(1)` upper bound; a family with
`tau(T_k)->infinity` for every chronology in a declared braid class is the
sharp scoped obstruction to that class.

## 12. Input theorems used

The proof imports only the already established statements recorded in:

* `MATH_AUDIT_AD_ALL_ODD_COMPILER_ONECORE_NORMALIZATION_20260729.md`
  (unrestricted `COMP_d(T)` and negative-window closure);
* `THREAD_A_UNRESTRICTED_COMP_TWO_BOUNDARY_LAMINAR_HALL_THEOREM_20260729.md`
  (exact atlas criterion and robust-core Hall scope);
* `MATH_EROSION_JOHNSON_CONTROLLER_DUALITY_20260728.md`
  (residence, maximal erosion, and mandatory run-boundary ports);
* `MATH_THEOREM_AD_PASCAL_EVENT_STREAM_BRAID_AND_DUAL_GAP_20260729.md`
  (Pascal shadow/envelope transport and promoted-collar bounds); and
* the monotone-deadline lower bound summarized in `MATHEMATICAL_HANDOFF.md`.

No finite certificate, probabilistic independence assumption beyond the
explicit product measure, or computational search is used in the proofs.
