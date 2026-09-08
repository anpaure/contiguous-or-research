# Rotation-equivariant status-necklace packets: exact partition and two linear Hall obstructions

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Verdict

Fix a cyclically ordered perfect matching of the \(2m\) physical coordinates,

\[
 P_i=\{u_i,v_i\},\qquad i\in\mathbb Z_m.
\tag{0.1}
\]

For a middle owner \(X\in\binom{[2m]}m\), record the pair-status word

\[
 w(X)\in\{\mathsf E,\mathsf S,\mathsf F\}^{\mathbb Z_m},
\tag{0.2}
\]

where a pair is empty, split, or full. Fix any total order on this
three-letter alphabet. If \(w(X)\) is aperiodic, it has a unique
lexicographically minimal cyclic rotation. Starting there, select the first
\(r\) split positions.

Here \(r\) denotes the number of active ambient pair-orientation
directions. If the inner parity-complete paired-order lift writes its active
dimension as \(2s\), substitute \(r=2s\) throughout; the argument does not
depend on how those \(r\) directions are paired internally.

For

\[
                         r\le m/4,
\tag{0.3}
\]

this gives an exact owner-disjoint packet partition of all but
\(e^{-\Omega(m)}W\) middle owners into physical orientation cubes \(Q_r\),
where

\[
                         W=\binom{2m}{m}.
\tag{0.4}
\]

The selector is exactly rotation-equivariant. If \({\cal G}_r\) is the
retained owner set, \(G=|{\cal G}_r|\), and
\(I(X)\subseteq\mathbb Z_m\) is the selected pair set, then every pair
coordinate has the exact marginal

\[
 \boxed{
 \#\{X\in{\cal G}_r:i\in I(X)\}={rG\over m}.}
\tag{0.5}
\]

Moreover each endpoint of \(P_i\) is contained in exactly half of the
owners counted in (0.5).

These statements prove the proposed partition and its one-coordinate
balance. They do **not** prove the desired outer target-Hall theorem. In
fact, the construction has two rigorous Gaussian-scale Hall obstructions.

The first obstruction does not use localization. For a set \(S\), let

\[
 h_P(S)=\#\{i:P_i\subseteq S\}
\tag{0.6}
\]

be its number of full ambient pairs. Every cell fixes the complete
empty/split/full word. A rank-\(m-q\) trace made inside the cell has the
same \(h_P\) as its owner; dually, a rank-\(m+q\) trace has the same number
of empty pairs as its owner. At

\[
 q=\lfloor A\sqrt m\rfloor\le r,
\tag{0.7}
\]

the resulting exact type cut gives, separately for both signs,

\[
 \boxed{
 M_q^\pm\ge(\delta_A-o(1))W,
 \qquad
 \delta_A=e^{-A^2}\Phi(A/2)-\Phi(-3A/2)>0.}
\tag{0.8}
\]

Here \(\Phi\) and \(\phi\) denote the standard normal distribution
function and density.

Thus rotation, reordering, correlated choices, and perfect trace
injectivity inside these cells cannot repair the fixed-pair supply
imbalance.

The selector removes the frozen *terminal* suffix of the linear
first-eligible rule, but it replaces it by a uniformly rotating short active
arc. If

\[
                         \log m\ll r=o(m),
\tag{0.9}
\]

then, outside \(o(W)\) owners, the selected set \(I(X)\) lies in a cyclic
arc of at most \(4r\) pair positions. Consequently, for every fixed cyclic
interval \(R\) of \(\alpha m\) pair positions,

\[
 \boxed{
 {1\over G}\#\{X\in{\cal G}_r:I(X)\cap R\ne\varnothing\}
 =\alpha+o(1).}
\tag{0.10}
\]

Thus \(R\) is still frozen on a \(1-\alpha-o(1)\) fraction of the owner
mass. The published terminal-quarter dual no longer proves a positive
deficit after the \((1/4+o(1))W\) mobile mass is charged. However, a finite
multi-core dual survives. For every fixed \(A>0\), one may take

\[
 K_A=\left\lceil e^{4/A^2}+2\right\rceil
\tag{0.11}
\]

consecutive pair blocks. A centered \(K_A\)-block occupancy ball gives

\[
 \boxed{
 M_q^\pm\ge(c_A-o(1))W,
 \qquad
 c_A={1\over4}e^{-A^2}\mu_{K_A}
 \left(B_{V_{K_A}}(0,\eta_A)\right)>0,}
\tag{0.12}
\]

where

\[
 \eta_A={\log(3/2)\over2K_AA},\qquad
 d\mu_K(z)=\left({K\over\pi}\right)^{(K-1)/2}
 e^{-K\|z\|^2}\,d\lambda_{V_K}(z),
 \quad V_K=\{z:\textstyle\sum_jz_j=0\}.
\tag{0.13}
\]

This proves that the rotating active arc does not defeat all fixed-core
cuts.

The candidate-face first moment is unchanged by the new partition. At depth
\(q\le r\), the total number of cell--target face incidences of either sign
is

\[
 \boxed{
                         G{\binom rq\over2^q}.}
\tag{0.14}
\]

Rotation equivariance makes target degrees constant only on cyclic target
orbits. It does not control their lower tail. At the selector level, if

\[
 N_q(D)=\#\{X\in{\cal G}_r:D\subseteq I(X)\},
\tag{0.15}
\]

then

\[
 N_q(D+i)=N_q(D),\qquad
 \sum_{D\in\binom{\mathbb Z_m}q}N_q(D)=G\binom rq,
\tag{0.16}
\]

but different cyclic gap shapes can have completely different degrees.
Indeed, unless \(D\) is contained in a \(4r\)-arc, only the \(o(W)\)
short-arc-exceptional owners can contribute to \(N_q(D)\). For
\(q=\Theta(\sqrt m)\) and \(r=o(m)\), such direction sets form a vanishing
fraction whenever

\[
 q\log\!\left({m-q+1\over4r}\right)-\log m
 \longrightarrow\infty.
\tag{0.17}
\]

This direction-set statement alone would not give a physical target cut,
because one target may admit several touched direction sets. The exact type
cut (0.8) and multi-core cut (0.12) do give literal physical target cuts.

The new construction therefore supplies a sound rotation-equivariant outer
packetization, but it is closed as a cellwise coefficient-one route. An
escape must use a positive-density family of windows which changes the
ambient pair frame or crosses status cells and, for the multi-core cut,
fails one-block localization by meeting at least two of the fixed pair
blocks. Constant one is not proved.

## 1. Status words and the canonical rotation

Let

\[
\begin{aligned}
 \mathsf E&:\quad X\cap P_i=\varnothing,\\
 \mathsf S&:\quad |X\cap P_i|=1,\\
 \mathsf F&:\quad X\cap P_i=P_i.
\end{aligned}
\tag{1.1}
\]

Write \(e(X),s(X),f(X)\) for the three letter counts. Since \(X\) has
size \(m\),

\[
 e+s+f=m,\qquad s+2f=m,
\tag{1.2}
\]

and hence

\[
                         e(X)=f(X).
\tag{1.3}
\]

Let \(\tau\) be the physical coordinate permutation

\[
 \tau(u_i)=u_{i-1},\qquad \tau(v_i)=v_{i-1}
 \quad(i\in\mathbb Z_m).
\tag{1.4a}
\]

It induces cyclic left rotation of the pair-status word. A word \(w\) is
aperiodic if

\[
                         \tau^jw\ne w
\quad(1\le j<m).
\tag{1.4}
\]

### Lemma 1.1 (unique root)

An aperiodic word has a unique rotation index \(\rho(w)\in\mathbb Z_m\)
at which its lexicographically least rotation starts.

Moreover,

\[
                         \rho(\tau^kw)=\rho(w)-k
                         \pmod m.
\tag{1.5}
\]

#### Proof

A finite set of rotations has a lexicographically least member. If two
indices produced that same least word, their difference would be a
nonzero cyclic period, contrary to (1.4). This proves uniqueness.
Rotating the input only shifts the index at which each cyclic word is read,
which gives (1.5). \(\square\)

For an aperiodic word with at least \(r\) split letters, read positions in
the cyclic order

\[
 \rho(w),\rho(w)+1,\ldots,\rho(w)+m-1
\tag{1.6}
\]

and let

\[
                         I(w)
\tag{1.7}
\]

be the positions of the first \(r\) letters \(\mathsf S\).
Equation (1.5) gives the exact selector equivariance

\[
                         I(\tau^kw)=I(w)-k.
\tag{1.8}
\]

## 2. The exact packet partition

For every split pair \(P_i\), write

\[
 \varepsilon_i(X)=
 \begin{cases}
 0,&u_i\in X,\\
 1,&v_i\in X.
 \end{cases}
\tag{2.1}
\]

Define the retained set

\[
 {\cal G}_r=
 \{X\in\binom{[2m]}m:
   w(X)\text{ is aperiodic and }s(X)\ge r\}.
\tag{2.2}
\]

For \(X\in{\cal G}_r\), put \(I(X)=I(w(X))\). Define

\[
 {\cal C}(X)=
 \left\{Y:
 \begin{array}{l}
 w(Y)=w(X),\\
 \varepsilon_i(Y)=\varepsilon_i(X)
       \quad\text{for every split }i\notin I(X)
 \end{array}\right\}.
\tag{2.3}
\]

### Theorem 2.1 (exact rotation-equivariant packetization)

The sets \({\cal C}(X)\), after duplicate names are identified, partition
\({\cal G}_r\). Every cell has exactly

\[
                         |{\cal C}(X)|=2^r
\tag{2.4}
\]

owners and is a literal physical \(Q_r\) in the middle layer. Furthermore,

\[
                         \tau{\cal C}(X)={\cal C}(\tau X).
\tag{2.5}
\]

#### Proof

Changing the chosen endpoint in a selected split pair leaves its status
letter equal to \(\mathsf S\). Thus every \(Y\in{\cal C}(X)\) has the same
status word, the same canonical root, and the same selected set:

\[
                         I(Y)=I(X).
\tag{2.6}
\]

The orientations on the \(r\) selected pairs are free and independent, while
all remaining data are fixed. This proves (2.4).

If two cells meet, their common owner determines the common status word and
all unselected orientations, so the two cells are equal. Every retained
owner belongs to its own cell, proving the partition.

Flipping one selected orientation removes one endpoint of \(P_i\) and adds
the other. It is therefore one Johnson edge between middle owners (and is
implemented by the usual two-edge Boolean detour through their union). The
\(r\) independent exchanges give a literal physical orientation cube
\(Q_r\) on middle owners.

Finally, (1.8) and rotation of the exterior orientation data give (2.5).
\(\square\)

This theorem is only an outer cell theorem. An inner parity-complete factor
or trace-code construction must still be installed in every \(Q_r\)-cell.

## 3. Exponentially small leave

There are two bad families.

### Lemma 3.1 (periodic statuses are exponentially rare)

The number of middle owners whose status word is periodic is at most

\[
                         m\,3^{m/2}2^m.
\tag{3.1}
\]

Consequently their fraction of the middle layer is at most

\[
 m(2m+1)\left({\sqrt3\over2}\right)^m
 =e^{-\Omega(m)}.
\tag{3.2}
\]

#### Proof

A periodic word has a proper period of length at most \(m/2\). Overcounting
all possible period lengths and all base words gives at most
\(m3^{m/2}\) status words. Once a status word is fixed, every split position
has two orientations, so it represents at most \(2^m\) owners.

The central binomial coefficient is the largest coefficient of
\((1+x)^{2m}\), hence

\[
                         W\ge {4^m\over2m+1}.
\tag{3.3}
\]

Dividing (3.1) by (3.3) proves (3.2). \(\square\)

### Lemma 3.2 (few split pairs are exponentially rare)

If \(r\le m/4\), then

\[
 {1\over W}
 \#\{X\in\binom{[2m]}m:s(X)<r\}
 \le(2m+1)e^{-m/16}.
\tag{3.4}
\]

#### Proof

Before conditioning on total rank, choose every physical coordinate
independently with probability \(1/2\). The split indicators of the \(m\)
pairs are independent Bernoulli variables of mean \(1/2\). Hence

\[
                         s(X)\sim{\rm Bin}(m,1/2).
\tag{3.5}
\]

For \(r\le m/4\), the usual multiplicative Chernoff bound gives

\[
                         \Pr(s(X)<r)\le e^{-m/16}.
\tag{3.6}
\]

Conditioning on total size \(m\) costs at most the reciprocal of
\(4^{-m}W\), which is at most \(2m+1\) by (3.3). \(\square\)

### Corollary 3.3

For \(r\le m/4\),

\[
                         |{\cal G}_r|
                         =W-e^{-\Omega(m)}W.
\tag{3.7}
\]

The constants in the two exponential terms are absolute.

## 4. Exact uniform marginals

Put

\[
                         G=|{\cal G}_r|.
\tag{4.1}
\]

The set \({\cal G}_r\) is rotation-invariant. Since every retained status
is aperiodic, every owner orbit under pair rotation has exactly \(m\)
members.

### Theorem 4.1 (selected-pair marginals)

For every \(i\in\mathbb Z_m\),

\[
 \boxed{
 \#\{X\in{\cal G}_r:i\in I(X)\}={rG\over m}.}
\tag{4.2}
\]

For either endpoint \(z\in P_i\),

\[
 \boxed{
 \#\{X\in{\cal G}_r:i\in I(X),\ z\in X\}
 ={rG\over2m}.}
\tag{4.3}
\]

If “active physical coordinate” means that \(z\) belongs to a selected
exchange pair, its incidence is \(rG/m\), the same as (4.2). Equation
(4.3) is the finer selected-and-present incidence.

Equivalently, because every cell has \(2^r\) owners, exactly

\[
                         {r\over m}{G\over2^r}
\tag{4.3a}
\]

retained cells select the pair \(P_i\).

#### Proof

Fix one rotation orbit. By (1.8), its \(m\) selected sets are the \(m\)
rotates of one \(r\)-set. Hence every pair position belongs to exactly
\(r\) of those selected sets. Summing over the disjoint owner orbits gives
(4.2).

For a selected split pair \(P_i\), flipping its orientation is a fixed-point
free involution of the retained owner set which preserves the status word
and selected set. It exchanges the two endpoint events, proving (4.3).
\(\square\)

Thus \(m\mid rG\), as is also immediate orbit by orbit.

The same argument is exact inside every full-pair stratum. If

\[
 {\cal G}_{r,f}=\{X\in{\cal G}_r:f(X)=f\},\qquad G_f=|{\cal G}_{r,f}|,
\tag{4.4}
\]

then, for every pair \(i\),

\[
 \#\{X\in{\cal G}_{r,f}:i\in I(X)\}={rG_f\over m},
\tag{4.5}
\]

and either endpoint is selected and present on exactly \(rG_f/(2m)\)
owners. Moreover,

\[
 \#\{X\in{\cal G}_{r,f}:P_i\text{ is split}\}
 ={(m-2f)G_f\over m},
\tag{4.6}
\]

so conditional on \(P_i\) being split its exact selection frequency is
\(r/(m-2f)\). Notice that an active exchange uses both physical endpoints
of \(P_i\); equation (4.3) counts which one is present at the owner.

### Proposition 4.2 (what rotation symmetry does not imply)

For \(D\in\binom{\mathbb Z_m}q\), define

\[
                         N_q(D)=\#\{X\in{\cal G}_r:D\subseteq I(X)\}.
\tag{4.7}
\]

Then

\[
 N_q(D+k)=N_q(D)
\tag{4.8}
\]

and

\[
 \sum_{D\in\binom{\mathbb Z_m}q}N_q(D)=G\binom rq.
\tag{4.9}
\]

No equality between different cyclic gap shapes follows.

#### Proof

Equation (4.8) follows from the bijection \(X\mapsto\tau^kX\).
For (4.9), every owner contributes once for each of the
\(\binom rq\) subsets of its selected set. \(\square\)

This is the precise distinction between a rotation-balanced selector and a
\(q\)-design.

## 4A. Exact full/empty-pair Hall obstruction

This obstruction applies to every status-stable orientation-cube atlas, not
only to the lexicographic necklace selector.

For \(0\le f\le m/2\), let \({\cal M}_f\) be the middle owners having
exactly \(f\) full ambient pairs. Such an owner also has exactly \(f\)
empty pairs and \(m-2f\) split pairs, so

\[
 V_f:=|{\cal M}_f|
 ={m!\,2^{m-2f}\over f!^2(m-2f)!}.
\tag{4A.1}
\]

A rank-\(m-q\) target having \(f\) full pairs has \(f+q\) empty pairs and
\(m-2f-q\) split pairs. A rank-\(m+q\) target having \(f\) empty pairs has
\(f+q\) full pairs and the same number of split pairs. Thus both labelled
target families have the common cardinality

\[
 T_{f,q}
 ={m!\,2^{m-2f-q}\over
 f!(f+q)!(m-2f-q)!}.
\tag{4A.2}
\]

Here \(0\le f\le\lfloor(m-q)/2\rfloor\); set \(T_{f,q}=0\) outside this
range.

### Lemma 4A.1 (statewise pair-type invariance)

Let a locally geodesic \(q\)-window stay in one orientation cube obtained
by flipping endpoints of split pairs. Its rank-\(m-q\) intersection has
exactly the original owner's full pairs. Its rank-\(m+q\) union has exactly
the original owner's empty pairs.

#### Proof

The \(q\) window directions are distinct because the two traces have ranks
exactly \(m-q\) and \(m+q\). On every touched split pair both endpoint
orientations occur, so the intersection contains neither endpoint and the
union contains both. An untouched pair has one status and one orientation
throughout the window. Hence original full pairs, respectively original
empty pairs, are preserved exactly. \(\square\)

### Theorem 4A.2 (exact type Hall cut)

Fix the one ambient matching \(P\). Choose arbitrary integral or fractional
owner-simple exact factors inside arbitrary status-stable orientation
cells. At one fixed depth \(q\), let \(M_q^-\)
and \(M_q^+\) be their uncovered lower and upper target masses; explicitly,
if \(\ell_q^\pm(T)\) is the occurrence load, then
\(M_q^\pm=\sum_T(1-\ell_q^\pm(T))_+\). Then

\[
 \boxed{
 M_q^-\ge\sum_f(T_{f,q}-V_f)_+,
 \qquad
 M_q^+\ge\sum_f(T_{f,q}-V_f)_+.}
\tag{4A.3}
\]

The same inequalities hold for the fractional uncovered-mass LP.

#### Proof

Every middle owner supplies exactly one occurrence of each sign at the
fixed depth. By Lemma 4A.1, all lower occurrences covering the target class
with \(f\) full pairs must come from the \(V_f\) owners in \({\cal M}_f\).
Thus at most \(V_f\) of its \(T_{f,q}\) target demands can be met. Sum the
positive deficiencies over the disjoint classes. For the upper sign use
the disjoint classes indexed by the number \(f\) of empty pairs. Fractional
packet weights obey the same exact-owner capacity inequality. \(\square\)

The bound optimistically allows every discarded necklace owner to help, so
no leave term is needed.

### Theorem 4A.3 (Gaussian constant)

Fix \(A>0\) and put \(q=\lfloor A\sqrt m\rfloor\). Then

\[
 {1\over W}\sum_f(T_{f,q}-V_f)_+
 \longrightarrow
 \boxed{\delta_A=e^{-A^2}\Phi(A/2)-\Phi(-3A/2)>0.}
\tag{4A.4}
\]

#### Proof

The exact likelihood ratio is

\[
 \lambda_{f,q}:={V_f\over T_{f,q}}
 =2^q{(f+1)^{\overline q}\over(m-2f)_{\underline q}},
\tag{4A.5}
\]

and is strictly increasing in \(f\). Uniformly for fixed \(x\) and

\[
                         f={m\over4}+x\sqrt m+O(1),
\tag{4A.6}
\]

Taylor expansion of the logarithm of (4A.5) gives

\[
 \log\lambda_{f,q}=8Ax+3A^2+o(1).
\tag{4A.7}
\]

Indeed the linear displacement contributes \(8Ax\), while summing the
first-order numerator/denominator drift over \(q\) factors contributes
\(3q^2/m=3A^2+o(1)\); the sum of the Taylor remainders is \(o(1)\) on
compact \(x\)-sets. Monotonicity therefore places the last deficient type
at

\[
 a_m={m\over4}-{3A\over8}\sqrt m+o(\sqrt m).
\tag{4A.8}
\]

Stirling's formula, uniformly for
\(f=m/4+O(\sqrt m)\), gives

\[
 {V_f\over W}
 ={4\over\sqrt m}\left[
 \phi\left({4(f-m/4)\over\sqrt m}\right)+o(1)\right]
\tag{4A.9}
\]

and

\[
 {T_{f,q}\over W}
 ={4\over\sqrt m}\left[
 e^{-A^2}\phi\left({4(f-m/4)\over\sqrt m}+2A\right)
 +o(1)\right].
\tag{4A.10}
\]

The errors are uniform on compact standardized intervals. The two exact
mass sequences are log-concave, so the tails outside a growing compact
interval are
uniformly negligible; equivalently, (4A.9)--(4A.10) sum to the usual
conditional lattice central limit theorem. Since

\[
 {\binom{2m}{m-q}\over W}\longrightarrow e^{-A^2},
\tag{4A.11}
\]

summing through the monotone crossing (4A.8) yields

\[
 {1\over W}\sum_f(T_{f,q}-V_f)_+
 \longrightarrow
 e^{-A^2}\Phi(A/2)-\Phi(-3A/2).
\tag{4A.12}
\]

Finally, after substituting \(u=v-2A\),

\[
 \Phi(-3A/2)
 =\int_{-\infty}^{A/2}e^{\,2Av-2A^2}\phi(v)\,dv
 <e^{-A^2}\Phi(A/2),
\tag{4A.13}
\]

because \(v<A/2\) almost everywhere in the integral. This proves strict
positivity. \(\square\)

Combining Theorems 4A.2 and 4A.3 proves (0.8). It also identifies the exact
scope: pair rotations and inner order changes cannot help. Escaping this
cut requires a positive-density supply of windows which genuinely changes
the unordered ambient matching or splices across different status cubes.

## 5. The active set is typically a short rotating arc

For the positive integer \(r\) fixed above and \(X\in{\cal G}_r\), let
\(\ell(X)\) be the length of the cyclic interval beginning at
\(\rho(w(X))\) and ending at the \(r\)-th selected split position.

### Lemma 5.1 (short-arc estimate)

\[
 {1\over W}\#\{X\in{\cal G}_r:\ell(X)>4r\}
 \le m(2m+1)e^{-r/4}.
\tag{5.1}
\]

#### Proof

If every cyclic interval of \(4r\) pair positions contains at least \(r\)
split letters, then the first \(r\) splits after any starting point occur
within \(4r\) positions. Thus the event in (5.1) implies that some cyclic interval of
length \(4r\) contains fewer than \(r\) split pairs.

Before rank conditioning, the split count in one prescribed interval is
\({\rm Bin}(4r,1/2)\), of mean \(2r\). Chernoff gives probability at most
\(e^{-r/4}\) that it is below \(r\). A union bound over the \(m\) cyclic
intervals and the same conditioning cost \(2m+1\) prove (5.1). \(\square\)

In particular, under (0.9), the exceptional fraction in (5.1) is \(o(1)\).

### Theorem 5.2 (exact fixed-interval mobility)

Let \(R\subseteq\mathbb Z_m\) be a cyclic interval of \(L\) pair positions,
where

\[
                         L+4r\le m.
\tag{5.3}
\]

Put

\[
 M_R=\#\{X\in{\cal G}_r:I(X)\cap R\ne\varnothing\}.
\tag{5.4}
\]

Then, if \(\log m\ll r=o(m)\),

\[
 \boxed{
                         {M_R\over G}
                         ={L\over m}+O(r/m)+o(1).}
\tag{5.5}
\]

#### Proof

Fix one free rotation orbit and write \(I\) for one selected set. The number
of rotations in the orbit for which the rotated selected set meets \(R\)
is exactly the cyclic difference-set size

\[
                         |R-I|.
\tag{5.6}
\]

Since \(I\ne\varnothing\), one translate \(R-i\) lies in \(R-I\), so

\[
                         |R-I|\ge L.
\tag{5.7}
\]

If \(I\) lies in an arc of length at most \(4r\), then \(R-I\) lies in an
arc of length at most \(L+4r-1\), by (5.3). Hence

\[
                         |R-I|\le L+4r-1.
\tag{5.8}
\]

Apply (5.7)--(5.8) to every orbit satisfying Lemma 5.1 and charge all
exceptional orbits trivially by \(m\). Equations (5.1) and (0.9) give
(5.5). \(\square\)

For \(L=\lfloor\alpha m\rfloor\) and fixed \(0<\alpha<1\), (5.5) is (0.10).
Thus the selector spreads the *location of the active arc* uniformly; it
does not disperse the \(r\) selected pairs around the circle.

## 6. Audit against the fixed-suffix occurrence dual

Let \(R^\sharp\) be the union of the physical coordinate pairs indexed by
\(R\). A necklace cell with

\[
                         I(X)\cap R=\varnothing
\tag{6.1}
\]

has one fixed restriction on \(R^\sharp\) throughout the cell. Therefore
every lower intersection and upper union emitted inside that cell agrees
with its owner on \(R^\sharp\), exactly as in the old fixed-suffix proof.

Cells violating (6.1) must be charged as mobile. Let \(M_R\) denote their
total owner mass, as in (5.4). For \(a<|R^\sharp|/2\), define the two
extreme target families

\[
\begin{aligned}
 {\cal Z}_{q,a}^-&=
 \{T\in\binom{[2m]}{m-q}:|T\cap R^\sharp|\le a\},\\
 {\cal Z}_{q,a}^+&=
 \{T\in\binom{[2m]}{m+q}:|T\cap R^\sharp|
                         \ge |R^\sharp|-a\},
\end{aligned}
\tag{6.2}
\]

and let

\[
 B_a=\#\{X\in\binom{[2m]}m:|X\cap R^\sharp|\le a\}.
\tag{6.3}
\]

Write \(E_{\rm leave}=W-G\). For a fractional exact-owner resolution, let
\(\ell_q^\pm(T)\) be the occurrence load at \(T\) and define

\[
 D_q^\pm=\sum_T(1-\ell_q^\pm(T))_+.
\tag{6.3a}
\]

For an integral resolution this is the number of uncovered labelled
targets of that sign.

### Theorem 6.1 (residual fixed-core dual)

For every exact-owner resolution inside the necklace cells, its uncovered
mass satisfies

\[
 \boxed{
 D_q^-+D_q^+
 \ge |{\cal Z}_{q,a}^-|+|{\cal Z}_{q,a}^+|
      -2B_a-2M_R-2E_{\rm leave}.}
\tag{6.4}
\]

#### Proof

On a frozen cell, a lower occurrence can enter
\({\cal Z}_{q,a}^-\) only when its owner is in the lower extreme event,
whose total middle mass is at most \(B_a\). The upper event has the same
middle mass by complementation. Exact ownership therefore gives frozen
capacity at most \(2B_a\).

A mobile or omitted owner supplies at most one occurrence of each sign at
the fixed depth. Charging all of them without restriction adds at most
\(2M_R+2E_{\rm leave}\). Subtract this total occurrence capacity from the
two target demands in (6.2). \(\square\)

For the terminal-quarter choice in the published parity-complete suffix
dual, \(L/m\to1/4\). Hence

\[
                         M_R=(1/4+o(1))W.
\tag{6.5}
\]

Put

\[
 d_A=A\sqrt{2/3},\qquad
 u_A=\max\left\{1,{A^2+\log2+1\over d_A}\right\},
 \qquad x_A=d_A+u_A.
\tag{6.6a}
\]

The published dual's displayed constant is

\[
 \kappa_A=e^{-A^2}\Phi(-u_A)-\Phi(-x_A),
\tag{6.6}
\]

and is positive: the standard Mills bounds give
\(\Phi(-u_A)/\Phi(-x_A)>e^{A^2}\) for this choice. Since \(u_A\ge1\),

\[
                         0<\kappa_A<\Phi(-1)<1/4.
\tag{6.7}
\]

After (6.5) is charged, that specific dual no longer gives a positive
lower bound. Thus the rotation-equivariant selector genuinely evades the
published *terminal-quarter* theorem.

It does not evade every fixed-core argument. Equation (5.5) says that a
fixed \(\alpha\)-core remains frozen on \(1-\alpha-o(1)\) of the mass.
Several separated cores can be combined so that one short active arc meets
only a few of them. Whether their target weights can be chosen within the
dual cap \(0\le y_T\le1\) to recover a positive coefficient is a new
multi-core LP. The next theorem solves that LP negatively for the necklace
atlas.

## 6A. A finite multi-core Gaussian Hall cut

Fix \(A>0\), assume (0.9), and put

\[
 q=\lfloor A\sqrt m\rfloor\le r,
 \qquad K=K_A=\left\lceil e^{4/A^2}+2\right\rceil.
\tag{6A.1}
\]

Partition the pair circle into \(K\) consecutive blocks
\(B_1,\ldots,B_K\), whose sizes differ by at most one, and write

\[
 B_j^\sharp=\bigcup_{i\in B_j}P_i,qquad
 \alpha_j={|B_j|\over m},qquad
 \alpha=(\alpha_1,\ldots,\alpha_K).
\tag{6A.2}
\]

Since \(K\) is fixed and \(r=o(m)\), every block has length greater than
\(4r\) for all sufficiently large \(m\).

### Lemma 6A.1 (one-block localization)

Apart from an exceptional owner mass \(E_m\) satisfying

\[
 {E_m\over W}
 \le e^{-\Omega(m)}+m(2m+1)e^{-r/4}+{4Kr\over m}
 =o(1),
\tag{6A.3}
\]

every whole necklace cell has its active set contained in one block
\(B_j\).

#### Proof

The first two terms charge the discarded and long-arc owners. On a free
rotation orbit whose selected set lies in a fixed arc of length at most
\(4r\), at most \(4r\) rotations make that arc cross any prescribed block
boundary. There are \(K\) boundaries. The short-arc event and the crossing
event are constant on each orientation cell, so this is an owner-mass
estimate, not merely a cell-count estimate. \(\square\)

For any set \(S\), let

\[
 n(S)=\bigl(|S\cap B_1^\sharp|,\ldots,
             |S\cap B_K^\sharp|\bigr).
\tag{6A.4}
\]

Put \(A_m=q/\sqrt m\), and define the centered occupancy vectors

\[
\begin{aligned}
 y(X)&={n(X)-m\alpha\over\sqrt m},\\
 z^-(T)&={n(T)-(m-q)\alpha\over\sqrt m},\\
 z^+(U)&={n(U)-(m+q)\alpha\over\sqrt m}.
\end{aligned}
\tag{6A.5}
\]

They lie in

\[
                         V_K=\{z\in\mathbb R^K:\sum_jz_j=0\}.
\tag{6A.6}
\]

Let \(v_j^{(m)}=e_j-\alpha\).

### Lemma 6A.2 (exact occupancy displacement)

If a nonexceptional cell is supported in \(B_j\), then every emitted target
of the indicated rank satisfies

\[
 y(X)=z^-(T)+A_m v_j^{(m)},
 \qquad
 y(X)=z^+(U)-A_m v_j^{(m)}.
\tag{6A.7}
\]

#### Proof

A lower trace deletes exactly \(q\) owner elements, all in
\(B_j^\sharp\), while an upper trace adds exactly \(q\) elements there.
All other block occupancies are unchanged. Substitution into (6A.5) gives
(6A.7) coordinate by coordinate. \(\square\)

For a bounded Jordan-measurable \({\cal U}\subset V_K\), let
\({\cal T}_{m}^{\pm}({\cal U})\) be the rank-\(m\pm q\) targets whose
corresponding \(z^\pm\) lies in \({\cal U}\). Exact ownership and Lemma
6A.2 give the literal capacity bounds

\[
\begin{aligned}
 M_q^-&\ge |{\cal T}_m^-({\cal U})|
 -\sum_{j=1}^K\#\{X:y(X)\in{\cal U}+A_mv_j^{(m)}\}-E_m,\\
 M_q^+&\ge |{\cal T}_m^+({\cal U})|
 -\sum_{j=1}^K\#\{X:y(X)\in{\cal U}-A_mv_j^{(m)}\}-E_m.
\end{aligned}
\tag{6A.8}
\]

The sums may count an owner more than once; this only makes the upper bound
on available capacity more generous.

### Lemma 6A.3 (block-occupancy limit)

For fixed \(K,A\), let \(\mu_K\) be the probability measure on \(V_K\)
with density

\[
 d\mu_K(z)=\left({K\over\pi}\right)^{(K-1)/2}
              e^{-K\|z\|_2^2}\,d\lambda_{V_K}(z).
\tag{6A.9}
\]

For every bounded Jordan-measurable \({\cal U}\),

\[
 {\#\{X:y(X)\in{\cal U}\}\over W}\longrightarrow\mu_K({\cal U}),
\tag{6A.10}
\]

and

\[
 {|{\cal T}_m^\pm({\cal U})|\over W}
 \longrightarrow e^{-A^2}\mu_K({\cal U}).
\tag{6A.11}
\]

#### Proof

The block occupancies have the multivariate hypergeometric law. Exactly,

\[
 \operatorname{Cov}(n_i,n_j)
 ={m^2\over2m-1}(\alpha_i\mathbf1_{i=j}-\alpha_i\alpha_j).
\tag{6A.12}
\]

After division by \(m\), and since \(\alpha_i\to1/K\), its restriction to
\(V_K\) converges to \((2K)^{-1}I_{V_K}\). Stirling's formula uniformly
for occupancies within \(O(\sqrt m)\) of their means gives (6A.9), and the
lattice Riemann sum gives (6A.10). At ranks \(m\pm q\) the limiting
covariance is the same, while

\[
 {\binom{2m}{m\pm q}\over W}\longrightarrow e^{-A^2};
\tag{6A.13}
\]

this proves (6A.11). Gaussian tail bounds obtained from the same Stirling
expansion justify truncation outside the displayed bounded region.
\(\square\)

### Theorem 6A.4 (explicit multi-core deficit)

Let

\[
 v_j=e_j-{1\over K}{\bf1},\qquad
 \eta_A={\log(3/2)\over2KA},\qquad
 {\cal U}=B_{V_K}(0,\eta_A).
\tag{6A.14}
\]

Then every cellwise exact factor satisfies, separately for both signs,

\[
 \boxed{
 M_q^\pm\ge(c_A-o(1))W,
 \qquad
 c_A={1\over4}e^{-A^2}\mu_K({\cal U})>0.}
\tag{6A.15}
\]

#### Proof

Since \(\|v_j\|^2=1-1/K\), for \(z\in{\cal U}\),

\[
 {e^{-K\|z\pm Av_j\|^2}\over e^{-K\|z\|^2}}
 \le e^{-(K-1)A^2+2KA\eta_A}.
\tag{6A.16}
\]

Therefore

\[
 \sum_{j=1}^K\mu_K({\cal U}\pm Av_j)
 \le K e^{-(K-1)A^2+2KA\eta_A}\mu_K({\cal U}).
\tag{6A.17}
\]

The explicit choice (6A.1) satisfies

\[
                         K e^{-(K-2)A^2}\le{1\over2}.
\tag{6A.18}
\]

For completeness, with \(t=4/A^2\), one has
\(A^2(K-2)\ge4e^t/t\). If \(t<\log3\), this exceeds
\(\log(2K)\) directly from \(K<e^t+3<6\); if \(t\ge\log3\), use
\(2(e^t+3)\le4e^t\) and
\(4e^t/t\ge t+\log4\), the latter following from
\(e^t\ge1+t+t^2/2\). This proves (6A.18).

By (6A.14), \(e^{2KA\eta_A}=3/2\). Hence (6A.17)--(6A.18) give

\[
 \sum_{j=1}^K\mu_K({\cal U}\pm Av_j)
 \le {3\over4}e^{-A^2}\mu_K({\cal U}).
\tag{6A.19}
\]

Since \(A_mv_j^{(m)}\to Av_j\) and the boundary of the ball
\({\cal U}\) has \(\mu_K\)-measure zero, inner and outer
\(\varepsilon\)-neighborhood sandwiches extend Lemma 6A.3 from fixed sets
to the finitely many moving translates in (6A.8).

Substitute Lemma 6A.3 and (6A.3) into (6A.8). The target demand exceeds
the optimistically overcounted compatible-owner supply by at least the
constant in (6A.15). \(\square\)

Thus the old single terminal-quarter cut is genuinely evaded, but the
rotating short arc is caught by finitely many fixed block cores. Changing
the order or the parity-complete seed inside a cell does not affect this
argument. To escape it, a non-\(o(W)\) owner mass must use physical windows
whose \(q\)-support meets at least two of the fixed blocks. Merely crossing
a necklace-cell boundary does not by itself defeat the occupancy cut if
all \(q\) changes remain in one block.

## 7. Candidate degrees and what has actually improved

There are \(G/2^r\) cells. In one \(Q_r\)-cell, the number of affine
\(q\)-faces is

\[
                         2^{r-q}\binom rq.
\tag{7.1}
\]

Every affine face has one physical lower intersection and one physical
upper union. The local face-separation property says that distinct faces in
one cell have distinct targets of either fixed sign. Hence the total
cell--target candidate incidence is exactly

\[
 {G\over2^r}2^{r-q}\binom rq
 =G{\binom rq\over2^q},
\tag{7.2}
\]

proving (0.14).

If \(d_q^\epsilon(T)\) is the number of candidate cells for target \(T\),
then

\[
 \sum_Td_q^\epsilon(T)=G{\binom rq\over2^q}.
\tag{7.3}
\]

The cyclic symmetry gives only

\[
                         d_q^\epsilon(\tau T)
                         =d_q^\epsilon(T).
\tag{7.4}
\]

It does not make \(d_q^\epsilon(T)\) independent of the cyclic gap pattern,
the empty/split/full status pattern, or the exterior orientation data.

### Proposition 7.1 (failure of a \(q\)-design conclusion)

If \(D\) is not contained in a cyclic \(4r\)-arc, then

\[
 N_q(D)\le
 \#\{X\in{\cal G}_r:\ell(X)>4r\}
 \le m(2m+1)e^{-r/4}W.
\tag{7.5}
\]

The fraction of
\(q\)-subsets of \(\mathbb Z_m\) which are contained in some such arc is at
most

\[
 m\,{\binom{4r}q\over\binom mq}
 \le
 m\left({4r\over m-q+1}\right)^q.
\tag{7.6}
\]

#### Proof

Every \(q\)-subset of \(I(X)\) lies in the same \(4r\)-arc as \(I(X)\)
whenever \(\ell(X)\le4r\). Thus only the exceptional owners from Lemma 5.1
can contribute, proving (7.5). Choose the start of an arc and then a
\(q\)-subset inside it to obtain the first bound in (7.6). The standard
product comparison of binomial coefficients gives the second. \(\square\)

Thus, in the regime (0.17), almost every abstract \(q\)-direction set has
only exceptional selector incidence. This is not yet a literal target-Hall
obstruction: a physical target can have several possible touched direction
sets. It is an exact obstruction to inferring target lower tails from
(4.2).

There is also an exact typewise degree comparison in the candidate-cell
graph of (7.3). Let \(G_f\) be the number of retained owners of full-pair
type \(f\). The total type-\(f\) cell--face incidences are
\((G_f/2^r)2^{r-q}\binom rq\), so the average degree on the lower target
class of size \(T_{f,q}\) is

\[
                         {G_f\over2^qT_{f,q}}\binom rq.
\tag{7.7}
\]

In the full fixed-pair status-cell graph, every target degree is
\(\binom{f+q}q\). The exact double-counting identity

\[
 {V_f\over2^q}\binom{m-2f}q
 =T_{f,q}\binom{f+q}q
\tag{7.8}
\]

therefore gives the exact ratio

\[
 {\text{necklace average target degree}
   \over\text{full fixed-pair target degree}}
 ={G_f\over V_f}
  {\binom rq\over\binom{m-2f}q}.
\tag{7.9}
\]

Thus the selector improves label symmetry at one coordinate but thins the
full face catalogue. It cannot change the deficient type capacity ratio
\(V_f/T_{f,q}\) from Theorem 4A.2.

The mean (7.3) is the same for every partition into equal physical
\(Q_r\)-cells. What the new selector changes is the geometry of the degree
distribution, not its mean. Theorems 4A.2 and 6A.4 show that no pointwise
lower-tail theorem strong enough for coefficient one can hold in this
cellwise fixed-pair atlas. A different construction would require one of:

1. a polynomial family of transverse cyclic pair frames whose combined
   shape orbits cover the bad targets.
2. a legal cross-status-cell splice which changes the fixed-pair type and
   makes a positive-density family of protected windows meet at least two
   fixed blocks; or
3. a nonlocal carrier which fails one-block localization while retaining
   exact middle ownership.

None follows from uniform coordinate marginals.

There is also no automatic two-sign symmetry. Complementation exchanges
\(\mathsf E\) and \(\mathsf F\), while a fixed lexicographic order on the
three letters need not commute with that exchange. Thus lower and upper
target degrees must be audited jointly; one cannot obtain the upper theorem
by silently complementing the selector. The upper bounds in Theorems 4A.2
and 6A.4 were instead proved directly, respectively by empty-pair type and
the negative occupancy translates.

## 8. Exact proved boundary

The proved positive theorem is:

> For \(r\le m/4\), apart from \(e^{-\Omega(m)}W\) owners, the middle layer has an exact
> rotation-equivariant partition into status-stable physical \(Q_r\)-cells
> with exactly uniform selected-pair and endpoint marginals.

The negative theorem is:

> For every fixed \(A>0\), every choice of exact locally geodesic factors
> which keeps each protected window inside one status-stable necklace cell
> misses at least \((\delta_A-o(1))W\) lower targets and the same number of
> upper targets at \(q=\lfloor A\sqrt m\rfloor\le r\). Under
> \(\log m\ll r=o(m)\), it also violates the explicit \(K_A\)-core Hall
> cut by at least \((c_A-o(1))W\) in each sign.

Thus there is no remaining Hall lemma inside the proposed fixed-pair
cellwise architecture. The shortest possible escape statement would have
to construct an exact owner-simple factor with a non-\(o(W)\) family of
Gaussian-depth windows which either changes the unordered ambient pairing
or genuinely changes status type, and whose \(q\)-support is not contained
in one fixed block.
It must then prove the simultaneous two-sign target Hall inequalities and
the ordered-port toll. That is a materially different outer atlas, not an
unproved property of the necklace selector.

## 9. Audit summary

1. Unique lexicographic rotation is valid exactly on aperiodic statuses.
2. Periodic/tied statuses and owners with fewer than \(r\) splits have
   exponentially small total mass for \(r\le m/4\).
3. Varying selected orientations fixes the status, canonical root, and
   selector, so the packet partition is exact.
4. Rotation equivariance gives exact singleton marginals, not a
   \(q\)-design.
5. For \(\log m\ll r=o(m)\), the selected positions form a short active
   arc which rotates uniformly.
6. The published terminal-quarter suffix dual is neutralized
   quantitatively, but the explicit \(K_A\)-core Gaussian cut leaves
   \((c_A-o(1))W\) holes in each sign.
7. More simply, the exact full/empty-pair type potential leaves
   \((\delta_A-o(1))W\) holes in each sign, without any localization
   assumption.
8. The average target candidate degree is unchanged and the candidate-cell
   typewise face graph is thinned by the exact ratio (7.9).
9. The selector is not automatically complement-equivariant; both upper
   cuts were proved directly rather than inferred from it.
10. The cellwise fixed-pair necklace route is rigorously closed. No MWB,
    SCI, or coefficient-one implication is asserted.
