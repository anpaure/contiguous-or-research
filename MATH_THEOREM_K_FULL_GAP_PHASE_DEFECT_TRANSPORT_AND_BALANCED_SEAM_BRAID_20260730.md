# Full-gap phase-defect transport and balanced seam braids

Date: 2026-07-30  
Lane: K  
Status: **proved the exact phase/rethread transport ledger, two fixed-length
defect invariants, the full-gap decomposition theorem, a literal three-cut
gap-opening braid, an exact compatible-witness section, and an
expansion-based alternating-port completion theorem.  These explain the K16
one-hole shuttles and give a sufficient path-to-reserve construction.  The
remaining all-\(k\) statement is one precise gap-crossing reserve conjecture.**

## 0. Result and exact boundary

The finite K16 facts now have one common interpretation.

1. The verified word of length 12,875 is the old partial followed by
   \(0x0200,0x287d\).  Deleting the last cell gives the one-hole word

       scratch/k16_append0200_12874_onehole.word

   whose hole is \(0x287d\).
2. Its minimum one-cell moves form a \(16\)-by-\(16\) shuttle.  They transport
   the hole

   \[
        0x287d\longleftrightarrow0xa879                 \tag{0.1}
   \]

   without reaching a complete word.
3. Replacing arbitrary values in the six cells

   \[
      [0,2)\cup[6439,6442)\cup[12873,12874)            \tag{0.2}
   \]

   is infeasible in the exact finite model.  The widened ten-cell collar

   \[
      [0,3)\cup[6438,6443)\cup[12872,12874)            \tag{0.3}
   \]

   is also exactly infeasible.  In both cases the two intervening fixed gaps
   have OR equal to \(0xffff\).
4. A global state of the same length, obtained from the verified word by
   deleting position 6435 and then coherently changing 78 cells, has the sole
   hole \(0x4e63\).  Its changes lie outside (0.2), and 77 of 78 lie outside
   (0.3).  Thus it crosses the full-gap barrier.  It still has one hole: its
   exact one-cell floor transports the debt back to \(0x287d\).

The structural conclusion is:

> A collar-local phase cycle cannot close the K16 debt.  Any successful move
> must alter a full-OR separator or rethread blocks across it, thereby
> creating a projected occurrence which no isolated collar can see.

The positive move family below is the three-cut gap-opening braid.  Its
remaining gate is not scalar phase balance: its new seams must route the
missing row to an occurrence row with genuine multiplicity reserve, while
the complete lower/upper shadow and compiler ledgers circulate.

Throughout, a word is a finite sequence of nonempty coordinate masks and an
interval is nonempty.

## 1. Phase-resolved occurrence loads

Let the coordinate set be \(\Omega=X\sqcup\{z\}\).  Write a nonzero word as

\[
 W_i=B_i\cup\bigl(\{z\}\text{ if }\epsilon_i=1\bigr),
 \qquad B_i\subseteq X,\quad\epsilon_i\in\{0,1\}.      \tag{1.1}
\]

For an interval \(I=[a,b]\), put

\[
 b(I)=\bigcup_{i=a}^b B_i,\qquad
 e(I)=\bigvee_{i=a}^b\epsilon_i.                      \tag{1.2}
\]

For \(S\subseteq X\), define

\[
 \lambda_0(S)=\#\{I:b(I)=S,\ e(I)=0\},\qquad
 \lambda_1(S)=\#\{I:b(I)=S,\ e(I)=1\}.                \tag{1.3}
\]

Thus \(\lambda_0(S)\) counts witnesses of \(S\), while \(\lambda_1(S)\)
counts witnesses of \(S+z\).  Their projected total is

\[
 \nu(S)=\lambda_0(S)+\lambda_1(S).                    \tag{1.4}
\]

Define the projected two-shore deficit

\[
 \Phi_z(W)=\sum_{\varnothing\ne S\subseteq X}
                  (2-\nu(S))^+.                       \tag{1.5}
\]

### Proposition 1.1 (pure-phase invariant)

Changing only the phase bits \(\epsilon_i\), with the projected payload
\((B_i)\) and its order fixed, preserves every \(\nu(S)\) and hence
\(\Phi_z(W)\).

If \(\nu(S)=1\), phase alone can only exchange which of \(S,S+z\) is
missing; it cannot cover both.

#### Proof

The projected interval family \(b(I)=S\) is unchanged.  Phase merely
partitions that fixed family into inactive and active intervals, proving the
claim.  \(\square\)

The exact K16 values are

\[
\begin{array}{c|c|c}
\text{word}&\Phi_z&\text{unique deficient projection}\\ \hline
\text{append-}0200&1&0x287d\\
\text{global five-phase}&1&0x4e63\\
\text{verified }12875&0&\text{none}.
\end{array}                                             \tag{1.6}
\]

Thus the global separator-crossing edit transports the sole projected
defect; the final extra cell in the verified word actually removes it.

### Proposition 1.2 (append-chain lower bound)

Fix a projected prefix \(B\) and append \(r\) projected cells.  Assign every
new interval to its rightmost appended endpoint.  For each fixed endpoint,
the resulting interval-OR labels form an inclusion chain as the left endpoint
moves left.  Consequently, if a family \(\mathcal D\) of projections all
have old load one and must each acquire a second projected occurrence, then

\[
 r\ge \operatorname{width}(\mathcal D,\subseteq).     \tag{1.7}
\]

#### Proof

For one right endpoint, moving the left endpoint left can only add
coordinates to the interval OR.  The projections serviced at that endpoint
therefore lie in one chain.  The \(r\) endpoints cover \(\mathcal D\) by at
most \(r\) chains, so every antichain has size at most \(r\).  \(\square\)

For the authenticated length-12,873 prefix, the projected unit-load deficit
family is exactly

\[
 \{0x287d,0x4e61,0x4e63\},
 \qquad 0x4e61\subset0x4e63,                          \tag{1.8}
\]

while \(0x287d\) is incomparable with the other two.  Hence one append is
impossible by (1.7).  The cell \(0x0200\) repairs the nested pair and the
cell \(0x287d\) repairs the remaining incomparable projection.  This is the
projected-capacity explanation of the verified append-two construction; the
physical phase audit supplies sufficiency.

## 2. Exact deletion and rethread ledger

Cut \(W\) into pairwise-disjoint retained contiguous fragments whose union
is the retained cell set.  Reverse chosen fragments if desired, and
concatenate every fragment exactly once in a new order to obtain \(W'\).
For a physical target \(T\subseteq\Omega\), let:

* \(D_T\) be the number of old \(T\)-witness intervals not wholly contained
  in one retained fragment;
* \(A_T\) be the number of final \(T\)-witness intervals crossing at least
  one new seam.

### Theorem 2.1 (exact rethread transport)

For every physical target \(T\),

\[
 \boxed{\lambda_{W'}(T)=\lambda_W(T)-D_T+A_T.}         \tag{2.1}
\]

Resolving by projection and phase gives

\[
 \lambda'_b(S)=\lambda_b(S)-D_b(S)+A_b(S),\qquad b=0,1, \tag{2.2}
\]

and

\[
 \nu'(S)-\nu(S)=
 A_0(S)+A_1(S)-D_0(S)-D_1(S).                         \tag{2.3}
\]

#### Proof

Every final interval either lies in one retained fragment or crosses a new
seam.  Internal intervals are in bijection with old internal intervals;
reversal preserves their union.  These contribute \(\lambda-D\).  Every
remaining final interval is counted once by \(A\), even if it crosses
several seams.  This proves (2.1), and phase resolution proves
(2.2)--(2.3).  \(\square\)

For deletion of one interior cell \(W_p\), \(D_T\) counts old
\(T\)-intervals containing \(p\), while \(A_T\) counts new intervals formed
from a left suffix and a right prefix across the deletion seam.

For a substitution \(x=W_p\mapsto y\), let \(\mathcal C_p\) be the multiset
of context ORs

\[
 c=\bigvee_{i=a}^{p-1}W_i\ \vee\
   \bigvee_{i=p+1}^{b}W_i                              \tag{2.4}
\]

over all \(a\le p\le b\).  If \(m_p(c)\) is the context multiplicity, then

\[
 \boxed{
 \lambda'(T)-\lambda(T)
 =\sum_c m_p(c)
   \bigl(1[c\vee y=T]-1[c\vee x=T]\bigr).}            \tag{2.5}
\]

This is the complete one-site portal law.

For a binary coordinate trace \(\chi_x(i)=1[x\in W_i]\), let

\[
 \partial_x(W)=\sum_i1[\chi_x(i)\ne\chi_x(i+1)]       \tag{2.6}
\]

with the declared linear or cyclic boundary convention.  If a rethread
keeps every fragment orientation, then

\[
 \boxed{
 \partial_x(W')-\partial_x(W)
 =\sum_{(R,L)\in J_{\rm new}}1[\chi_x(R)\ne\chi_x(L)]
  -\sum_{(R,L)\in J_{\rm old}}1[\chi_x(R)\ne\chi_x(L)].} \tag{2.7}
\]

Here \(R,L\) are the terminal and initial cells at a seam.  With reversed
fragments one uses their new oriented endpoints; internal run lengths are
unchanged.  Formula (2.7) is the exact phase-boundary ledger when \(x=z\),
and the exact coordinate-boundary ledger otherwise.  Minimum-run conditions
are therefore finite collar tests once the seam set is fixed.

### Proposition 2.2 (OR-convolution boundary monoid)

Work in the integral algebra with basis \([S]\), \(S\subseteq\Omega\), and
product \([S]*[T]=[S\cup T]\).  For a word \(U\), let \(C(U)\), \(P(U)\),
and \(Q(U)\) be respectively the multisets of interval-, prefix-, and
suffix-ORs, and let \(u(U)=\bigvee U\).  Then

\[
\begin{aligned}
 C(UV)&=C(U)+C(V)+Q(U)*P(V),\\
 P(UV)&=P(U)+[u(U)]*P(V),\\
 Q(UV)&=Q(V)+Q(U)*[u(V)].                            \tag{2.8}
\end{aligned}
\]

Consequently, replacing the middle block in \(A|X|B\) by \(Y\) has exact
interval drift

\[
\begin{aligned}
 \Delta C={}&\Delta C_X+Q(A)*\Delta P+\Delta Q*P(B)\\
 &+Q(A)*\bigl([u(Y)]-[u(X)]\bigr)*P(B).              \tag{2.9}
\end{aligned}
\]

In particular the last, genuinely nonlocal term vanishes when the replaced
block keeps its total OR.  These identities follow by partitioning an
interval according to whether it lies in one factor or crosses the join.

### Proposition 2.3 (exact run-energy scalarization)

For \(T\subseteq\Omega\), put

\[
 F_T(W)=\sum_{S\subseteq T}\lambda_W(S).             \tag{2.10}
\]

A position is \(T\)-compatible when \(W_i\subseteq T\).  If the maximal
compatible runs have lengths \(\ell_1,\ldots,\ell_j\), then

\[
 \boxed{F_T(W)=\sum_{a=1}^j\binom{\ell_a+1}{2}.}     \tag{2.11}
\]

Moreover

\[
 \lambda_W(S)=\sum_{T\subseteq S}(-1)^{|S|-|T|}F_T(W), \tag{2.12}
\]

and, if \(R_T(U)\), \(L_T(V)\) are the lengths of the compatible suffix and
prefix,

\[
 F_T(UV)=F_T(U)+F_T(V)+R_T(U)L_T(V).                 \tag{2.13}
\]

#### Proof

An interval has OR contained in \(T\) exactly when every one of its cells is
\(T\)-compatible, giving (2.11).  Equation (2.12) is Boolean-lattice
Möbius inversion.  The crossing compatible intervals at a join are exactly
the \(R_T(U)L_T(V)\) suffix-prefix pairs, giving (2.13).  \(\square\)

Thus arbitrary long-window transport is still an exact seam product; it is
not controlled by bounded halo disjointness alone.

## 3. Fixed-length occurrence reserve

Assume, as in the contiguous-OR problem, that every word cell is nonempty.
In this section \(\lambda_W\) counts ordinary nonempty linear intervals,
not cyclic wraparound intervals.  Let \(K=2^{|\Omega|}-1\), \(N=|W|\), and

\[
 M=\binom{N+1}{2}.                                    \tag{3.1}
\]

Let

\[
 H(W)=\#\{\varnothing\ne T\subseteq\Omega:\lambda_W(T)=0\},\qquad
 E(W)=\sum_{\substack{\varnothing\ne T\subseteq\Omega\\
                       \lambda_W(T)>0}}(\lambda_W(T)-1). \tag{3.2}
\]

### Theorem 3.1 (defect--reserve invariant)

Every word of length \(N\) satisfies

\[
 \boxed{E(W)-H(W)=M-K.}                               \tag{3.3}
\]

Consequently, reducing the hole count by \(j\) at fixed length necessarily
spends exactly \(j\) units of excess occurrence reserve.

#### Proof

There are \(K-H(W)\) covered targets, so

\[
 E(W)=\sum_T\lambda_W(T)-(K-H(W))=M-K+H(W).           \tag{3.4}
\]

This is (3.3).  \(\square\)

A move which fills one unit-load hole and removes the last occurrence of
another target keeps \(H\) and \(E\) unchanged: it only moves the debt.  A
successful move must instead remove an occurrence from a target of load at
least two.

### Lemma 3.2 (path to reserve)

Let \(h_0\) be one hole of the initial load vector.  Suppose compatible moves
\(a_1,\ldots,a_t\), evaluated in their one literal simultaneous final
state, have aggregate physical occurrence drift

\[
 \sum_i\delta(a_i)=e_{h_0}-e_{h_t}+r.                 \tag{3.5}
\]

Assume \(r(h_0)=r(h_t)=0\), the terminal row \(h_t\) has initial load at
least two, and

\[
 \lambda(T)+r(T)\ge1
 \quad\text{for every initially covered }T\ne h_t.   \tag{3.6}
\]

Then applying all moves fills \(h_0\) and creates no new hole; other old
holes may remain or may also be filled.  A sufficient special case is the
literal unit-transfer path

\[
 \delta(a_i)=e_{h_{i-1}}-e_{h_i}\quad(1\le i\le t),  \tag{3.7}
\]

with no remainder.

Separately, if unit-transfer atoms form a closed cycle, their total drift is
zero and the initial hole remains.  Thus a closed unit-transfer cycle alone
cannot close one hole.

#### Proof

The chosen hole gains one occurrence, the terminal row loses one but remains
positive, and (3.6) protects every previously covered row.  Literal final
loads are nonnegative on the other old holes.  Formula (3.7) telescopes to
(3.5) with \(r=0\).  In the cyclic case it telescopes to zero.  \(\square\)

This is the constructive principle: route the debt to multiplicity reserve.
A purported balanced cycle which never meets reserve is only a shuttle.

### Corollary 3.3 (reserve-augmented cycle criterion)

In the exact unit-transfer abstraction, direct an atom edge \(u\to v\) when
its full drift is \(e_u-e_v\): it moves the unique debt from \(u\) to \(v\).
Adjoin one formal **reserve edge** \(r\to h_0\) for every row \(r\) of
initial load at least two.  Every compatible directed
\(h_0\)-to-\(r\) atom path, together with a residual circulation whose full
simultaneous remainder satisfies (3.6), is a hole-closing macro.  It is
equivalently a directed cycle through \(h_0\) after adjoining the formal
reserve edge, plus safe residual cycles.  Conversely, any no-new-hole
unit-transfer flow whose only net imbalances fill \(h_0\) and consume one
reserve unit decomposes into such a path plus directed cycles; their complete
aggregate ledger, not graph containment alone, supplies safety.

The reserve edge is bookkeeping, not another word operation: it records
that the final physical loss consumes one occurrence above the required
baseline.  A cycle containing no such edge merely transports or returns the
debt.

## 4. The K16 affine shuttle and holonomy

At position \(p=6440\) of the append-\(0200\) word, define

\[
 X_+(s)=0xa000\vee s,\qquad
 X_-(s)=0x2004\vee s,\qquad s\subseteq0x0069.          \tag{4.1}
\]

There are sixteen values on each shore.  The authenticated minimum-debt
graph is \(K_{16,16}\): every \(X_+\to X_-\) move transports the sole hole
from \(0x287d\) to \(0xa879\), and every reverse move transports it back.

### Proposition 4.1 (portal latch invariant)

Every shuttle edge satisfies

\[
 \boxed{
 0x287d\vee X_+(s)
 =0xa879\vee X_-(t)
 =0xa87d.}                                             \tag{4.2}
\]

Hence all 256 return edges form one affine portal latch, not an absorber.

#### Proof

The optional mask \(0x0069\) lies in both target sides.  The first union
adds the phase bit \(0x8000\); the second adds the missing bit \(0x0004\).
Both give \(0xa87d\).  The exact one-cell audit supplies the stated debt
transition and the complete return audit proves nonabsorption.  \(\square\)

The newer global state supplies a larger literal holonomy:

\[
 0x4e63\longrightarrow0x287d
 \longrightarrow0xa879\longrightarrow0x4e63.          \tag{4.3}
\]

The first leg uses one of 128 terminal portal values, the second one of 16
central portal values, and the third the terminal portal again.  The exact
radius-three audit covers all \(128\cdot16=2048\) sharp two-step states and
every possible third substitution.  No state completes; among minimum third
rows, 2,048 return the sole hole to \(0x4e63\), while 32,768 return it to
\(0x287d\).  Thus (4.3) is a genuine support-level closed defect-transport
cycle, and Theorem 3.1 explains why it is not a completion.  The audit does
not assert that each leg has full occurrence drift \(e_u-e_v\); any additive
macro must use its simultaneous literal ledger as required in Lemma 3.2.

## 5. Full-gap decomposition

Let disjoint variable collars \(C_1,\ldots,C_s\) occur in order.  Let \(G_i\)
be the complete fixed subword between \(C_i\) and \(C_{i+1}\), and assume

\[
 \bigvee G_i=\Omega                                   \tag{5.1}
\]

for every \(i\).

### Theorem 5.1 (full-gap decomposition)

For every proper target \(T\ne\Omega\), a \(T\)-witness interval meets at
most one variable collar.  Every nonfixed witness therefore has the exact
form

\[
 \text{suffix of the left fixed gap}\ \vee\
 \text{one contiguous interval of }C_i\ \vee\
 \text{prefix of the right fixed gap}                 \tag{5.2}
\]

for one \(i\), with either fixed side allowed to be empty.  Thus all proper
target constraints are disjunctions of exact per-collar interval forms;
there is no cross-collar interval synergy.

Equivalently, for edits supported in two different collars, every proper
target load has zero mixed finite difference:

\[
 \lambda^{ij}(T)-\lambda^i(T)-\lambda^j(T)+\lambda^0(T)=0. \tag{5.3}
\]

#### Proof

An interval meeting \(C_i\) and a later \(C_j\) contains an intervening
fixed gap of OR \(\Omega\).  Its OR is therefore \(\Omega\), contradicting
\(T\ne\Omega\).  An interval meeting one collar has exactly form (5.2).
Since no proper-target interval sees two collars, its contribution is a sum
of one-collar functions, which gives (5.3).
\(\square\)

The same statement holds after declaring a cut in a cyclic word.  If every
fixed arc between consecutive collars has full OR, a proper cyclic witness
meeting two collars contains one such arc and is impossible.

### Corollary 5.2 (separator-breaking necessity)

Suppose arbitrary assignments to one declared frozen collar family cannot satisfy
the per-collar forms (5.2).  Then no successful word with the same fixed
gaps can differ only inside those collars.  Every completion must either:

1. alter at least one full-OR gap; or
2. rethread the blocks so two service collars become adjacent without
   traversing a full-OR gap.

This is stronger than a Hamming-radius statement because the collar entries
were already arbitrary masks.

For K16, the six-cell family (0.2) leaves 17 residual proper targets and its
exact arbitrary-value finite model returned infeasible.  The widened family
(0.3) leaves 30 residual targets and its corresponding model also returned
infeasible.  These finite solver results are calibration, not premises of
Theorem 5.1; together with the proved decomposition they give a barrier for
those two frozen architectures.  A larger collar that alters or crosses a
separator remains open.

## 6. A constructive gap-opening braid

Consider

\[
 W=A\mid P\mid G\mid Q\mid H\mid D,\qquad
 \bigvee G=\bigvee H=\Omega.                          \tag{6.1}
\]

All six displayed blocks are assumed nonempty.

Define the three-cut block transposition

\[
 \boxed{
 A\mid P\mid G\mid Q\mid H\mid D
 \longmapsto
 A\mid P\mid Q\mid G\mid H\mid D.}                   \tag{6.2}
\]

It replaces the old seams

\[
 P|G,\quad G|Q,\quad Q|H                              \tag{6.3}
\]

by

\[
 P|Q,\quad Q|G,\quad G|H.                            \tag{6.4}
\]

### Theorem 6.1 (gap-opening three-cut braid)

Operation (6.2):

1. preserves length, the multiset of cells, every coordinate mass, and
   total phase mass;
2. preserves every interval internal to one displayed block;
3. changes only occurrences crossing a seam in (6.3) or (6.4), with exact
   ledger (2.1);
4. creates at \(P|Q\) every crossing mask

   \[
       \bigvee(\text{suffix of }P)\ \vee\
       \bigvee(\text{prefix of }Q);                   \tag{6.5}
   \]

   before the braid no proper target interval could meet both \(P\) and
   \(Q\); and
5. changes the phase-boundary count and coordinate runs only at the three
   old and three new seams.

#### Proof

The operation permutes intact blocks, proving items 1--2.  Internal interval
loads therefore cancel from (2.1), proving item 3.  Every old interval from
\(P\) to \(Q\) contains all of \(G\) and has full OR; after the swap the
suffix--prefix interval is contiguous at \(P|Q\), proving item 4.  Internal
adjacencies are unchanged, proving item 5.  \(\square\)

For a Johnson carrier, orient the retained fragments as declared.  If the
three new endpoint pairs are Johnson edges, no inserted undirected edge
duplicates a retained or another new edge, no directed two-cycle is created,
and the desired endpoint monodromy holds, then (6.2) is a literal simple
three-cut segment braid preserving every middle owner.  Fixed shadow windows
change only in the three seam halos.  Arbitrary upper shadows are preserved
exactly when they retain an uncut witness or acquire an accepting
accumulated-union path.

Thus (6.2) is a concrete all-scale move, not an annealing neighbourhood.  It
breaks one full-gap separator using only three physical joins and creates
the cross-collar occurrence forbidden by Theorem 5.1.

### Lemma 6.2 (exact compatible witness section)

Fix variable positions \(C\).  For every target \(T\) to be serviced,
select one occurrence-labelled interval \(I_T\), and put

\[
 f_T=\bigvee_{i\in I_T\setminus C}W_i,qquad
 V_T=I_T\cap C,qquad
 A_p=\bigcap_{T:p\in V_T}T.                          \tag{6.6}
\]

There are nonempty masks \(X_p\), \(p\in C\), making every selected
interval have OR exactly \(T\) if and only if, for every selected row and
every used position,

\[
 f_T\subseteq T,qquad A_p\ne\varnothing,qquad
 f_T\cup\bigcup_{p\in V_T}A_p=T.                    \tag{6.7}
\]

#### Proof

Necessity follows because every feasible \(X_p\) lies in every target using
it, hence \(X_p\subseteq A_p\).  Therefore the final OR is contained in the
right side of (6.7), which is itself contained in \(T\); equality forces
(6.7).  Conversely choose \(X_p=A_p\).  Equation (6.7) then makes every
selected interval exact.  Unused positions are arbitrary nonempty masks.
\(\square\)

For typed Johnson or compiler cells with domains \(\mathcal D_p\), the same
statement becomes the finite section problem

\[
 X_p\in\mathcal D_p,quad X_p\subseteq A_p,quad
 f_T\cup\bigcup_{p\in V_T}X_p=T.                    \tag{6.8}
\]

The unrestricted intersection criterion is then only a relaxation.  This is
the missing compatibility test between a list of individually legal service
intervals and one literal simultaneous braid; marginal Hall or raw provider
counts alone do not imply it.

## 7. Balanced seam-braid closure

Let \(\mathcal A\) be compatible gap-opening braids of type (6.2), possibly
with fragment reversals.  Give each atom its complete physical occurrence,
phase, shadow, and compiler signed vectors.  Disjoint bounded seam halos make
only bounded fixed-window ledgers additive.  For objective OR rows and
arbitrary upper rows, require either the zero mixed interaction supplied by
Theorem 5.1 or one literal combined final-state vector for the interacting
family.

### Theorem 7.1 (balanced seam descent)

Suppose a selected family satisfies:

1. all new carrier seams are literal and final fragment monodromy has the
   required path or cycle topology;
2. its simultaneous objective occurrence vector satisfies the
   path-to-reserve hypotheses of Lemma 3.2 for a chosen old hole;
3. every initially covered physical target \(T\) satisfies

   \[
      \lambda(T)+\delta_{\mathcal A}(T)\ge1;          \tag{7.1}
   \]

4. every fixed lower and upper shadow satisfies its exact occurrence ledger;
5. every arbitrary upper target has an uncut witness or a final accepting
   path;
6. all newly selected service paths have a common literal realization,
   certified by Lemma 6.2 or its typed form (6.8); and
7. final coordinate runs and compiler pins pass their literal tests.

Then the simultaneous braid fills the chosen objective hole, creates no new
hole, and preserves the complete carrier/compiler interface.

#### Proof

Lemma 3.2 fills the objective row by spending one duplicate occurrence.
Equation (7.1) preserves every other word target.  Theorem 2.1 gives all
fixed word-occurrence ledgers; the established shadow-braid ledger supplies
the fixed carrier rows.  The compatible section, final accepting paths, run
test, and compiler test supply its remaining hypotheses.  \(\square\)

### Theorem 7.2 (slack-terminated alternating port circulation)

Let \(H=(L,R;E)\) be a bipartite graph of legal tail-to-head joins on a
protected reservoir, with \(|L|=|R|=n\), and suppose

\[
 |N_H(X)|\ge\min\{n,|X|+h\}
 \qquad(\varnothing\ne X\subseteq L).                \tag{7.2}
\]

Let \(M_0\) be the old endpoint matching.  Prescribe a service matching
\(K\subseteq E\) of size at most \(h\).  Assume:

1. the seams in \(K\), their objective drifts, and their service intervals
   satisfy the ledger and typed-section conditions 2--6 of Theorem 7.1, and
   every variable seam on a service path belongs to \(K\);
2. every positivity-only protected target or compiler realization not
   explicitly serviced has a literal witness or realization disjoint from
   the entire cut reservoir;
3. every edge of \(H\) is Johnson-, simplicity-, and collar-legal; and
4. for every perfect extension of \(K\) in \(H\), the residual joins have
   zero combined drift on every serviced row and every equality-constrained
   occurrence, shadow, or compiler row (it suffices that full-gap separation
   makes all mixed terms vanish).

Then \(K\) extends to a perfect endpoint matching \(M\).  The owner edit
\(M_0\mathbin\triangle M\) is a disjoint union of even alternating cycles,
while its target occurrence ledger contains the open, reserve-terminated
augmenting path carried by \(K\).  Hence it gives the protected descent of
Theorem 7.1 as an exact cycle cover.  If the chosen completion also has the
required monodromy or a certified safe opening, it gives the required final
carrier topology.

#### Proof

Delete the endpoints of \(K\).  For \(X\subseteq L\setminus L(K)\), if
\(|X|+h\le n\), then

\[
 |N_{H-K}(X)|\ge |X|+h-|K|\ge|X|.
\]

If \(|X|+h>n\), (7.2) gives every right vertex as a neighbor before the
deletion, so \(|N_{H-K}(X)|=n-|K|\ge|X|\).  Hall's theorem extends \(K\)
to \(M\).  The symmetric difference of two perfect matchings is a union of
even alternating cycles.  The disjoint protected witnesses make residual
completion edges harmless to all nonservice rows; hypothesis 4 makes their
complete simultaneous ledger transparent on the service rows.  The service
matching therefore supplies the ledger required by Theorem 7.1.  \(\square\)

This is the precise balanced-cycle mechanism: closed owner-space cycles can
carry an open target-space augmenting path, but only if the path terminates
at occurrence reserve.

### Corollary 7.3 (phase-pair absorber)

Suppose \(\nu(S)=1\), with unique projected occurrence \(I\).  If a
protected port circulation preserves \(I\), creates a distinct projected
occurrence \(J\) of \(S\), assigns opposite phase activities to \(I,J\), and
terminates every resulting physical loss at a row retaining another
occurrence, and if no other projection's deficit term increases:

\[
 (2-\nu'(R))^+\le(2-\nu(R))^+\qquad(R\ne S).         \tag{7.3}
\]

then it covers both \(S\) and \(S+z\), decreases \(\Phi_z\) by at least one,
and creates no physical hole.  The decrease is exactly one if equality holds
in (7.3) for every \(R\ne S\).

This is exactly the duplicate projected occurrence which pure phase cannot
create.  It is local to the live defect and does not demand two witnesses for
every projection.

No prefix of the atoms need be complete.  Shuttle dependencies may be fired
as one macro, but at least one dependency path must terminate in reserve.

## 8. K16 reconciliation

The canonical verified word is

    answers/k16_upper12875.word
    SHA-256 d4690a0d11f1d8e69765ec988d9fbcbac63d354ebd6ab07aa8081b577a9ac0c9

The append-\(0200\) one-hole word is

    scratch/k16_append0200_12874_onehole.word
    SHA-256 aa17f3ca70525115c941e906fecf1384bad8302cd95b236413c7f2f3f8777c18

It has 6376 tagged cells, 122 cyclic phase boundaries, and
\(\Phi_z=1\), with unique projected occurrence

\[
 0x287d:[6439,6441].                                  \tag{8.1}
\]

Both fixed gaps around (0.2) have full OR.  The narrow arbitrary-value model
has 17 residual targets and is infeasible.  The widened model has 30
residual targets and is also infeasible.  Corollary 5.2 therefore forces any
completion outside both isolated-collar architectures.

The global word is

    scratch/k16_fivephase_rex_hole20067.word
    SHA-256 eef3555aa12675de8707de994d20300aaf8e96538b4691880810d84454fbb1b5

It is exactly the verified word with position 6435, value \(0x0600\),
deleted, followed by 78 substitutions.  All 78 changes are outside the
narrow collars and 77 are outside the widened collars.  Its phase profile is

\[
6365\text{ tagged cells},\qquad144\text{ cyclic boundaries},              \tag{8.2}
\]

and \(\Phi_z=1\), with unique projected occurrence

\[
 0x4e63:[12869,12872].                                \tag{8.3}
\]

Its sole physical hole is \(0x4e63\).  The complete one-cell census has
26,916 service assignments, collateral floor one, and 128 terminal
minimizers; every minimum move exchanges the \(0x4e63\) debt for
\(0x287d\).  The larger holonomy (4.3) proves that global separator crossing
enlarges the defect graph, but it has not yet found a reserve sink.

The 78-cell relation is a literal-word theorem.  No retained artifact yet
proves that those substitutions are the image of an all-depth-safe
PBBS/Johnson braid.  That provenance remains part of the all-\(k\) gate.

## 9. All-\(k\) shadow-braid interface

The full-gap theorem is the word-level form of an accumulated-union barrier.
In a PBBS/Pascal carrier, a retained fragment whose union is the full ground
set blocks every proper upper accepting path from using ports on both sides.
A local router atlas confined to collars separated by such fragments cannot
regenerate a cross-interface witness.

Define \({\rm GCR}(r,d)\), the **gap-crossing reserve property**, as follows.
For every all-depth-complete, resident PBBS/Pascal near-carrier in the
protected PPR class with a nonempty canonical hole bank:

1. there is a finite selected family of literal gap-opening three-cut braids
   (6.2), with endpoint Johnson tests and \(d\)-collars certified;
2. their objective occurrence vectors contain a path from some hole row to a
   row of load at least two, and their simultaneous literal ledger preserves
   every initially covered row;
3. their one simultaneous final state leaves every required fixed
   lower/upper shadow load positive, preserves the declared exact q1
   multiplicity vector whenever the protected class requires q1 exactness,
   and retains a feasible compiler pin matching; and
4. every arbitrary upper casualty has an uncut witness or a declared final
   accepting path through the same braids;
5. the selected service paths and variable seam cells admit one typed
   compatible witness section (6.8); and
6. the residual endpoint circulation has the required simple monodromy and
   protected opening.

### Theorem 9.1 (GCR gives strict descent)

If \({\rm GCR}(r,d)\) holds, the near-carrier admits a literal one-hole
descent, meaning that its hole count drops strictly, preserving residence,
the complete lower tower, all arbitrary upper shadows, and the pinned
compiler.  If every length-preserving successor remains in the same
protected GCR class, iteration reaches a complete carrier after at most the
initial number of holes.

#### Proof

Apply Theorem 7.1 to the GCR family.  Its conclusion is the missing protected
one-hole descent.  The hole count is a nonnegative integer and drops at each
step, proving finite termination under the stated closure.  \(\square\)

Separately, if the resulting complete carrier also satisfies all external
protected Pascal reservoir and full-compiler hypotheses, the established
decorated Pascal compiler theorem produces a word of length

\[
 \binom{2r+1}{r+1}+d.                                 \tag{9.1}
\]

### Conjecture 9.2 (gap-crossing reserve conjecture)

For \(d=d(2r+1)\), every PBBS/Pascal near-carrier satisfying the established
all-depth support and protected compiler hypotheses has
\({\rm GCR}(r,d)\), with a braid family of size polynomial in \(r+d\).

This is stronger than connectivity and weaker than an arbitrary universal
router.  It asks for a path from at least one live defect to existing
multiplicity reserve in every nonempty successor, plus exact circulation on
the shadow and compiler rows.  The K16 six/ten-cell results prove why
separator crossing is necessary; the global \(0x4e63\) phase proves that the
defect graph genuinely extends beyond the local shuttle.  Neither fact
proves the reserve endpoint.

## 10. Frozen artifacts and scope

The new lightweight reconciliation audit is

    scratch/audit_k16_phase_gap_transport_frontier_20260730.py
    SHA-256 6f818c32b343e87a51c21fa606095a22d04dfdb437452b48d385e57fb017f3f5
    scratch/k16_phase_gap_transport_frontier_20260730.audit.json
    SHA-256 b1150e310f036759ea5dfaf9301c3e0a62afe2174a69fd1237481ae40e5e0d3b
    payload dd75647130162549a84c45594356d0d57516f8a73376e3c44a72d7295513d393

It verifies the word hashes, exact coverage, phase profiles, projected
deficits, delete-plus-78 relation, both full-gap decompositions, the retained
narrow-collar result, the \(K_{16,16}\) shuttle, and the exact one-cell floor
at the \(0x4e63\) state.  It performs no annealing or solver search.

The exact local and global transport graphs are frozen in

    scratch/k16_append0200_onehole_return_cycle_20260730.audit.json
    SHA-256 cbdf91496c3bd7862304f9d5b1fdd0f7084f1e35f15a6163a58fb0eb9c39dcd6
    scratch/k16_fivephase_return_graph_20260730.audit.json
    SHA-256 3948e904d00ac17024277a0e7010de90ebf70a07e3c3cf00a14a257886962d95
    scratch/k16_fivephase_radius3_sharp_fibre_exact_20260730.audit.json
    SHA-256 b164a2067d03fc968659ba89bf9c41b3fae242d81bbecb865651944b33efb629

The narrow arbitrary-collar model is

    scratch/search_k16_append0200_phase_collar_csp_20260730.py
    SHA-256 e29dca66534bd81240fe22507569e07d203e5eaf1daa553bdc3b09e3e7a1bbff
    scratch/k16_append0200_phase_collar_csp_20260730.audit.json
    SHA-256 20cbfa5ef4bfe51f288db864fcedb224bdff99ac12064ca49ab10d20f8fce069

The widened-collar infeasibility is used as an authoritative exact input but
was not independently replayed here because its retained artifact was not
present at the time of writing.

The narrow six-cell result is semantically exact for its declared finite
model.  Its current compact artifact records CP-SAT infeasibility but no
independently checkable DRAT/LRAT proof; it is used only as K16 calibration,
not as a premise of Theorems 1.1--9.1.

No length-12,874 universal word, unconditional GCR theorem, or all-\(k\)
upper bound is claimed.  The proved advance is the separator theorem, the
two reserve invariants, the constructive gap-opening move, the exact common
witness-section test, and the transparent-residual Hall completion theorem
identifying what a successful global shadow braid must do.
