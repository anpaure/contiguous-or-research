# Protected multi-order chain rounding and the exact one-copy gap

**Date:** 2026-08-01  
**Lane:** K, protected multi-order flags  
**Status:** exact one-copy theorem for the complete (or
path-splice-complete) local-order atlas, including any \(h\le m+1\)
prescribed root flags. A sharp three-pin obstruction rules out balanced
floor/ceiling suffix loads for a general prepared bank. A literal
determinant-two minor shows why a finite sampled atlas needs a correlated
chain argument. No owner/turn Hall, residence, upper chronology, or
additive-constant word theorem is asserted.

## 0. Verdict

Put \(n=2m+1\), and let

\[
   \mathcal L_j=\binom{[n]}{m-j}\qquad(0\le j\le D),
   \quad D\le m-1.
\]

An order flag at a root \(Q\in\mathcal L_0\) is exactly a descending
Boolean path

\[
       Q=S_0\supset S_1\supset\cdots\supset S_D,
       \qquad S_j\in\mathcal L_j.                 \tag{0.1}
\]

There are two different integral targets.

1. **Marked one-copy cover:** every lower target must occur in at least one
   chosen flag; one occurrence can then be marked. Duplicates are harmless.
2. **Balanced unmarked loads:** every target at depth \(j\) must have load
   \(\lfloor\rho_j\rfloor\) or \(\lceil\rho_j\rceil\), where
   \(\rho_j=|\mathcal L_0|/|\mathcal L_j|\).

Without pins, the second (stronger) target is exactly solvable in the
complete atlas by an integral node-capacitated flow. With
\(h\le m+1\) arbitrary prepared flags, the first target is still exactly
solvable. The second is false for three prepared roots under one robust
order throughout \(\Theta(\min\{D,\sqrt m\})\) initial depths.

The complete-atlas proof does **not** round the exponentially smaller
random global-order menu. That menu is not closed under exchanging path
suffixes. A literal non-TU chain minor identifies the first exact
correlation gap. It is a proof barrier, not a counterexample to the full
sampled menu, whose additional root--order columns may repair the minor.

## 1. Exact uniform fractional suffix law

Choose independently at each root \(Q\in\mathcal L_0\) a uniformly random
ordering of its \(m\) elements, and let \(S_j\) be the suffix after its first
\(j\) elements are deleted. Fix \(S\in\mathcal L_j\). There are

\[
             \binom{m+j+1}{j}                       \tag{1.1}
\]

roots containing \(S\), and for each such root

\[
       \Pr(S_j=S)=\binom mj^{-1}.
\]

Hence every target at depth \(j\) has exactly the same fractional load

\[
 \rho_j=
   \frac{\binom{m+j+1}{j}}{\binom mj}
   =\frac{|\mathcal L_0|}{|\mathcal L_j|}\ge1.      \tag{1.2}
\]

This is a marginal statement. It neither fixes prepared roots nor selects
one whole chain at every root.

### Theorem 1.1 (unprotected balanced chain rounding)

In the complete local-order atlas one can select one flag at every root so
that, simultaneously for every \(1\le j\le D\), every
\(S\in\mathcal L_j\) has integral load

\[
                  \lfloor\rho_j\rfloor
       \quad\text{or}\quad
                  \lceil\rho_j\rceil.                          \tag{1.3}
\]

#### Proof

Use the layered containment network (4.1). Give every root unit supply and
split every lower node into an entrance and exit joined by a capacity arc.
At depth \(j\), give every such node the integral lower and upper capacities

\[
                    \lfloor\rho_j\rfloor,\qquad
                    \lceil\rho_j\rceil.                         \tag{1.4}
\]

There is a feasible fractional flow: from every \(r\)-set split its incoming
mass equally among its \(r\) children. By symmetry its load at depth \(j\)
is exactly \(\rho_j\), as computed in (1.2). The node-split network has an
integral incidence matrix and all supplies and bounds in (1.4) are
integers. Therefore the standard integral-flow theorem gives an integral
feasible flow. Decompose its \(W\) units into root-to-bottom paths. These
paths are order flags and have precisely the loads (1.3). \(\square\)

Thus the complete-host chain correlation itself is not an integrality
obstruction. The obstruction begins when the available path columns are
restricted or when prescribed paths make the residual node capacities
infeasible.

### Corollary 1.2 (exact prepared-flow criterion)

Let \(c_j(S)\) be the number of prepared paths using
\(S\in\mathcal L_j\). A balanced floor/ceiling extension exists in the
complete atlas if and only if the residual layered network, with the
prepared source units removed, has a feasible flow and node bounds

\[
 \max\{0,\lfloor\rho_j\rfloor-c_j(S)\}
 \ \le f_j(S)\le\
 \lceil\rho_j\rceil-c_j(S).                                  \tag{1.5}
\]

Whenever a fractional residual flow exists, an integral one exists.

#### Proof

Necessity follows by deleting the prepared paths from an extension.
Conversely add any residual flow to the prepared paths. Node splitting
turns (1.5) into ordinary lower and upper arc bounds. The integral-flow
theorem proves the last assertion. \(\square\)

This is a finite exact max-flow/min-cut criterion. It is not automatic from
rankwise marginals: all ranks share the same path units.

## 2. A sharp first-shadow reserve

For \(\mathcal A\subseteq\mathcal L_1\), let

\[
 N(\mathcal A)=
 \{Q\in\mathcal L_0:S\subset Q\text{ for some }S\in\mathcal A\}.
                                                               \tag{2.1}
\]

### Lemma 2.1 (middle first-shadow surplus)

For every nonempty \(\mathcal A\subseteq\mathcal L_1\),

\[
                   |N(\mathcal A)|\ge|\mathcal A|+m+1.        \tag{2.2}
\]

#### Proof

Complementing gives a family
\(\mathcal F\subseteq\binom{[2m+1]}{m+2}\), and complements identify
\(N(\mathcal A)\) with its one-step lower shadow. Put \(k=m+2\), and write

\[
                         |\mathcal F|=\binom{x}{k}
\]

for the unique real \(x\in[k,2k-3]\). Lovász--Kruskal--Katona gives

\[
                 |\partial\mathcal F|\ge\binom{x}{k-1}.       \tag{2.3}
\]

The chord

\[
 g(x):=\binom{x}{k-1}-\binom{x}{k}
      =\binom{x}{k-1}\frac{2k-x-1}{k}                         \tag{2.4}
\]

is increasing on this interval. Indeed,

\[
 \frac{g'(x)}{g(x)}
 =\sum_{i=0}^{k-2}\frac1{x-i}-\frac1{2k-x-1}>0,               \tag{2.5}
\]

because the sum is at least \((k-1)/x\), while

\[
 \frac{k-1}{x}\ge\frac1{2k-x-1}
 \quad\Longleftrightarrow\quad
 x\le\frac{(k-1)(2k-1)}k=2k-3+\frac1k.                        \tag{2.6}
\]

Thus \(g(x)\ge g(k)=k-1=m+1\), proving (2.2). \(\square\)

### Corollary 2.2 (prepared-root deletion is Hall-safe)

If \(H\subseteq\mathcal L_0\) and \(|H|=h\le m+1\), then the containment
graph from \(\mathcal L_1\) to \(\mathcal L_0-H\) has a matching saturating
all of \(\mathcal L_1\).

#### Proof

For every nonempty \(\mathcal A\subseteq\mathcal L_1\),

\[
 |N(\mathcal A)-H|
 \ge |\mathcal A|+m+1-h
 \ge |\mathcal A|.
\]

Apply Hall. \(\square\)

The \(m+1\) reserve is stronger than the bare normalized-matching ratio
\(|N(\mathcal A)|\ge(1+2/m)|\mathcal A|\), and is exactly what makes an
arbitrary bounded protected bank harmless at the first layer.

## 3. Exact protected marked one-copy rounding

### Theorem 3.1 (protected complete-atlas selector)

Let \(0\le D\le m-1\). Prescribe arbitrary paths (0.1) at \(h\le m+1\)
distinct prepared roots. In the complete local-order atlas one can choose
one path at every other root so that

\[
 \forall j\in\{1,\ldots,D\},\quad
 \forall S\in\mathcal L_j,\quad
 S\text{ occurs in at least one selected path}.                \tag{3.1}
\]

#### Proof

Call roots outside the prepared bank flexible tokens. By Corollary 2.2,
match every member of \(\mathcal L_1\) to a distinct flexible parent.
Send each matched token to that child, and every unused flexible root token
to an arbitrary child. Every member of \(\mathcal L_1\) now carries at
least one flexible token.

Inductively suppose rank \(r\), \(1\le r\le m-1\), carries multiplicities
\(w(A)\ge1\) for all \(A\in\binom{[n]}r\). Replace \(A\) by \(w(A)\)
labelled copies. For
\(\mathcal Y\subseteq\binom{[n]}{r-1}\), incidence counting gives

\[
 (n-r+1)|\mathcal Y|\le r|N(\mathcal Y)|.                      \tag{3.2}
\]

Since \(r\le m\), \(|N(\mathcal Y)|\ge|\mathcal Y|\). Therefore the
number of neighboring token copies is at least

\[
 \sum_{A\in N(\mathcal Y)}w(A)
 \ge |N(\mathcal Y)|\ge|\mathcal Y|.                           \tag{3.3}
\]

Hall assigns one distinct parent token to every child. Send the remaining
tokens arbitrarily downward. The new multiplicities are again at least one
everywhere. Iterate, retaining token identities. Every flexible root traces
one descending path, and the prepared paths may be added without harming
coverage. \(\square\)

Equivalently, choose a containment matching saturating each lower shore.
At the top adjacency use Corollary 2.2 so that the matching avoids the
prepared roots; below it use ordinary normalized matching. The union is a
chain forest covering every high target once. Reading each component
downward from its unprepared rank-\(m\) endpoint gives the marked flag, and
the prescribed flags are quarantined unmarked. This is the SCD/chain-forest
form proved independently in
MATH_THEOREM_SCD_EXACT_ALL_HIGH_ORDERED_CHAIN_SELECTOR_AND_PROTECTED_GATE_20260801.md.

### Corollary 3.2 (one common robust prepared order)

For \(h=O(1)\) and sufficiently large \(m\), all prepared roots may use the
one order supplied by the bounded-prepared robust-order theorem, while the
complete selected table remains marked-one-copy exact at every high suffix
rank.

This statement fixes the prepared **root flags** only. It does not preserve
the ordered-shift portal lists from those roots, because each certified turn
also uses the prepared order at its head root; see Section 7.

Every constructed path is induced by a total order: list the successive
deleted elements first, the remaining root elements next, and the outside
coordinates last. Thus the selected flags lie in a common adaptive menu of
at most

\[
                         1+|\mathcal L_0|-h                     \tag{3.4}
\]

global orders. This is an existence bound, not the
\(O(m2^d\exp(O(d^2/m)))\) random-menu bound.

## 4. Network-flow closure and the sampled-atlas gap

Represent allowed flags by paths in

\[
 \mathcal L_0\longrightarrow\mathcal L_1\longrightarrow\cdots
 \longrightarrow\mathcal L_D.                                  \tag{4.1}
\]

Call an atlas **path-splice-complete** if every path formed from its
permitted consecutive arcs is available at its source; equivalently, two
available flags meeting at a suffix may exchange their remaining suffixes.

### Corollary 4.1 (flow sufficient condition)

Theorem 3.1 remains true in an atlas which contains the prepared flags, has
the first-layer Hall property after deleting them, and is path-splice-
complete on all arcs used by the token construction.

Indeed this is a lower-bounded network flow with an integral constraint
matrix. A finite independently sampled global-order menu is generally not
path-splice-complete, so this corollary does not settle the random atlas.

## 5. Literal determinant-two chain minor

Take rank-five roots

\[
 Q_1=12345,\qquad Q_2=12346,
\]

rank-three suffixes \(A_0=123,A_1=124\), and rank-one suffixes
\(B_0=1,B_1=2\). All four containments \(B_v\subset A_u\) hold. Consider
the four literal order-flag columns

\[
\begin{array}{c|cc}
 &\text{rank three}&\text{rank one}\\ \hline
e_{00}&Q_1:A_0&B_0\\
e_{11}&Q_1:A_1&B_1\\
f_{01}&Q_2:A_0&B_1\\
f_{10}&Q_2:A_1&B_0.
\end{array}                                                    \tag{5.1}
\]

Their omitted rank-four and rank-two suffixes can be filled along the
displayed nested chains, so all columns extend to total orders.

Weight \(1/2\) on every column gives load one on both root rows and all
four displayed target rows. No integral choice exists. To cover both
\(A\)-rows, the roots must choose opposite \(A\)-labels; then their
\(B\)-labels coincide.

This proves that a root-occurrence-restricted chain matrix is not TU and
that rankwise SCD/matching certificates do not automatically synchronize.
It does **not** prove a full sampled global-order menu infeasible: each
total order used above also induces columns at the other root, and those
extra columns may remove the obstruction.

Thus the exact finite-menu one-copy gate is an alternating-chain
splicing/absorption theorem for the complete root--order column set, not
another marginal Hall estimate.

## 6. Sharp obstruction to balanced floor/ceiling loads

The marked-cover theorem permits duplicate unmarked suffixes. If the target
is instead the balanced unmarked profile, even the complete atlas cannot
accommodate an arbitrary three-root robust bank.

### Theorem 6.1 (three prepared roots violate every initial cap-two rank)

Let \(d\ge2\). Choose an \((m-1)\)-set

\[
 S=\{s_1,\ldots,s_{m-1}\}
\]

and distinct \(a_1,a_2,a_3\notin S\). Put
\(p_i=S\cup\{a_i\}\), and use one total order

\[
 a_1\prec a_2\prec a_3\prec
 s_1\prec\cdots\prec s_{m-1}\prec\text{(all remaining labels)}. \tag{6.1}
\]

At every deletion depth \(1\le j<d\), all three prepared flags have the
same suffix

\[
                 T_j=S-\{s_1,\ldots,s_{j-1}\}.                 \tag{6.2}
\]

Moreover these are legitimate robust prepared roots: take
\[
 Q_i=\{a_i,s_1,\ldots,s_{d-1}\}\subseteq p_i
\]
in the bounded-prepared order theorem.

The uniform fractional load obeys

\[
 \rho_j
 =\prod_{i=0}^{j-1}\left(1+\frac{j+1}{m-i}\right)
 \le \exp\!\left(\frac{j(j+1)}{m-j+1}\right).                  \tag{6.3}
\]

Hence whenever

\[
                    j(j+1)<(m-j+1)\log2,                       \tag{6.4}
\]

we have \(1<\rho_j<2\), so every floor/ceiling realization has target cap
two. Equation (6.2) already gives \(T_j\) load three. Therefore balanced
floor/ceiling completion is impossible at every depth satisfying (6.4).
The number of violated ranks is

\[
 \min\!\left\{d-1,\
 \max\{j:j(j+1)<(m-j+1)\log2\}\right\}
 =\Theta(\min\{d,\sqrt m\}).                                  \tag{6.5}
\]

\(\square\)

This is not a cover obstruction: the three coincident occurrences can be
left unmarked except for one. It is exactly the distinction between marked
one-copy feasibility and balanced suffix-multiplicity rounding.

### Corollary 6.2 (sharp scale of the generic prepared-load error)

For any \(h\) prescribed flags there is a selector whose total positive
cap excess and total lower-bound shortfall, summed over all \(D\) ranks, is
at most \(2hD\). For the three-root construction of Theorem 6.1, the
positive cap excess alone is at least the quantity in (6.5). Consequently
no dimension-independent balanced-load defect follows for an arbitrary
bounded bank fixed to one order.

#### Proof

Start with the balanced selector of Theorem 1.1 and replace its flag at
each prepared root by the prescribed flag. At each rank a replacement
removes one occurrence and adds one occurrence. Thus the load vector at
that rank changes in \(\ell_1\) by at most \(2h\), which bounds its distance
from the floor/ceiling box by the same amount. Summing gives \(2hD\).
Theorem 6.1 contributes at least one unit above the cap at every rank
counted in (6.5). \(\square\)

This upper bound concerns multiplicity balance and may have holes. Theorem
3.1 separately gives zero marked-cover holes, but does not keep the
floor/ceiling profile. Combining both conclusions with \(O(1)\) total
error is precisely what the three-pin lower bound forbids in general.

## 7. The mixed-order head quantifier destroys the naive portal list

Let a prepared tail \(p\) use one order \(\pi\), with

\[
                        z_1\prec_\pi\cdots\prec_\pi z_m.
\]

The ordered-shift candidate indexed by \(\beta\notin p\) has head

\[
                    q_\beta=p-\{z_1\}+\{\beta\}.                \tag{7.1}
\]

The proof of that candidate assumes that \(q_\beta\) also uses \(\pi\).
If its selected order is \(\sigma\), write its first \(d-1\) elements as
\(w_1,\ldots,w_{d-1}\). Literal survivor containment is equivalent to

\[
 w_1=z_2,\quad\ldots,\quad w_{d-2}=z_{d-1},\qquad
 w_{d-1}\in\{z_d,\ldots,z_m\}.                                 \tag{7.2}
\]

Thus only \(m-d+1\) of the \((m)_{d-1}\) ordered head prefixes are
compatible. Under an independently uniform head order, one prepared-tail
candidate survives with probability

\[
                       \frac{m-d+1}{(m)_{d-1}},                 \tag{7.3}
\]

and the expected surviving list among its \(m+1\) candidate heads is at
most

\[
                 (m+1)\frac{m-d+1}{(m)_{d-1}}.                 \tag{7.4}
\]

This is \(O(1)\) already at \(d=3\) and tends to zero for every fixed
\(d\ge4\). Consequently, fixing \(O(1)\) tails to one robust order inside a
mixed one-order-per-root selector does not preserve the \(\Omega(m)\)
portal degree of the complete single-order table.

One must either constrain the flags at linearly many candidate heads or
prove a new cross-order head-robustness theorem in the final selected table.
There is also a shore issue: the displayed ordered-shift list is
tail-anchored, whereas a head- or owner-anchored odd-cycle portal needs a
separate conjugate construction.

The complete-atlas marked-cover theorem can afford the first option.

### Corollary 7.1 (linear frozen-head halo)

Let \(t\) prepared task tails use one robust order. Put

\[
 R_0=m+1-(t-1)d,\qquad
 \ell_0=\min\!\left\{R_0,\left\lfloor\frac{m+1-t}{t}\right\rfloor\right\}.
                                                               \tag{7.5}
\]

If \(\ell_0>0\), then in the complete local-order atlas one can freeze the
task tails and \(\ell_0\) certified ordered-shift heads per tail to that same
order, and still complete an exact marked one-copy suffix selector. Every
task tail has a frozen list of \(\ell_0\) literal portal turns of
pair-codegree one. After any bank of at most \(b\) foreign resource rows,
none equal to the task tail, at least \(\ell_0-b\) candidates remain.

#### Proof

The bounded-prepared order theorem leaves at least \(R_0\) candidates at
each task tail. Choose any \(\ell_0\) of their head roots and freeze those
head flags to the same order. The union of all
frozen tails and head halos has size at most

\[
                         t+t\ell_0\le m+1.                       \tag{7.6}
\]

Theorem 3.1 therefore completes every marked suffix row using the remaining
roots. Since both endpoints of every retained candidate use the prepared
order, the ordered-shift proof applies literally. Its resource
pair-codegree-one statement is unchanged by restriction to a sublist, so
each foreign row deletes at most one frozen candidate.
\(\square\)

For fixed \(t\), \(d=O(\sqrt m)\), and \(b=O(d)\), this gives
\(\ell_0-b=\Omega(m)\). Thus the complete/adaptive atlas simultaneously has
exact marked lower coverage and the robust lists needed by a bounded
tail-portal bank. In the notation of the balanced-turn theorem, on these
task rows it gives

\[
                       \delta_F(b)\ge\ell_0-b,\qquad
                       \gamma_F\le1.                            \tag{7.7}
\]

The price is a linear frozen-head halo. This still does
not place the flexible chain flow inside the support-optimal sampled menu,
provide head/owner-shore portal conjugates, or prove residual fractional
turn Hall.

## 8. Remaining owner/turn theorem

Theorem 3.1 settles only marked strict-lower coverage in the complete,
adaptive atlas. The flexible flags produced by token flow need not retain

* a fractional or integral owner/turn matching;
* functional owner attachment or balanced turn support;
* robust portal degree away from the prepared roots;
* residence or upper-shadow chronology; or
* membership in the support-optimal finite random menu.

The remaining coupled statement must either find the chain flow inside the
sampled menu while retaining owner/turn Hall, prove a chain-splicing Markov
basis whose moves preserve that Hall state, or supply a bounded absorber for
the residual chain-parity and turn odd-cycle defects. Uniform fractional
marginals alone imply none of these.
