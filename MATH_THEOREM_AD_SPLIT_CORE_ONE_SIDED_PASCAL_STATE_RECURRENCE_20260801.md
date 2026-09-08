# The inherited-site split-core state has a sharp shared-bank residence horizon

Date: 2026-08-01  
Lane: AD, same-parity `B+1` recurrence  
Status: exact algebraic no-reset plateau/jump packet transducer, exact
terminal-socket transducer, minimal two-address native-`q1` repair, and an
exact obstruction to indefinite residence closure.  The construction
of the global child preword, its protected upper-exact Hamilton path, all
mixed cap/guard rows, arbitrary-depth background transport, and one common
compiler cap remain hypotheses.  No claim `nu(k)<=B(k)+1` is made.

The inherited-index block identities agree with the independently frozen
prefix-automaton theorem
`MATH_THEOREM_A_K2_PIVOT_ONE_ENDED_PREFIX_EXTENSION_AND_RELATIVE_EROSION_20260801.md`.
At owner/native-`q1` scope they agree exactly.  This note corrects that
theorem's unqualified repeated-jump residence claim: paired-bank sharing has
the sharp finite horizon in Theorem 5.2.  The other distinct content audited
here is the paired-bank singleton geometry, explicit terminal-nonowner
socket, triangular slack ledger, and exact conditional child-state count.

## 0. Outcome

Put

\[
 k=2m-1,\qquad r=m,\qquad
 W={2m-1\choose m},\qquad B(k)=W+h,
\]

where `h=d_m` is the triangular deadline.  The desired additive-one state
has

\[
 D^hA^+=(O_0,O_1,\ldots,O_{W-1},a).                  \tag{0.1}
\]

The first `W` cells are all rank-`r` owners exactly once, ordered as a
rooted upper-exact Hamilton path.  The last cell `a` is the unique omitted
rank-`r-1` lower endpoint of that path.  Thus it is one controlled
nonowner, not an untyped scalar surplus.

Require the owner row to begin with the split-core pivot packet.  Deleting
its central source letter `[X]` changes its `3h+1` owner cells to

\[
 (L_0,\ldots,L_{h-1},U_0,\ldots,U_{h-1},
  R_0,\ldots,R_{h-1}),                                 \tag{0.2}
\]

where `L,R` have rank `r` and the `U` have rank `r+1`.  The exterior cells
and terminal `a` do not move.  Hence

\[
\begin{array}{c|c}
\text{pre-insertion}&2h\text{ packet owners}+h\text{ upper cells}
 +(W-3h-1)\text{ exterior owners}+a=W,\\
\text{post-insertion}&(3h+1)\text{ packet owners}
 +(W-3h-1)\text{ exterior owners}+a=W+1.
\end{array}                                             \tag{0.3}
\]

This is an exact nonflat cell-to-turn conversion.  It is not insertion into
an already-flat length-`B(k)` source.

Two further exact transducers are proved.

1. The packet regenerates under `(r,h)->(r+1,h+epsilon)`,
   `epsilon in {0,1}`.  At a jump, using the two new coordinates
   `alpha,gamma`,

   \[
   \Lambda'=(\alpha,\Lambda),\quad P'=(P,\gamma),\quad
   D'^-=(\gamma,D^-),\quad D'^+=(D^+,\alpha),          \tag{0.4}
   \]

   and the child central owners are

   \[
   M'_0=M_0+\alpha,\quad
   M'_j=M_{j-1}\cup M_j\ (1\le j\le h),\quad
   M'_{h+1}=M_h+\gamma.                                \tag{0.5}
   \]

   Thus parent upper turns become child owners and parent owners become
   child lower turns.

2. If the final `h+2` source letters realize consecutive cells
   `O,a`, where `a subset O`, `|O|=r`, `|a|=r-1`, then

   \[
   (O,a)\longmapsto
   \begin{cases}
   (O+\beta,a+\beta),&\epsilon=0,\\
   (O+\alpha,O),&\epsilon=1.
   \end{cases}                                         \tag{0.6}
   \]

   Hence one terminal nonowner regenerates exactly; at a jump the old
   endpoint owner becomes the new missing lower endpoint.

The sparse split source has four nonnative lower intersections.  They all
vanish after changing only two existing source positions.  For arbitrary

\[
                         1\le j<h,\qquad2\le s\le h,   \tag{0.7}
\]

replace

\[
 \{\lambda_j\}\mapsto(K-\{x_R\})+\lambda_j,qquad
 \{\rho_s\}\mapsto(K-\{x_L\})+\rho_s.                \tag{0.8}
\]

All `(h-1)^2` choices preserve the owner row, pre-row, insertion rays,
residence, and pre-to-post OR deck, and make every lower and upper `q1`
cell literal at its native address.  Two changed positions are necessary
among enlargement-only repairs.  A two-site repair does remove the original
one-letter cells `{lambda_j},{rho_s}`; absent alternate singleton hosts this
is a real two-target compiler debt.  The proof-safe recurrence does **not**
reset the repair sites.  It uses

\[
 (j,s)\longmapsto
 \begin{cases}
   (j,s),&h'=h,\\
   (j+1,s),&h'=h+1.
 \end{cases}                                           \tag{0.9}
\]

At a jump `Lambda'=(alpha,Lambda)` shifts the same enriched logical
`lambda_j` to index `j+1`, while `P'=(P,gamma)` leaves the same enriched
logical `rho_s` at index `s`.  Since `j<h` implies `j+1<h+1`, and
`2<=s<=h<h+1`, menu validity is invariant.  If the active pair is
jump-born, its opposite-bank hosts in `D^+` and `D^-` persist.  For a barred
base pair, literal transport of its exterior hosts remains an antecedent.
Moreover the fresh `alpha` and `gamma` each
occur as literal singleton source letters twice: once in the newly inserted
central position and once on the opposite outer collar.  Thus the newborn
singleton targets also remain literal.  No packet formula, Pascal-sector
tag, native-`q1` row, or local owner cap forces a fresh reset.  A mixed
compiler/common-cap row may still reject the inherited pair; Theorem 7.1
assumes admissibility.  Thus a new repair choice is not an algebraic local
gate, but can be forced by the unresolved exterior ledger.

There is, however, a different exact obstruction.  Every jump coordinate is
used once in a central bank and once in the opposite outer bank.  If it was
introduced when the new depth was `H`, those two positive owner runs have an
internal zero-gap of fixed length `2H-1`.  At a later depth `d` signed
residence requires `2H-1>=d+1`, equivalently `d<=2H-2`.  Starting from a
disjoint depth-`h_0` base, all shared labels remain resident for exactly the
first `h_0` deadline jumps, and the oldest pair fails at jump `h_0+1`.
Changing only `(j,s)` does not alter these two occurrences, so a fresh `K2`
repair-site reset does not cure the obstruction.  An unbounded recurrence
needs a genuine shared-bank rebase, occurrence removal, or a nonlocal
residence rethread.

Placing the packet at the global word start discharges all left clipped
flags.  The packet exports its literal right suffix word `omega_h`, one
nested right gap-exclusion schedule `Gamma_h`, the terminal pair, and the
two cap choices.  At a jump

\[
                         \omega_{h+1}=(\omega_h,\{\alpha\}). \tag{0.10}
\]

This is a bounded number of structured state objects, but `omega_h`,
`Gamma_h`, and the shared-label birth ledger themselves have length
`Theta(h)`.  The local formulas do not construct the child exterior
completion or the required eventual shared-bank residence rebase.

## 1. State and feasibility

For a source word `A=(A_0,...,A_(N-1))`, write

\[
                       (D^hA)_i=\bigcup_{t=i}^{i+h}A_t. \tag{1.1}
\]

The packet requires

\[
 h\ge2,\qquad r-h\ge2,\qquad |\Omega|\ge r+3h.        \tag{1.2}
\]

On the odd ground `|Omega|=2r-1`, the last condition is `3h<=r-1`.
It is eventually compatible with `h=Theta(sqrt(r))`, but small dimensions
need separate bases.

A one-sided state `S(r,h)` consists of:

1. a length-`W+h+1` source with row (0.1);
2. a rooted upper-exact Hamilton owner path: consecutive owners are Johnson
   neighbours, their `W-1` lower colours are distinct and omit exactly `a`,
   their upper colours cover every rank-`r+1` set, and
   `a subset O_(W-1)`;
3. the split-core packet as the initial owner segment and the literal
   terminal cell `a`;
4. one selected literal occurrence for every lower target, with the packet
   transitions supplied at their native shared cells; and
5. the exact packet suffix `omega_h`, right gap schedule `Gamma_h`, and
   terminal source word `theta_h`;
6. the birth depth of every coordinate shared between the central and outer
   banks, together with the inequalities `h<=2H_i-2`, or an explicit
   residence compensation hitting each failed internal gap.

When the two-site repair is used, the state also records literal alternate
hosts for `{lambda_j}` and `{rho_s}`.  These hosts are part of the state
transition, not consequences of owner geometry.  The internally closed case
uses singleton occurrences of the same labels in the opposite `D^+` and
`D^-` banks; an exterior host is allowed only if the child exterior theorem
transports it literally.  The fresh jump pair is not enriched and instead
has two singleton occurrences per coordinate; a disjoint-bank base need not
provide hosts for an arbitrary enriched pair.

The protected Hamilton path and literal lower occurrence matching are
separate requirements.  An abstract Johnson intersection is not by itself
a source interval.

## 2. The repaired split-core packet

Write

\[
 K=C\mathbin{\dot\cup}X_L\mathbin{\dot\cup}X_R,qquad
 X=X_L\mathbin{\dot\cup}X_R,qquad |K|=r-h,            \tag{2.1}
\]

with `X_L,X_R` nonempty, and fix `x_L in X_L`, `x_R in X_R`.
Let

\[
 \Lambda=(\lambda_1,\ldots,\lambda_h),\quad
 P=(\rho_1,\ldots,\rho_h),\quad
 D^\pm=(d^\pm_1,\ldots,d^\pm_{h-1})                  \tag{2.2}
\]

and fresh `q^-,q^+`.  Initially all displayed banks are disjoint.  Section
5 gives the exact endpoint-sharing pattern permitted after repeated jumps.

Define the sparse length-`h` blocks, suppressing singleton braces,

\[
\begin{aligned}
 E_h^-&=(d^-_1,\ldots,d^-_{h-2},CX_Ld^-_{h-1},
                                      (X_R-x_R)q^-),\\
 \bar A_h^-&=(\lambda_1,\ldots,\lambda_{h-1},CX_L\lambda_h),\\
 \bar A_h^+&=(CX_R\rho_1,\rho_2,\ldots,\rho_h),\\
 E_h^+&=((X_L-x_L)q^+,CX_Rd^+_1,d^+_2,\ldots,d^+_{h-1}).
                                                               \tag{2.3}
\end{aligned}
\]

For `(j,s)` as in (0.7), obtain `A_h^-(j)` from `bar A_h^-` by the first
replacement in (0.8), and obtain `A_h^+(s)` from `bar A_h^+` by the second.
Put

\[
 \mathcal P_h^+(j,s)=E_h^-A_h^-(j)[X]A_h^+(s)E_h^+,
 \quad
 \mathcal P_h^-(j,s)=E_h^-A_h^-(j)A_h^+(s)E_h^+.      \tag{2.4}
\]

Define

\[
\begin{aligned}
 M_t&=K\cup\rho[1,t]\cup\lambda[t+1,h],\\
 U_t&=M_t\cup M_{t+1},\\
 L_t&=((K-x_R)+q^-)\cup\lambda[1,t+1]\cup D^-[t+1,h-1],\\
 R_t&=((K-x_L)+q^+)\cup\rho[t+1,h]\cup D^+[1,t].       \tag{2.5}
\end{aligned}
\]

The exact factorization, independent of `(j,s)`, is

\[
\begin{aligned}
 D^h\mathcal P_h^+(j,s)
   &=(L_0,\ldots,L_{h-1},M_0,\ldots,M_h,R_0,\ldots,R_{h-1}),\\
 D^h\mathcal P_h^-(j,s)
   &=(L_0,\ldots,L_{h-1},U_0,\ldots,U_{h-1},R_0,\ldots,R_{h-1}).
                                                               \tag{2.6}
\end{aligned}
\]

All final cells are distinct rank-`r` owners forming a Johnson path; every
internal positive run has length at least `h+1`.  Deleting `[X]` preserves
every old interval OR in every fixed exterior context because the two new
adjacent letters have union containing `K`, hence `X`.

The right boundary word is independent of `(j,s)`:

\[
 \boxed{\omega_h=E_h^+
   =((X_L-x_L)q^+,CX_Rd^+_1,d^+_2,\ldots,d^+_{h-1}).} \tag{2.7}
\]

The insertion-born short-cell occurrences are

\[
 [X],\qquad [P_i],\ [S_i]\quad(1\le i<h),             \tag{2.8}
\]

where

\[
 P_i=K\cup\lambda[h-i+1,h],\qquad
 S_i=K\cup\rho[1,i].                                  \tag{2.9}
\]

They are occurrences, not all new target vertices:

\[
 P_{h-1}=M_0\cap M_1,qquad
 S_{h-1}=M_{h-1}\cap M_h.                             \tag{2.10}
\]

A target matching counts each equality in (2.10) once, choosing either
physical occurrence.

## 3. Two enrichments are necessary and sufficient

For a source `(a_i)` with fixed depth row, put

\[
 O_t=\bigcup_{p=t}^{t+h}a_p,qquad
 C_t=\bigcup_{p=t+1}^{t+h}a_p.                         \tag{3.1}
\]

Then

\[
 O_t\cap O_{t+1}=C_t\cup(a_t\cap a_{t+h+1}).          \tag{3.2}
\]

The sparse split source is tight except at four transitions.  Its two left
missing-coordinate sets have union `K-x_R`, and every source position
`lambda_j`, `1<=j<h`, lies in both deficient left shared ranges.  Hence the
left replacement in (0.8) repairs both.  Symmetrically every
`rho_s`, `2<=s<=h`, lies in both deficient right shared ranges and the right
replacement repairs both.  Every addition lies in the maximal envelope of
its source position, so (2.6) is unchanged.  Equation (3.2) now gives

\[
       \bigvee(\text{the }h\text{ shared letters})
             =O_t\cap O_{t+1}                          \tag{3.3}
\]

at all `3h` transitions.  The `h+2` spanning letters tautologically realize
each adjacent owner union.  Both `q1` palettes are therefore literal and
injective.

The always-nonempty left-outer deficit can be repaired only from its shared
position range `[h-1,2h-2]`; the always-nonempty right-outer deficit only
from `[2h+2,3h+1]`.  These ranges are disjoint.  Thus at least two source
positions must change in any enlargement-only repair, while (0.8) attains
two.  The menu has exactly `(h-1)^2` choices.

The enriched positions may alter the sparse source deck.  All transparency
claims compare `\mathcal P_h^-(j,s)` with `\mathcal P_h^+(j,s)` for the same
chosen pair.  No frozen compiler on the sparse source transports for free.
The two enlarged positions remain exact cap/guard obligations of the jointly
designed scaffold.

The exact `K2` and `K4` interfaces, and the formal one-shore accounting for
the intermediate `K3` choice, have the following ledger:

\[
\begin{array}{c|c|c|c}
\text{interface}&\text{changed addresses}&
 \text{lambda/rho singleton targets displaced}&\text{extra requirement}\\ \hline
K4&4&0&4\text{ cap/guard checks}\\
K3&3&1&1\text{ alternate singleton host}\\
K2&2&2&2\text{ alternate singleton hosts}.
\end{array}                                             \tag{3.4}
\]

Here `K4` is the four-nonsingleton enrichment of the authoritative tight
source; the `K3` row only counts repairing one shore centrally and the other
at its two nonsingleton positions (no symmetric `K3` source theorem is
claimed here); `K2` is (0.8).  The table concerns literal
lambda/rho singleton occurrences, not every target affected by changing a
source letter and not owner or `q1` defects.  All three interfaces require a
jointly redesigned compiler.  Thus `K2` is not strictly better in an
arbitrary scaffold.  It becomes closed for the two newborn coordinate
singletons at a jump because (5.3) supplies two literal occurrences of each.
Closure of the two inherited displaced targets is a state hypothesis; the
paired-bank normal form below proves it automatically once those active
labels are jump labels.

## 4. Plateau transition

Let `h'=h`, `r'=r+1`, and add a new coordinate `beta` to the fixed core:

\[
                         K'=K+\beta,qquad C'=C+\beta.  \tag{4.1}
\]

Keep the inherited pair

\[
                              (j',s')=(j,s).           \tag{4.1a}
\]

The logical enriched labels are unchanged.  Jump-born opposite-bank hosts
remain singleton; admissibility of any exterior host is assumed by the
child state.  Substitute `K',C'` in (2.3),(0.8).
Then

\[
 L'_t=L_t+\beta,\quad M'_t=M_t+\beta,\quad
 R'_t=R_t+\beta,\quad U'_t=U_t+\beta.                \tag{4.2}
\]

The inserted letter is still `X`, both rays gain `beta`, all native `q1`
cells remain exact, and the clipped traces are unchanged.  The right state
is

\[
 \omega'_h=((X_L-x_L)q^+,(C+\beta)X_Rd^+_1,
             d^+_2,\ldots,d^+_{h-1}).                  \tag{4.3}
\]

This proves exact plateau persistence of the repaired cells.  If the active
pair came from a previous jump, its copies in `D^+,D^-` remain singleton
hosts, so the `K2` interface is internally closed.  An exterior alternate
host instead remains an explicit child-transport hypothesis.  Choosing a
different `(j',s')` is legal only with its own singleton hosts and is not a
deck-preserving rewrite of a frozen parent compiler.  No plateau sector
identity forces such a change.

## 5. Deadline jump and recursive endpoint sharing

Let `H=h+1`, `r'=r+1`, and let `alpha,gamma` be the two new coordinates.
Use (0.4) and retain the same logical enriched labels, hence the child
indices

\[
                              j'=j+1,\qquad s'=s.       \tag{5.1}
\]

All four source blocks obey literal concatenation identities:

\[
\begin{aligned}
 E_H^-&=(\gamma)E_h^-,&
 A_H^-(j+1)&=(\alpha)A_h^-(j),\\
 A_H^+(s)&=A_h^+(s)(\gamma),&
 E_H^+&=E_h^+(\alpha).
\end{aligned}                                           \tag{5.2}
\]

Indeed `alpha` is prepended before the old `Lambda` block and `gamma` is
appended after the old `P` block, while the selected old source letters are
unchanged.  Thus every repaired native cell persists at the corresponding
shifted physical address.  This is stronger than merely recomputing the
child intersections.  In particular, the central child source is obtained
by literal prefix/suffix insertion; none of the inherited full-core source
values is withdrawn or reassigned.  A fresh reset would undo the two old
enrichments and create two different enriched values, so its source-deck
transport would be an additional compiler theorem.

The source still contains

\[
\begin{aligned}
 &\{\gamma\}\text{ as the first letter of }E_H^-,\quad
 \{\gamma\}\text{ as the last letter of }A_H^+(s),\\
 &\{\alpha\}\text{ as the first letter of }A_H^-(j+1),\quad
 \{\alpha\}\text{ as the last letter of }E_H^+.
\end{aligned}                                           \tag{5.3}
\]

Thus each fresh coordinate has two literal singleton source occurrences.
In the paired-bank state, the old enriched labels retain their old singleton
backups in the opposite outer bank; an exterior backup is covered by the
explicit child-transport hypothesis.  Thus no newborn selected singleton is
displaced locally, and no inherited one is displaced under the declared
host transition.

### Theorem 5.1 (no-reset `K2` persistence)

Suppose the depth-`h` packet uses a valid pair `(j,s)` and its two displaced
singleton targets have declared post-transition-admissible, cell-distinct
hosts.  Then the plateau packet
with pair `(j,s)` and the jump packet with pair `(j+1,s)` retain the same
repaired logical `lambda_j,rho_s` positions (the plateau adds its compulsory
core tag), all `3h'` native lower cells
are exact, and the two fresh jump-coordinate singleton targets remain
literal.  The pair remains in the `K2` menu and locally owner/`q1`-admissible
after every finite plateau/jump word.  Signed residence is separately
limited by Theorem 5.2.
No alternative repair-site choice is required by the packet owner row,
pre-row, either `q1` palette, the four Pascal sectors, or the packet's own
maximal owner envelopes.  Mixed exterior/compiler caps can still reject the
inherited physical addresses.

#### Proof

The plateau assertion is (4.1a)--(4.3).  At a jump the four literal source
identities (5.2) retain the two enriched source sets and merely shift the
left one by one address.  The inequalities following (0.9) preserve menu
admissibility.  Equations (3.2)--(3.3), with the shared-bank separation
proved below, give every native lower cell; spanning windows give the upper
cells.  Equation (5.3) gives the fresh singleton occurrences.  Algebraic
iteration uses (5.6).  Every packet source set lies in the intersection of the packet
owners whose windows contain it, by the exact factorizations, so the local
owner caps hold.  External deadline, address, or compiler guards are not
asserted and remain hypotheses of Theorem 7.1.  \(\square\)

The child owners are

\[
\begin{aligned}
 L'_0&=((K-x_R)+q^-)\cup\{\alpha,\gamma\}\cup D^-,\\
 L'_t&=L_{t-1}+\alpha &&(1\le t\le h),\\
 M'_0&=M_0+\alpha,\\
 M'_t&=U_{t-1} &&(1\le t\le h),\\
 M'_{h+1}&=M_h+\gamma,\\
 R'_t&=R_t+\gamma &&(0\le t<h),\\
 R'_h&=((K-x_L)+q^+)\cup\{\alpha,\gamma\}\cup D^+.
                                                               \tag{5.4}
\end{aligned}
\]

They are distinct rank-`r+1` Johnson owners.  Both palettes are injective;
by Section 3 both are literal.  The child central lower colours are exactly
`M_0,...,M_h`.  The rays satisfy

\[
 P'_i=P_i,\quad S'_i=S_i\ (i<h),\qquad
 P'_h=M_0,\quad S'_h=M_h,                            \tag{5.5}
\]

so the new top ray addresses duplicate existing child `q1` target values.
Equation (5.2) gives (0.10).

Repeated jumps do not return to pairwise-disjoint banks.  The exact closed
bank state is

\[
\begin{aligned}
 \Lambda&=(\alpha_t,\ldots,\alpha_1,\bar\Lambda),&
 D^+&=(\bar D^+,\alpha_1,\ldots,\alpha_t),\\
 P&=(\bar P,\gamma_1,\ldots,\gamma_t),&
 D^-&=(\gamma_t,\ldots,\gamma_1,\bar D^-),             \tag{5.6}
\end{aligned}
\]

where all barred banks and all displayed jump labels are mutually disjoint.
Thus the only allowed overlaps are

\[
                     \Lambda\cap D^+=\{\alpha_i\},
       \qquad P\cap D^-=\{\gamma_i\}.                 \tag{5.7}
\]

When the active enriched labels are jump labels, they are some `alpha_i` in
`Lambda` and some `gamma_j` in `P`, and (5.6) supplies their internal
singleton backups.  A base label with an exterior backup is carried under
the separate exterior-host hypothesis.  In either case, under the no-reset
map the indices change exactly as in (0.9), but the logical labels do not.
The next jump prepends
`alpha_(t+1)` to `Lambda`, appends it to `D^+`, appends `gamma_(t+1)` to
`P`, and prepends it to `D^-`, preserving (5.6).
The moving pairs used inside one collar remain disjoint:
`Lambda cap D^-=emptyset`, `P cap D^+=emptyset`, and
`Lambda cap P=D^- cap D^+=emptyset`.  Consequently the usual cutoff-index
proof of owner and palette injectivity remains valid at every repeated
jump.

For completeness, the shared labels also preserve native tightness.  In the
current depth-`h` source, the `Lambda` and `D^+` occurrences of every reused
`alpha_i` are at least `h+2` source positions apart; the `D^-` and `P`
occurrences of every reused `gamma_i` have the same separation.  The two
claims follow directly from block positions.  If their one-based within-bank
indices are `ell,p`, respectively, then the separations are

\[
 (3h+p)-(h+\ell-1)=2h+p-\ell+1\ge h+2,
\]

and

\[
 (2h+\ell)-(p-1)=2h+\ell-p+1\ge h+2.
\]

Here `1<=ell<=h` and `1<=p<=h-1`.  The two
excluded endpoints in (3.2) are only `h+1` positions apart.  Hence no reused
label can lie in both endpoints, so the correction term
`a_t cap a_(t+h+1)` acquires no new shared-bank coordinate.  Equation (3.3)
therefore remains exact.  This is the recursive algebraic/native-`q1`
normal form; it is **not** by itself a recursively resident normal form.

### Theorem 5.2 (sharp shared-bank residence horizon)

Start from a pairwise-disjoint packet at depth `h_0`.  After `t` deadline
jumps the depth is `h=h_0+t`.  For the labels `alpha_i,gamma_i` introduced
at jump `i` (`1<=i<=t`), their two source occurrences are separated by

\[
                         \Delta_i=3h_0+t+2i.           \tag{5.8}
\]

Consequently their two positive owner runs enclose one internal zero-gap of
length

\[
                g_i=\Delta_i-h-1=2h_0+2i-1.           \tag{5.9}
\]

Signed depth-`h` residence holds for this label exactly when

\[
                 g_i\ge h+1
       \quad\Longleftrightarrow\quad t\le h_0+2i-2.   \tag{5.10}
\]

Thus all shared labels are resident exactly through `t<=h_0`; at
`t=h_0+1` the oldest pair `alpha_1,gamma_1` fails.  Plateaux do not change
this ledger.  Changing the active enrichment indices does not change
`Delta_i` and cannot repair the gap.

The complete local owner traces are

\[
 \operatorname{tr}(\alpha_i)
   =0^{t-i}1^{h+1}0^{g_i}1^{t-i+1},\qquad
 \operatorname{tr}(\gamma_i)
   =1^{t-i+1}0^{g_i}1^{h+1}0^{t-i}.                  \tag{5.10a}
\]

#### Proof

At time `t`, `alpha_i` has within-bank indices
`t-i+1` in `Lambda` and `h_0-1+i` in `D^+`.  Reading their absolute source
positions from the four-block word gives separation `Delta_i`.  The same
calculation for `gamma_i`, at indices `t-i+1` in `D^-` and `h_0+i` in `P`,
gives the same value.  One source occurrence supports `h+1` consecutive
owner windows.  Since the two support intervals are disjoint, the number of
owners strictly between them is `Delta_i-h-1`, proving (5.9).  This gap is
internal.  Signed residence therefore gives (5.10), whose strongest row is
`i=1`.  A plateau changes neither block length nor either membership trace.
\(\square\)

For example, `h_0=2` first fails after three jumps, at depth `h=5`:

\[
 \operatorname{tr}(\alpha_1)=0^2 1^6 0^5 1^3,
 \qquad
 \operatorname{tr}(\gamma_1)=1^3 0^5 1^6 0^2.       \tag{5.10b}
\]

The bad `0^5` lies strictly inside the displayed packet, while signed
residence requires six.  Appending or prepending an exterior chronology
cannot alter it.  A full chronology can evade the obstruction only by not
retaining this packet contiguously--for example by removing one shared
occurrence or by an interior rethread.

### Corollary 5.3 (conditional optimal rebase cadence)

Suppose, as an additional black box, that at any depth `b` a literal rebase
can replace the current packet by a pairwise-disjoint packet with the same
exported owner/native/boundary state.  Then the latest safe next rebase is
after exactly `b` deadline jumps, at depth `2b`; delaying one more jump is
impossible for the unchanged packet.  Repeating at the latest safe times
gives rebase depths

\[
                         2b,4b,8b,\ldots.              \tag{5.10c}
\]

The scheduling state is one integer countdown `c=b-t` (equivalently the
oldest birth-depth slack `2H_min-2-h`).  This is a constant number of state
fields.  No bounded-support literal rebase is constructed here; therefore
(5.10c) is not a constant-additive-cost recurrence theorem.

If one instead postulates a rolling single-pair refresh, the unrefreshed
first-generation pair `i` expires at

\[
                          t_i=b+2i-1.                  \tag{5.10d}
\]

Thus the first service is forced before jump `b+1`, and thereafter one old
pair reaches its deadline every two jumps.  This is only a necessary service
calendar: no constant-support refresh preserving the owner/palette/compiler
interface is proved.

The inherited transition is exact locally but does not freeze arbitrary
compiler addresses: the new leading/trailing source letters shift physical
interval positions and create new mixed exterior rows.  Those are precisely
the global transport/cap hypotheses retained in Theorem 7.1; they do not
force a local repair-site reset.

The tag itinerary is

\[
 \alpha\gamma\longrightarrow\alpha\longrightarrow
 \varnothing\longrightarrow\gamma\longrightarrow
 \alpha\gamma.                                      \tag{5.11}
\]

The packet is therefore a literal four-sector connector.

## 6. Right boundary and terminal socket

Because the packet is the global word prefix, every left clipped run is a
global boundary run.  The exact packet/background de Bruijn state contains
the length-`h` word `omega_h` in (2.7).  At a jump its exact update is
(0.10).  If at least `H` further source letters follow and the resulting
cells belong to the declared owner chronology, those letters complete every
right-clipped **positive** run, including the new trailing `alpha`
occurrence.  This controls the packet's trailing positive runs; all later
source occurrences remain part of the global residence audit.

Zero-gap residence is separate.  If `y_1,y_2,...` are the continuation
letters, the exact nested exclusions exported by the sparse right collar
are

\[
 x_L\notin y_1,\qquad
 \rho_j\notin\bigcup_{t=1}^{j+1}y_t\quad(1\le j<h).   \tag{6.0}
\]

Call this family `Gamma_h`.  At a jump it is read with the child depth and
child `rho` list.  Equivalently one may export the corresponding right-gap
flags.  Thus `omega_h` alone is not the complete residence state.

Let

\[
                    \theta_h=(z_0,z_1,\ldots,z_{h+1}) \tag{6.1}
\]

be the last `h+2` source letters and suppose

\[
 O=\bigcup_{i=0}^{h}z_i,qquad
 a=\bigcup_{i=1}^{h+1}z_i,qquad a\subset O.          \tag{6.2}
\]

On a plateau replace every `z_i` by `z_i+beta`; this gives
`O+beta,a+beta`.  On a jump put

\[
                  \theta_H=(\{\alpha\},z_0,\ldots,z_{h+1}). \tag{6.3}
\]

The two order-`H` cells are

\[
 \{\alpha\}\cup z_0\cup\cdots\cup z_h=O+\alpha,
 \qquad
 z_0\cup\cdots\cup z_{h+1}=O\cup a=O.                \tag{6.4}
\]

This proves (0.6).  The split-core insertion transports the terminal
nonowner within one stage; this explicit `theta_h` socket is what regenerates
it across a plateau or jump.  It specifies only the last two derivative
cells.  The earlier cells crossing the start of `theta` belong to the global
exterior completion.  Every transformed terminal source letter and every
mixed row through it needs its own child cap/guard check.

For literal boundary words `v,u` of length `h`, direct reset cost is

\[
                         h-\operatorname{ov}(v,u),      \tag{6.5}
\]

where `ov` is longest suffix/prefix overlap.  Cost at most an absolute `c`
requires equality of `h-c` literal letters.  Clipped flag lengths alone do
not encode this.  The exact right state is the literal suffix `omega_h`
together with the nested zero-gap schedule `Gamma_h`.  It has boundedly many
structured objects, but their explicit descriptions grow with `h`.  The
whole packet residence state additionally carries the internal shared-label
birth ledger of Theorem 5.2; `Gamma_h` cannot repair those internal gaps.

## 7. What the local recurrence proves--and does not prove

For the triangular deadline, put

\[
 \tau_h={h+1\choose2},\qquad h'=h+\varepsilon,
 \qquad\varepsilon\in\{0,1\}.                         \tag{7.0}
\]

If

\[
 \sigma_m=hW+{h+1\choose2}-(4^{m-1}-1),                \tag{7.1}
\]

then, writing `W'={2r+1 choose r+1}`, the exact slack transition is

\[
 \sigma_{m+1}=4\sigma_m-h\operatorname{Cat}_r-3\tau_h-3
       +\varepsilon(W'+h+1).                          \tag{7.2}
\]

The exact plateau criterion is

\[
 \varepsilon=0\quad\Longleftrightarrow\quad
 4\sigma_m\ge h\operatorname{Cat}_r+3\tau_h+3.       \tag{7.3}
\]

The scalar lengths obey

\[
 4B(k)-B(k+2)=\operatorname{Cat}_r+3h-\varepsilon,   \tag{7.4}
\]

and therefore

\[
 4(B(k)+1)-(B(k+2)+1)
   =\operatorname{Cat}_r+3h+3-\varepsilon.            \tag{7.5}
\]

Thus four parent terminal slots do not by themselves canonically contract
to one child terminal slot.  The theorem below is a one-state local
transducer, not a scalar four-copy contraction theorem.

### Theorem 7.1 (conditional child insertion and state renewal)

Assume a **literal** child pre-insertion word of length `B(k+2)` such that:

1. it begins with the plateau or jump pre-packet above;
2. that prepacket contributes `2h'` rank-`r+1` owners and `h'`
   rank-`r+2` upper cells, while outside it are exactly
   `W'-3h'-1` further owners and the terminal cell from Section 6;
3. the eventual `W'` owners form a rooted upper-exact Hamilton path starting
   with the packet and ending at the prescribed terminal port;
4. its continuation accepts `omega_(h')` literally and satisfies the nested
   zero-gap schedule `Gamma_(h')`; and
5. every shared jump label satisfies its birth-depth inequality from
   Theorem 5.2, or the child word supplies an explicit residence
   compensation for its internal gap; and
6. every displayed packet, enrichment, continuation and terminal source
   letter passes its maximal cap, every mixed exterior row is admissible
   after insertion, every displaced singleton source target has a declared
   post-transition-admissible alternate occurrence cell-distinct from all
   other selected target occurrences, the ray/native equalities are charged
   once by target value, and all background targets have selected
   occurrences in one common ledger.

Then inserting `[X]` produces a length-`B(k+2)+1` state `S(r+1,h')` with
exactly one terminal nonowner, literal packet `q1` on both shores, no
packet-internal residence defect, and no old-interval OR loss at the
insertion.  Its repair-site state is `(j,s)` on a plateau and `(j+1,s)` on
a jump.

#### Proof

Equations (2.6), (4.2), and (5.4) give the packet rows.  The primed version
of (0.3) gives `W'` selected owners plus the one terminal cell.  The assumed
completion makes the owners the required path; Section 6 types its terminal
cell.  Section 3 makes every packet lower transition native and literal;
spanning source unions make every packet upper transition literal.
Monotone insertion preserves every preword interval OR because its adjacent
letters jointly contain `X`.  The literal boundary and cap hypotheses close
the remaining state rows.  \(\square\)

This is an exact **conditional child insertion lemma**.  It is not yet a
map from an arbitrary parent `S(r,h)` to a child state: the antecedent already
contains the child exterior owner path, background occurrences and common
cap.  What is genuinely recursive without further hypotheses is the local
owner/native-`q1` packet normal form (Sections 4--5), the terminal socket
(Section 6), and the algebraic no-reset repair-site map (0.9).  Signed
residence is recursive only up to the sharp horizon in Theorem 5.2.

The precise global missing theorem is therefore:

> From a parent state, build the child exterior completion accepting the
> prescribed `omega_(h')`, the protected packet prefix and terminal port,
> while transporting all deeper targets in one cap/guard ledger.

For an already host-equipped state **within the residence horizon**--in
particular, for a jump-born active pair with its permanent opposite-bank
backups and `t<=h_0`--the unresolved rows are only exterior rows:

1. an upper-exact rooted Hamilton owner-path completion containing the
   protected prefix and terminal port;
2. literal acceptance of `omega_(h')`, `Gamma_(h')`, and the transformed
   terminal socket (the exterior residence/boundary row); and
3. one common cap/guard and occurrence ledger transporting the old and deep
   targets through the Pascal sectors.

The local owner row, both packet `q1` palettes, native lower addresses,
repair-site evolution, and terminal two-cell type are no longer gates.  A
disjoint-bank base still needs initial hosts for its two displaced singleton
targets; that is part of the state antecedent, not supplied by `K2`.  Beyond
the sharp horizon, a fourth gate reappears: rebase or rethread the shared
bank to repair the internal signed zero-gaps.  Neither the inherited nor the
fresh repair-site choice alone does this.

No additional lower-`q1` packet sidecar is needed for such a host-equipped
state.  The same two enriched logical source letters persist; jump-born
alternate hosts persist internally, while barred-pair exterior hosts remain
part of the transport hypothesis.  The fresh jump coordinates have two
literal singleton occurrences each.  What remains is admission of every
transformed packet/terminal letter and every mixed exterior row into one
child cap/guard ledger.  This is a global old-target transport question,
not a local algebraic reset-existence question.

## 8. Comparison with the C8 bridge

The double-crossrail C8 theorem puts both zero-block cross banks in one
**local maximal-envelope source/cap state** and, after twelve isolated
edges are added, gives a thirteen-component protected forest with all
sixteen canonical upper support values.  It does not presently give:

1. a deletion/insertion identity of the form (2.6);
2. a same-parity map of its source boundary word;
3. a terminal-cell transducer of the form (0.6); or
4. an attachment of all thirteen components to one rooted upper-exact path
   preserving the exterior compiler.

It may become a background/cap actuator, but it is not yet a smaller
recursive state than the one-sided split-core packet.

## 9. Audit

The dependency-free replay

```text
scratch/audit_ad_split_core_one_sided_pascal_state_20260801.py
```

checks, for every `2<=h<=12`, all `(h-1)^2` two-position repair choices,
the final and pre-insertion rows, exact native lower cells, both palettes,
the plateau map, the inherited-site jump map, rays, one-step signed
residence, and
both terminal formulas.  It also replays six consecutive jumps for a barred
active pair and six more for a jump-born active pair, including the
paired-bank overlaps, their source-position separation, both pre-insertion
rank patterns, the four physical newborn singleton occurrences, and
permanent opposite-bank backups.  Crucially, it checks **signed** internal
runs and verifies the sharp residence horizon for every base depth
`2<=h_0<=12`: last legal jump `h_0`, first failure `h_0+1`, with oldest
gap `2h_0+1`.  Thus the audit intentionally refutes indefinite residence
closure.  It also checks a plateau after an accumulated shared-bank jump,
integrated-rank terminal examples, and the exact slack identities
(7.2)--(7.5) in 78 consecutive parameter cases.  Its formal label universe
does not test the
physical support inequality (1.2), global caps, the exterior Hamilton path,
or the common compiler.  The proof above is symbolic for all feasible
`h`; the finite replay is an independent formula audit.

The frozen output is

```text
scratch/ad_split_core_one_sided_pascal_state_20260801.audit.json
```

with payload SHA-256
`537b47a8da56535b0d4ae3574b611eaf836846a96cd6f311aef4880710ec6543`.
