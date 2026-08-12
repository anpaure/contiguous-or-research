# Lane W update: coordinate-relabel parents, Hamilton-aware rounding, and entropy compression at (k=15)

Date: 2026-07-28

**Index convention.** Every coordinate tuple copied from a relabel screen in
this note is zero based.  Thus `[1,12]_0=(2,13)_1`, and all other screen
labels are converted to one-based mathematical coordinates by adding one.

## 0. Result and exact boundary

This note takes the latest coordinate-relabel screen as audited input and
proves four things.

1. A coordinate relabel of the Hall-29 carrier can clear all seven *old*
   zero labels, but the whole relabelled carrier is still exactly Hall-29.
   The deficient family is merely relabelled.  Thus the new input is
   catalogue supply for a genuinely mixed chronology, not a better pure
   parent.
2. For two parents, the alternating-component cube has an exact global
   circuit invariant.  If the relative component lengths are
   \(\ell_j\), a Hamilton selection must satisfy
   \[
      \sum_{j\ \mathrm{selected}}(\ell_j-1)\equiv0\pmod 2.
   \]
   More strongly, Hamiltonicity is a maximum-genus condition.  This gives
   an exact forced-component cut and proves that a raw component-bit LLL is
   not a valid Hamilton argument.
3. There is an exact randomized/deterministic whole-selection criterion.
   Its circuit term is
   \[
      2^{c(C)-1}-1,
   \]
   where \(c(C)\) is the number of successor cycles.  This term equals the
   number of nontrivial invariant subsets avoiding a fixed root, so it
   accounts for global circuit dependence without pretending it is local.
4. A finite entropy-compression theorem is proved on **globally certified
   Hamilton states**.  At level \(h\), the state already carries one
   Hamilton circuit, exact residence, all upper witnesses, and a physical
   compiler matching of size \(16354+h\).  A sharp rollback/congestion
   inequality then implies a level-29 state and hence full compiler Hall.

The positive theorem is unconditional.  Its required k15 action atlas is
not yet constructed.  The precise remaining lemma is `CAA_29` in Section
7: produce enough correlated, Hamilton-preserving successor packets from
the fixed five-parent catalogue and prove their backward congestion beats
the entropy threshold.  Neither seven-zero positivity nor the unique
Pareto score proves `CAA_29`.

No constant-one or length-6438 word is claimed here.

## 1. Frozen k15 data and the relabel correction

Let \(P=P_{29}\) be the current Hall-29 chronology on
\[
   V=\binom{[15]}8,
   \qquad |V|=6435.
\]
Adjoin the dummy endpoint \(\partial\).  The augmented successor map of
\(P\) is a \(6436\)-cycle.

The seven current zero-candidate targets, in the order used below, are
\[
  2575,\ 5801,\ 13616,\ 13620,\ 17738,\ 21641,\ 29776.
  \tag{1.1}
\]
The rank-six targets are
\(2575,13616,17738,21641,29776\), and the rank-seven targets are
\(5801,13620\).

Among all \(\binom{15}{2}=105\) coordinate transpositions, exactly four
make every entry of (1.1) positive in the relabel-parent interior motif
catalogue.  Their count vectors are
\[
\begin{array}{c|c}
 \tau & (c_{\tau P}(T):T\text{ in the order }(1.1))\\ \hline
 (1,12)&(4,1,4,1,2,1,3)\\
 (3,4)&(3,1,2,1,3,2,2)\\
 (10,11)&(4,1,2,1,3,3,3)\\
 (3,13)&(1,1,2,1,2,1,4).
\end{array}
\tag{1.2}
\]
The unique Pareto winner in the audited screen is \(\tau_*=(1,12)\).
This Pareto statement is only for the three screen coordinates:

* minimum normalized slack on the three frozen DM families;
* number of normal arcs novel relative to the previous three-parent union;
* distance from the closest previous parent.

For \((1,12)\), the three frozen neighbourhood slacks are
\[
 (1524,1616,92),\qquad(1530,1889,359),\qquad(1374,1707,333),
 \tag{1.3}
\]
so the minimum normalized slack is \(92/1524=23/381\).  Its novel-arc
count is \(3861\), and its closest-parent distance is \(0.77622444\).
None of these diagnostics contains an overlay parity,
subtour, genus, residence, upper-window, or full compiler-Hall term.

### Lemma 1.1 (a pure relabel transports Hall deficiency exactly)

For every coordinate permutation \(\tau\), the full physical compiler
graphs of \(P\) and \(\tau P\) are isomorphic.  In particular,
\[
  \nu(G_{\tau P})=\nu(G_P)=16354,
  \tag{1.4}
\]
and if the canonical DM family \(A_{29}\) obeys
\[
   |A_{29}|=1524,
   \qquad |N_P(A_{29})|=1495,
   \tag{1.5}
\]
then
\[
   |\tau A_{29}|=1524,
   \qquad |N_{\tau P}(\tau A_{29})|=1495.
   \tag{1.6}
\]

#### Proof

The lower target universe is
\[
   \mathcal L=2^{[15]}\setminus\{\varnothing\},
   \qquad |\mathcal L|=16383.
\]
Apply \(\tau\) to every target, every vertex in the chronology, and every
named physical cell.  The cell word, its oriented collar, its mandatory
and eroded masks, and target containment are all coordinate-equivariant.
Thus
\[
   T\sim_P c
   \quad\Longleftrightarrow\quad
   \tau T\sim_{\tau P}\tau c.
\]
This is a bipartite-graph isomorphism, proving (1.4).  It carries the
neighbourhood of \(A_{29}\) bijectively to the neighbourhood of
\(\tau A_{29}\), proving (1.6). \(\square\)

Every whole relabel parent is separately a Hamilton chronology, is
residence-exact, and is upper-complete by the same equivariance.  Lemma
1.1 shows why this does not improve the lower matching.  Only a genuinely
mixed successor selection can change the full Hall score.

There is already a direct relocation witness in the four-parent catalogue:
one mixed checkpoint is a single residence-safe, upper-complete path and
still has matching \(16354/16383\), with its seven zeros moved to
\[
   1707,6669,9522,9526,17547,21832,25682.
   \tag{1.7}
\]
Thus even preserving the three geometric gates while clearing the old
labels does not prevent the Hall-29 defect from relocating.

Consequently the three transpositions dominated in the screen must not be
discarded before the circuit and congestion audit.  A dominated parent can
still be the only parent supplying a parity repair, a subtour merger, or a
low-congestion reverse action.

## 2. Exact successor-selection formulation

Put
\[
   X=V\cup\{\partial\},\qquad n=|X|=6436.
\]
Let \(f_0,\ldots,f_{d-1}\) be augmented parent successor cycles, where
\(d=O(1)\).  For the concrete catalogue one may take
\[
 \mathcal P_*=
 \{P,(1,12)P,(3,4)P,(10,11)P,(3,13)P\},
 \qquad d=5.
 \tag{2.1}
\]
Let
\[
  E_* = \bigcup_{a<d}\{(x,f_a(x)):x\in X\}.
  \tag{2.2}
\]

A **successor factor** is a permutation \(h:X\to X\) with
\((x,h(x))\in E_*\) for every \(x\).  Equivalently, its arcs are a perfect
matching between source and target copies of \(X\).  It is a **Hamilton
successor factor** if \(h\) has one cycle.  Deleting \(\partial\) then gives
one directed Hamilton path on the 6435 middle owners.

For a Hamilton factor \(h\), linearized at \(\partial\), define:

* \(R(h)\): the number of selected forbidden residence paths of two to
  four normal arcs;
* \(U(h)\): the number of missing upper targets over depths \(1\le q\le7\),
  with no window allowed to cross \(\partial\);
* \(G_h\): the exact lower physical-cell compiler graph, including its
  oriented boundary palettes;
* \(D(h)=16383-\nu(G_h)\): its matching deficiency.

The upper target count is
\[
 \sum_{q=1}^7\binom{15}{8+q}
 =5005+3003+1365+455+105+15+1
 =9949.
 \tag{2.3}
\]
Thus \(U(h)=0\) is a finite literal condition.  Hall's theorem gives the
exact dual identity
\[
 D(h)=max_{A\subseteq\mathcal L}
       \bigl(|A|-|N_h(A)|\bigr).
 \tag{2.4}
\]
In particular, positivity of seven targets is only a necessary pointwise
condition; it does not control the maximum in (2.4).

When Theorem 5.1 is applied to a law which also contains non-Hamilton
successor factors, extend \(R,U,D\) to those outcomes by the value zero (or
by any other nonnegative convention).  Their circuit-defect term is already
positive, so this harmless extension cannot create a zero-defect invalid
outcome.

## 3. Exact two-parent overlay and the global circuit invariant

Let \(f,g\) be two augmented parent cycles on \(X\), and put
\[
    \rho=f^{-1}g.
    \tag{3.1}
\]
Write the nontrivial cycles of \(\rho\) as
\(O_1,\ldots,O_c\), with \(|O_j|=\ell_j\).

### Theorem 3.1 (two-parent shore normal form)

Every successor factor supported on the two-parent union
\(E(f)\cup E(g)\) is uniquely
\[
    h_I=f\rho_I,
    \qquad I\subseteq[c],
    \tag{3.2}
\]
where \(\rho_I\) equals \(\rho\) on \(O_j\) for \(j\in I\) and is the
identity on every unselected component.  Moreover
\[
 \operatorname{sgn}(h_I)
 =(-1)^{n-1+\sum_{j\in I}(\ell_j-1)}.
 \tag{3.3}
\]
Hence a necessary condition for \(h_I\) to be Hamilton is
\[
 \boxed{
   \sum_{j\in I}(\ell_j-1)\equiv0\pmod2.}
 \tag{3.4}
\]
Equivalently, an even number of selected even-length relative components
is required.

#### Proof

Starting at a source \(x\), traverse its \(g\)-edge and then the reverse
of the incident \(f\)-edge.  The next source is
\(f^{-1}g(x)=\rho(x)\).  Thus a nontrivial \(\rho\)-cycle of length
\(\ell_j\) is exactly one alternating bipartite cycle of length
\(2\ell_j\).  An even cycle has exactly two perfect matchings, its full
\(f\)-shore and its full \(g\)-shore.  Choices on distinct components are
independent at the degree-one level.  Since \(g=f\rho\), choosing the
\(g\)-shore precisely on \(I\) gives (3.2).

The sign of an \(\ell_j\)-cycle is \((-1)^{\ell_j-1}\), while \(f\) is an
\(n\)-cycle and has sign \((-1)^{n-1}\).  This proves (3.3).  Every
\(n\)-cycle has sign \((-1)^{n-1}\), giving (3.4). \(\square\)

For a coordinate transposition \(\tau\), one has
\[
   g=\tau f\tau,
   \qquad \rho=f^{-1}\tau f\tau.
   \tag{3.5}
\]
The special dihedral symmetry of (3.5) does not remove (3.4): it pairs or
reflects relative cycles, but arbitrary shore choices are still only
perfect matchings, not necessarily Hamilton cycles.

### Theorem 3.2 (maximum-genus circuit formula)

For \(I\subseteq[c]\), set
\[
   s(I)=\sum_{j\in I}(\ell_j-1)
       =n-c(\rho_I).
   \tag{3.6}
\]
There is a nonnegative integer \(g(I)\) such that
\[
   \boxed{c(h_I)=1+s(I)-2g(I),}
   \tag{3.7}
\]
where \(c(\pi)\) denotes the number of cycles of a permutation \(\pi\).
Consequently
\[
 h_I\text{ is Hamilton}
 \quad\Longleftrightarrow\quad
 s(I)\text{ is even and }g(I)=s(I)/2.
 \tag{3.8}
\]

#### Proof

The permutations \(f\) and \(\rho_I\) define an orientable permutation
map on \(n\) darts.  It has one black vertex, one white vertex for every
cycle of \(\rho_I\), \(n\) edges, and one face for every cycle of
\(f\rho_I=h_I\).  The map is connected because the black rotation \(f\)
is transitive.  Euler's formula therefore gives
\[
  2-2g(I)
  =1+c(\rho_I)-n+c(h_I).
\]
Substituting \(c(\rho_I)=n-s(I)\) yields (3.7).  Since \(c(h_I)\ge1\),
one has \(g(I)\le s(I)/2\), with equality exactly when
\(c(h_I)=1\). \(\square\)

Thus parity is only the first shadow of the obstruction.  A valid mixed
chronology must make all selected component surgeries attain maximum genus.

### Corollary 3.3 (relative two-cycles and interlacement)

Suppose every selected nontrivial component in \(I\) is a two-cycle
\((a_jb_j)\).  Draw the chord \(a_jb_j\) in the cyclic \(f\)-order, and
let \(A_I\) be the symmetric zero-diagonal matrix over \(\mathbf F_2\)
whose \((i,j)\) entry is one exactly when the two chords interlace.  Then
\[
    c(h_I)=1+\operatorname{nullity}_{\mathbf F_2}(A_I).
    \tag{3.9}
\]
In particular, the switch is Hamilton exactly when \(A_I\) is nonsingular.

#### Proof

Start with a disk whose boundary order is \(f\), and attach one band along
the two ends of every selected chord.  The boundary components of the
resulting orientable surface are the cycles of
\(f\prod_{j\in I}(a_jb_j)\).  On the band-core basis, the mod-two
intersection form is exactly \(A_I\), so
\(\operatorname{rank}A_I=2g(I)\).  With \(|I|=s(I)\), (3.7) becomes
\[
 c(h_I)=1+|I|-\operatorname{rank}A_I,
\]
which is (3.9). \(\square\)

One relative two-cycle always splits a Hamilton circuit into two circuits.
Two repair it precisely when their chords interlace.  This is the minimal
example of why independent local component flips are the wrong actions;
Hamilton-preserving packets must generally couple several components.

## 4. Exact forced-component and invariant-set cuts

Suppose motif, degree, or residence propagation forces components in
\(I_+\) to the \(g\)-shore and components in \(I_-\) to the \(f\)-shore.
Let \(F\) be the still-free components and put
\[
   h_0=f\rho_{I_+}.
   \tag{4.1}
\]
Let \(Q_1,\ldots,Q_b\) be the successor cycles of \(h_0\).  Form a
hypergraph \(\mathcal K\) on \([b]\) by giving each free component
\(O_j\), \(j\in F\), the hyperedge
\[
  e_j=\{a:O_j\cap Q_a\ne\varnothing\}.
  \tag{4.2}
\]

### Proposition 4.1 (forced-state component cut)

If \(\mathcal K\) is disconnected, no completion of the free shore bits is
Hamilton.

#### Proof

Let \(K\) be a nonempty proper connected component of \(\mathcal K\), and
put \(S=\bigcup_{a\in K}Q_a\).  The permutation \(h_0\) preserves \(S\).
Every free support \(O_j\) lies wholly in \(S\) or wholly outside \(S\):
otherwise its hyperedge would connect \(K\) to its complement.  Hence every
\(\rho_j\), and therefore every product of free \(\rho_j\)'s, preserves
\(S\).  All completions \(h_0\rho_J\) preserve the same nontrivial set
\(S\), so none is one cycle. \(\square\)

Two weaker scalar prefilters follow immediately.  If \(c_0=c(h_0)\), then
every completion obeys
\[
 c(h_0\rho_J)
 \ge c_0-\sum_{j\in J}(\ell_j-1),
 \tag{4.3}
\]
because an \(\ell_j\)-cycle is a product of \(\ell_j-1\) transpositions
and one transposition can merge at most two successor cycles.  Thus
\[
  c_0-1>\sum_{j\in F}(\ell_j-1)
  \tag{4.4}
\]
is an immediate no-go.  The sign equation also requires
\[
 \sum_{j\in J}(\ell_j-1)\equiv c_0-1\pmod2.
 \tag{4.5}
\]

There is an exact sign cut for the full five-parent catalogue as well.  Let
\(B\) be any residual bipartite successor graph after forced arcs and
forbidden arcs have been propagated.  Order its rows and columns using a
fixed Hamilton reference parent, and let \(P_+\) and \(P_-\) be the numbers
of its perfect matchings of the two relative signs.  Then
\[
   \operatorname{per}B=P_++P_-,
   \qquad \det B=P_+-P_-.
   \tag{4.5a}
\]
Thus, if \(|\det B|=\operatorname{per}B\) and the surviving sign is opposite
to the sign \((-1)^{n-1}\) of an \(n\)-cycle, degree-one feasibility holds
only on the wrong sign and Hamilton completion is impossible.  This is only
a necessary sign audit; passing it does not remove the subtour or
maximum-genus obstruction.

These cuts apply directly after choosing zero-target motifs.  Indeed, an
interior parent-pure motif for an old \(P\)-zero target in \(\tau P\) must
contain a \(\tau P\)-exclusive successor arc.  If every arc of its local
word were common with \(P\), functionality would put the identical
consecutive word, hence the identical physical cell, in \(P\), contrary to
the zero count.  Such a motif therefore forces at least one nonbase overlay
shore.  Boundary motifs require the analogous endpoint-flag statement and
are not silently included in this interior argument.

### Proposition 4.2 (exact invariant-set circuit defect)

Fix a root \(r\in X\).  For every successor permutation \(h\),
\[
  \boxed{
  2^{c(h)-1}-1
  =\sum_{\varnothing\ne S\subseteq X\setminus\{r\}}
       \mathbf 1_{\{h(S)=S\}}.}
  \tag{4.6}
\]

#### Proof

An invariant set of a permutation is exactly a union of its cycles.  Among
the \(c(h)\) cycles, the cycle containing \(r\) cannot be used because
\(S\subseteq X\setminus\{r\}\).  Every nonempty union of the other
\(c(h)-1\) cycles is permitted, giving \(2^{c(h)-1}-1\) sets. \(\square\)

For the fair two-parent component law, call a shore of component \(O_j\)
**\(S\)-preserving** when all its arcs respect membership in \(S\).  If
some component has no preserving shore, then
\(\Pr(h_I(S)=S)=0\).  Otherwise, if \(u(S)\) components have exactly one
preserving shore, then
\[
    \Pr(h_I(S)=S)=2^{-u(S)}.
    \tag{4.7}
\]
For biased independent bits with \(\Pr(j\in I)=p_j\), the exact formula is
\[
 \Pr(h_I(S)=S)
 =\prod_{\substack{j:\text{only the }g\text{-shore}\\\text{preserves }S}}p_j
  \prod_{\substack{j:\text{only the }f\text{-shore}\\\text{preserves }S}}(1-p_j),
 \tag{4.8}
\]
again with value zero if a component has neither shore.

Taking expectations in (4.6) gives the exact global identity
\[
 \sum_{\varnothing\ne S\subseteq X\setminus\{r\}}
      \Pr(h_I(S)=S)
 =\mathbb E\bigl[2^{c(h_I)-1}-1\bigr].
 \tag{4.9}
\]
For example, the sufficient component-cut expansion estimate
\[
 u(S)\ge
 \log_2\binom{n-1}{|S|}+2\log_2 n
 \tag{4.10}
\]
for every feasible \(S\) would make the left side of (4.9) less than
\(1/n\).  The coordinate-parent screen contains no estimate resembling
(4.10).

## 5. An exact randomized and deterministic whole-selection theorem

For an arbitrary probability law on degree-one successor factors, define
the nonnegative integer
\[
 \Phi(h)=
   \bigl(2^{c(h)-1}-1\bigr)+R(h)+U(h)+D(h).
 \tag{5.1}
\]

### Theorem 5.1 (global defect rounding)

If
\[
    \mathbb E\Phi(h)<1,
    \tag{5.2}
\]
then the law's support contains a successor factor \(h\) such that
\[
    c(h)=1,qquad R(h)=0,qquad U(h)=0,qquad D(h)=0.
    \tag{5.3}
\]
If the law is generated by finitely many random choices and the relevant
conditional expectations can be evaluated, the choices can be fixed
deterministically while preserving (5.2).

#### Proof

The four summands in (5.1) are nonnegative integers.  If every outcome had
\(\Phi(h)\ge1\), its expectation would be at least one.  Hence some outcome
has \(\Phi(h)=0\), which is exactly (5.3).

For the deterministic statement, expose the random choices successively.
At each step, at least one value has conditional expectation no larger than
the current conditional expectation.  Choose such a value.  At the end,
the realized integer \(\Phi\) is strictly below one and is therefore zero.
\(\square\)

For two parents, (4.7)--(4.9) make the first summand completely explicit.
For more than two parents, Theorem 5.1 remains valid under any law on
perfect successor matchings, but constructing and analysing such a law is a
separate step.  In particular, the exact fractional point of the parent
matching polytope does not by itself control \(D(h)\) or the circuit term.

Theorem 5.1 is an honest first-moment target, not a claim that (5.2) holds
for the present catalogue.  Its value is that it identifies the missing
global quantity exactly.  A calculation involving only bounded residence
events and seven target occurrences is incomplete unless it also controls
\(\mathbb E[2^{c-1}-1]\), all upper holes, and the maximum Hall deficiency
(2.4).

## 6. Why the raw component-bit LLL is invalid

The following four-state example already occurs in the coordinate-
transposition conjugacy class.  Let
\[
   f=(1\ 2\ 3\ 4),
   \qquad \tau=(2\ 4),
   \qquad g=\tau f\tau=(1\ 4\ 3\ 2).
   \tag{6.1}
\]
Then
\[
    \rho=f^{-1}g=(1\ 3)(2\ 4).
    \tag{6.2}
\]
There are two disjoint overlay bits \(x_1,x_2\).  The mixed choice
\((x_1,x_2)=(1,0)\) gives
\[
    f(1\ 3)=(1\ 4)(2\ 3),
    \tag{6.3}
\]
a disconnected cycle cover.

Now impose the two local bad events
\[
    B_1=\{x_1=0\},
    \qquad B_2=\{x_2=1\}.
    \tag{6.4}
\]
They depend on disjoint variables.  Bias the bits so that
\(\Pr(B_1)=\Pr(B_2)=\varepsilon\).  Their probabilities are arbitrarily
small and an ordinary variable LLL avoids both, but the unique assignment
avoiding them is (6.3), which is not Hamilton.

Thus no LLL whose event family consists only of local degree, motif,
residence, upper, or cell events can infer one circuit from independent
overlay bits.  One must do one of the following:

1. include every invariant-set cylinder in (4.6), together with its true
   global bit dependencies;
2. prove a global cut-expansion estimate such as (4.10); or
3. move the random process to a state space in which Hamiltonicity is
   preserved by every action.

The last alternative is the viable entropy-compression formulation for the
current k15 lane.

## 7. Hamilton-state entropy compression

We first give the abstract theorem.  It makes no independence assumption
about parent labels or alternating components.

Let
\[
   \mathcal Q_0,\mathcal Q_1,\ldots,\mathcal Q_D
   \tag{7.1}
\]
be finite configuration levels, with \(\mathcal Q_D\) terminal.  Every
nonterminal configuration has exactly \(R\) labelled trials.  A resolved
trial has a record symbol \(\beta\), changes the level by an integer
\(d_\beta\le1\), and has **backward congestion** \(c_\beta\): for every
post-state \(q'\) and symbol \(\beta\), at most \(c_\beta\)
predecessor-state/trial pairs resolve to \((q',\beta)\).  Transitions which
would leave \([0,D]\) are not allowed.

Put
\[
    F(x)=\sum_\beta c_\beta x^{d_\beta},
    \qquad x>0.
    \tag{7.2}
\]

### Theorem 7.1 (finite-state rollback entropy compression)

If
\[
    R>\inf_{x>0}F(x),
    \tag{7.3}
\]
then a terminal configuration is reachable from every specified initial
configuration to which the trial system applies.

More precisely, fix \(x>0\) with \(F(x)<R\), let the initial level be
\(h_0\), and set
\[
   C(x)=\sum_{h=0}^{D-1}|\mathcal Q_h|x^{h_0-h}.
   \tag{7.4}
\]
For independent uniform trial labels, the probability of making \(N\)
resolved nonterminal steps without reaching \(\mathcal Q_D\) is at most
\[
    C(x)\left(\frac{F(x)}R\right)^N.
    \tag{7.5}
\]
Consequently a deterministic successful trial word exists.  It suffices to
take
\[
 N>\frac{\log C(x)}{\log(R/F(x))}
 \tag{7.6}
\]
when \(C(x)>1\).

#### Proof

Consider a length-\(N\) trial-label word whose trajectory has not yet
reached level \(D\).  Record only the resolution symbols
\(\beta_1,\ldots,\beta_N\) and the final configuration.  Reading backward,
the congestion definition gives at most
\[
    \prod_{t=1}^N c_{\beta_t}
    \tag{7.7}
\]
predecessor/trial histories with that final state and record.

If the final level is \(h\), then
\[
   \sum_{t=1}^N d_{\beta_t}=h-h_0.
\]
The total reverse multiplicity of all formal records with that increment is
the coefficient of \(z^{h-h_0}\) in the Laurent polynomial
\[
   \left(\sum_\beta c_\beta z^{d_\beta}\right)^N.
\]
All coefficients are nonnegative, so evaluation at \(z=x>0\) bounds this
coefficient by
\[
   F(x)^N x^{h_0-h}.
   \tag{7.8}
\]
Summing (7.8) over all nonterminal final configurations gives at most
\(C(x)F(x)^N\) failing trial words.  There are \(R^N\) input words, proving
(7.5).  Since its right side tends to zero, a terminal-reaching word exists,
and (7.6) is the displayed finite bound. \(\square\)

A convenient specialization has success types
\(\alpha\in\mathfrak S\), each of increment \(+1\), and failure types
\(\beta\in\mathfrak B_\ell\) of rollback length \(\ell\), hence increment
\(1-\ell\).  Put
\[
    A_+=\sum_{\alpha\in\mathfrak S}c_\alpha,
    \qquad
    A_\ell=\sum_{\beta\in\mathfrak B_\ell}c_\beta.
    \tag{7.9}
\]
Then
\[
    F(x)=A_+x+\sum_{\ell\ge1}A_\ell x^{1-\ell}.
    \tag{7.10}
\]
The coefficient is \(A_+=1\) only when the combined map
\((\text{prestate},\text{success trial})\mapsto\text{poststate}\) is
globally injective after recording the single common success symbol.  Merely
recovering the predecessor after also revealing one of several finite
success types gives the displayed sum \(A_+\), not one.

If only rollback lengths one and two occur, the threshold is exactly
\[
    \boxed{R>A_1+2\sqrt{A_+A_2}.}
    \tag{7.11}
\]

### The k15 augmented levels

For \(0\le h\le29\), a state in \(\mathcal Q_h\) consists of:

1. a successor factor \(C\) supported on the five-parent arc union (2.1),
   already certified to be one cycle on \(X\);
2. its linearization at \(\partial\), already certified to contain no
   forbidden residence path of two to four normal arcs;
3. one literal, non-wrapping witness window for each of the 9949 upper
   targets in (2.3);
4. an exact matching \(M\) in the full physical compiler graph \(G_C\) of
   size
   \[
      |M|=16354+h;
      \tag{7.12}
   \]
5. the finite checkpoint/type data needed to make the claimed reverse
   congestion bounds literal.

The Hall-29 parent and any maximum matching in its compiler graph give a
state in \(\mathcal Q_0\).  A state in \(\mathcal Q_{29}\) carries a matching
of size
\[
    16354+29=16383=|\mathcal L|,
    \tag{7.13}
\]
so it has exact compiler Hall while retaining one Hamilton chronology,
residence, and all upper shadows.

Crucially, a trial is not one independent overlay bit.  It is a correlated
bundle of alternating successor components whose output has already passed
the one-cycle, residence, and upper-witness requirements.  Thus every
intermediate state remains globally legal; Hamiltonicity is never inferred
from a bounded dependency graph.

### Lemma 7.2 (exact matching-gain certificate)

Let \((C,M)\in\mathcal Q_h\), and let \(Q\) be another globally certified
Hamilton/residence/upper chronology in the same parent union.  Put
\[
    M_0=M\cap E(G_Q),
    \qquad r=|M\setminus M_0|.
    \tag{7.14}
\]
If \(G_Q\) contains \(r+1\) pairwise vertex-disjoint
\(M_0\)-augmenting paths, then \(Q\) supports a matching of size
\(|M|+1\).

#### Proof

The retained matching has size \(|M_0|=|M|-r\).  Symmetric-difference
flips on pairwise vertex-disjoint augmenting paths commute and each increase
matching size by one.  Flipping all \(r+1\) paths therefore gives size
\[
    |M|-r+(r+1)=|M|+1.
\]
\(\square\)

If the resulting matching is larger, discard arbitrary matched edges to
place the state at the required exact level.

### Lemma 7.3 (cell damage from changed successor arcs)

Suppose two linear chronologies differ in \(s\) normal successor arcs.  At
most
\[
    30s+36
    \tag{7.15}
\]
named compiler-cell shores can change.  Consequently the quantity \(r\) in
(7.14) obeys
\[
    r\le30s+36.
    \tag{7.16}
\]

#### Proof

An unchanged interior cell is determined by its complete consecutive word.
The three interior word lengths are 10, 11, and 12 vertices.  A fixed
changed arc occurs in at most 9, 10, and 11 windows of those respective
lengths.  Hence at most
\[
   (9+10+11)s=30s
\]
interior cell occurrences can change.  There are 36 oriented endpoint
cells, all of which are included in the safe worst case.  This proves
(7.15).  Every destroyed edge of a matching uses a distinct destroyed cell,
giving (7.16). \(\square\)

Similarly, an upper witness whose at-most-seven-arc support avoids the
changed-arc collar survives literally.  Lemma 7.3 is only a damage bound:
it does not supply the \(r+1\) augmenting paths, replacement upper witnesses,
or a low-congestion reverse encoding.

### `CAA_29` (causal augmentation atlas; unproved)

For every reachable nonterminal state in the levels above, construct \(R\)
labelled trials such that:

1. every resolved output is again a globally certified one-cycle,
   residence-safe, upper-complete state in the same five-parent union;
2. a successful trial has the certificate of Lemma 7.2 and raises the
   matching level by one; every success type \(\alpha\) has a proved reverse
   congestion \(c_\alpha\);
3. every failure is assigned a rollback length \(\ell\) and a finite type
   \(\beta\), with a proved backward congestion \(c_\beta\);
4. the exact inequality
   \[
      R>\inf_{x>0}
      \left(A_+x+\sum_{\ell\ge1}A_\ell x^{1-\ell}\right)
      \tag{7.17}
\]
   holds, where
   \(A_+=\sum_{\alpha\in\mathfrak S}c_\alpha\) and
   \(A_\ell=\sum_{\beta\in\mathfrak B_\ell}c_\beta\).

Theorem 7.1 and (7.13) prove a full k15 carrier immediately from
`CAA_29`.  The exact sandwich/compiler theorem would then turn that carrier
into the required literal word, subject to the final independent verifier.

The winner vector in (1.2) has three entries equal to one.  Therefore a
target-by-target scheme whose trial labels are only the parent-pure motif
occurrences in \((1,12)P\) has \(R\le1\) at those stages.  That particular
scheme cannot satisfy even the rollback-one specialization \(R>A_1\) if
any nonzero reversible failure type is present.  This does not bound a
correlated packet family which keeps the same local motif and varies remote
Hamilton-preserving components.  It does prove that the parent-cover count,
by itself, cannot be inserted directly into the entropy argument.  One must
use additional parents or prove multiplicity for correlated globally legal
packets.

## 8. Final audit and shortest viable route

The following implications are now exact.

1. **Pure-parent geometry.**  Every relabel parent is separately Hamilton,
   residence-safe, and upper-complete.
2. **Pure-parent Hall.**  Every relabel parent is nevertheless exactly
   Hall-29 by Lemma 1.1.
3. **Old-zero supply.**  Exactly the four transpositions in (1.2) supply
   every old zero.  This forces some nonbase shores when those interior
   motifs are selected, but supplies neither compatible cells nor a circuit.
4. **Degree-one selection.**  Alternating-component shore choices preserve
   a perfect successor matching.  They do not preserve one circuit.
5. **Circuit audit.**  Parity (3.4), maximum genus (3.8), and the forced
   hypergraph cut of Proposition 4.1 are exact necessary tests.  For
   two-cycle components, nonsingularity in (3.9) is exact.
6. **Residence and upper audit.**  These must be checked on the mixed
   chronology.  Parentwise safety does not survive an arbitrary mixture.
7. **Compiler audit.**  The required condition is the full matching
   \(16383/16383\), equivalently every cut in (2.4), not positivity of the
   seven old targets or slack on three frozen DM families.
8. **Entropy compression.**  Theorem 7.1 is global-dependence safe because
   all states and all resolved actions are Hamilton before they enter the
   count.  The only unproved part is the action atlas and its quantitative
   reverse congestion.

The shortest viable proof route is therefore:

\[
\boxed{
\begin{array}{c}
\text{retain all four zero-clearing relabel parents}\\
\Downarrow\\
\text{select motif packets and propagate forced component shores}\\
\Downarrow\\
\text{reject parity/genus/forced-hypergraph failures}\\
\Downarrow\\
\text{bundle the surviving components into globally Hamilton actions}\\
\Downarrow\\
\text{carry residence, all 9949 upper witnesses, and the exact matching}\\
\Downarrow\\
\text{prove `CAA_29` and apply Theorem 7.1.}
\end{array}}
\tag{8.1}
\]

The present lane has thus produced a rigorous Hamilton-aware rounding
theorem and two exact obstruction families.  It has not produced the
required k15 action atlas.  That atlas, not another pointwise parent screen
and not a raw independent-component LLL, is the minimal remaining lemma for
this route.
