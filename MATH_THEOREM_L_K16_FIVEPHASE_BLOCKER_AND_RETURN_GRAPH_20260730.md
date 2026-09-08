# K16 five-phase one-hole blocker criterion and exact return graph

**Date:** 2026-07-30  
**Status:** exact one-cell and complete sharp radius-three theorems; exact
support-56 CNF with scoped UNSAT solver evidence; no global length-12,874
claim

## 1. Frozen source

The authenticated literal word

```text
scratch/k16_fivephase_rex_hole20067.word
SHA-256 eef3555aa12675de8707de994d20300aaf8e96538b4691880810d84454fbb1b5
length 12874
```

has exactly one missing nonzero interval-OR target,

\[
 E=20067=\mathtt{0x4e63}.                                  \tag{1.1}
\]

Its final two cells are

\[
 W_{12872}=\mathtt{0x4e61},\qquad
 W_{12873}=H=\mathtt{0x287d}.                              \tag{1.2}
\]

The target \(H\) has the unique source witness `[12873,12873]`, and
`0x4e61` has the unique witness `[12872,12872]`.  This word is a coherent
five-phase annealing output, not a one-edit descendant of the append-`0200`
source; aligned byte comparison changes thousands of cells.  Arguments below
use only the authenticated bytes in (1.1).

## 2. Exact one-cell calculus

Let \(C_W(t)\) be the number of intervals of \(W\) having OR \(t\).  For
position \(p\), let \(D_p^W(t)\) count those intervals containing \(p\), and
let \(A_{p,x}^W(t)\) count the containing-\(p\) intervals after replacing
\(W_p\) by \(x\).  Then

\[
 C_{W[p\leftarrow x]}(t)
   =C_W(t)-D_p^W(t)+A_{p,x}^W(t).                           \tag{2.1}
\]

If \(c\) is the OR of a left suffix and right prefix around \(p\), then a
new containing-\(p\) interval has target \(t\) precisely when

\[
 c\subseteq t,qquad t\setminus c\subseteq x\subseteq t.   \tag{2.2}
\]

Thus (2.2), over all positions and all distinct contexts, enumerates every
arbitrary nonzero substitution which creates a specified target.  A target
can be lost only when all of its old witnesses contain \(p\); (2.1) then
tests exactly whether the new local labels replace it.  This is the complete
finite oracle used below.

## 3. The 128-terminal portal cube

The exact all-position census has `26,916` substitutions which create a
witness of \(E\).  None completes the word.  The collateral floor is one,
attained in exactly 128 rows, all at the terminal position:

\[
 W_{12873}=\mathtt{0x287d}\longmapsto x,\qquad
 x\in X:=\{\mathtt{0x0002}\vee q:q\subseteq\mathtt{0x4e61}\}. \tag{3.1}
\]

Here \(|X|=2^7=128\).  Every row in (3.1) creates \(E\) on
`[12872,12873]` and destroys only the unique terminal witness of \(H\).
Consequently every sharp state \(W_x\) has the sole hole

\[
                         H=\mathtt{0x287d}.                  \tag{3.2}
\]

This proves that the first one-hole label outside the old shuttle does not
itself give a one-cell completion: its sharp face enters the old \(H\)-phase.

## 4. Complete return graph from every sharp state

For each of all 128 states \(W_x\), the complete arbitrary substitution
census has exactly `26,783` rows which create \(H\), no completing row, and
collateral floor one.  Exactly 17 rows attain the floor:

1. the literal terminal return `p12873: x -> 0x287d`, which recreates sole
   hole \(E\);
2. the sixteen central rows

   \[
   p6439:\mathtt{0xa069}\longmapsto
   \ell\in L:=\{\mathtt{0x2004}\vee s:s\subseteq\mathtt{0x0069}\}, \tag{4.1}
   \]

   each of which leaves the sole hole

   \[
                         A=\mathtt{0xa879}.                  \tag{4.2}
   \]

The minimum routing pattern is uniform over all \(x\in X\), although the
higher-collateral histogram depends slightly on the terminal singleton
label.  There are `128` return edges to the \(E\)-state and
`128*16=2,048` sharp central transfers to \(A\)-states.  In particular:

> **Theorem 4.1 (sharp-first radius-two no-go).** No universal word obtained
> by two substitutions from the frozen source can have its first edit in
> the sharp portal cube (3.1).

This does not exclude the 42 collateral-two first service rows, any larger
first spill, or a synergistic pair for which neither edit alone creates
\(E\).

### Theorem 4.2 (complete sharp third layer)

For every \((x,\ell)\in X\times L\), perform both sharp edits from the
source.  Each of the `128*16=2,048` resulting literal states has sole hole
\(A\).  Its complete one-cell census has `27,926` rows which create \(A\),
no completion, collateral floor one, and exactly 17 minimizers:

1. sixteen central returns

   \[
   p6439:\ell\longmapsto z,\qquad
   z\in Z:=\{\mathtt{0xa000}\vee s:s\subseteq\mathtt{0x0069}\}, \tag{4.3}
   \]

   each reopening sole hole \(H\);
2. the terminal move `p12873: x -> 0xa879`, which reopens sole hole \(E\).

Thus the complete authenticated sharp-service fibre has label transitions

\[
                  E\longrightarrow H\longrightarrow A
                    \longrightarrow\{H,E\},               \tag{4.4}
\]

with no zero and no fourth one-hole label through this layer.  The exact
aggregate is

```text
scratch/k16_fivephase_radius3_sharp_fibre_exact_20260730.audit.json
SHA b164a2067d03fc968659ba89bf9c41b3fae242d81bbecb865651944b33efb629
```

There is also a solver-free two-port obstruction.  If every cell except
`p6439,p12873` is frozen, arbitrary nonzero values at those two ports cannot
cover \(E,H,A\) simultaneously.  An \(E\)-witness through the terminal
crosses fixed `0x4e61`, so the terminal cannot simultaneously supply \(H\)
or \(A\); the central port would then have to supply both, but \(H\) requires
bit `0x0004` and forbids `0x8000`, whereas \(A\) has the opposite
requirements.  If \(E\) is instead supplied through the central port, its
only contained side-context is empty, forcing the central value to equal
\(E\); the terminal would have to equal both \(H\) and \(A\).  Intervals
meeting both ports cross fixed OR `0xffff` and cannot witness a proper
target.

## 5. The named-blocker equivalence

The following criterion is independent of K16.

### Lemma 5.1 (portal blocker criterion, with compatibility)

Let a word \(V\) have sole hole \(E\), and let \(P\) replace the cell at
\(p\).  Suppose \(U=P(V)\) has sole hole \(H\).  For any packet \(R\) whose
support avoids \(p\),

\[
                         P(R(V))=R(U).                       \tag{5.1}
\]

Consequently, if \(R\) is **post-portal safe**, meaning

\[
             C_{R(U)}(t)>0\qquad(t\ne H),                   \tag{5.2}
\]

then \(R(U)\) is universal if and only if \(C_{R(U)}(H)>0\).
Equivalently in the pre-portal word, it is sufficient that:

1. the portal's \(E\)-witness survives \(R\);
2. every \(t\ne E,H\) has after \(R\) a witness that survives \(P\); and
3. \(R(V)\) has an \(H\)-witness avoiding \(p\).

Under these three conditions, applying \(P\) is universal.

#### Proof

The two packets have disjoint supports, so (5.1) holds literally.  Condition
(5.2) says that only \(H\) can be absent from \(R(U)\), proving the first
assertion.  The three pre-portal conditions respectively preserve \(E\),
all targets other than \(E,H\), and \(H\) after applying \(P\). \(\square\)

The post-portal safety clause is essential.  Merely keeping the pre-portal
word hole-free away from \(E\) does not prevent an outside edit from deleting
the last portal-surviving witness of a third target.  Every finite claim
below therefore uses exact combined-word replay, not the named witness alone.

For the source (1.1), \(p=12873\), \(H=0x287d\), and every \(x\in X\)
is such a portal.  Hence the exact constructive objective, with post-portal
safety retained, is:

\[
 \text{create one nonterminal }0x287d\text{ witness while preserving all
 current coverage}.                                         \tag{5.3}
\]

The global one-cell blocker census enumerates every nonterminal position and
every arbitrary value which creates \(H\).  It has `27,036` service rows and
no coverage-safe row.  Its collateral floor is one, attained exactly by the
sixteen central rows (4.1), all losing only \(A=0xa879\).  Thus (5.3) cannot
be paid by one additional cell; its nearest realization is the named chain

\[
                    E\longrightarrow H\longrightarrow A.   \tag{5.4}
\]

The same lemma explains the append-phase latch: a second
`0xa879` witness avoiding its central portal would make any of the sixteen
`0x287d` portals debt-free.  The useful search objective is therefore a
named avoiding witness, not aggregate singleton reduction.

A deeper representative-packet census is also exact.  Fix the canonical
terminal portal `p12873 <- 0x4e63`.  There are 500 one-cell external
fortifications which create an avoiding \(H\)-witness and leave at most five
literal holes, with debt histogram

\[
                  1^{16},\ 2^{136},\ 3^1,\ 4^{313},\ 5^{34}. \tag{5.5}
\]

After every such fortification, every arbitrary one-cell substitution able
to cover all current holes was evaluated by the common-submask oracle.  The
batch checks 912,277,388 assignments and 1,001,631 compatible returns, finds
no completion, and its 23,019 minimum pairs return only to \(H\) (23,003
times) or \(E\) (16 terminal backtracks).  This closes the declared
canonical-portal/debt-at-most-five pair fibre, not fortifications with six or
more debts or cooperative pairs in which neither edit alone supplies the
avoiding witness.

## 6. Exact named-witness support and weighted Hall pricing

The blocker criterion admits a complete support oracle before any search.
Let \(U\) be a word in which the proper target \(H\) is absent.  For a
nonempty cyclic interval \(I\), define its set of \(H\)-bad cells by

\[
 B_H(I)=\{i\in I:U_i\not\subseteq H\}.                     \tag{6.1}
\]

### Lemma 6.1 (forced support of a new blocker witness)

The minimum number of arbitrary nonzero substitutions inside \(I\) needed
to make \(\bigvee_{i\in I}U_i=H\) is

\[
 r_H(I)=
 \begin{cases}
 |B_H(I)|,&B_H(I)\ne\varnothing,\\
 1,&B_H(I)=\varnothing.
 \end{cases}                                                \tag{6.2}
\]

Moreover every realizing packet must edit every cell in \(B_H(I)\).

#### Proof

Any unedited cell not contained in \(H\) makes the final interval OR exceed
\(H\), proving necessity.  If \(B_H(I)\ne\varnothing\), change every bad
cell to a nonzero submask of \(H\), choosing one of them to equal \(H\).
This uses exactly \(|B_H(I)|\) changes and makes the OR equal \(H\).  If
\(B_H(I)=\varnothing\), the old OR is a strict submask of \(H\), since \(H\)
is absent.  Changing any cell of \(I\) to \(H\) is one actual substitution
and suffices. \(\square\)

Thus a budget-\(r\) blocker search need inspect only intervals having at most
\(r\) bad cells.  This is a named-target enumeration, not a search over all
hole labels.

For exact preservation, let \(S\) be the packet support and \(y\) its final
values.  Write \(D_S^U(t)\) for the number of old \(t\)-intervals meeting
\(S\), and \(A_{S,y}^U(t)\) for the number of final \(t\)-intervals meeting
\(S\).  Then the multi-cell identity

\[
 C_{U[S\leftarrow y]}(t)
   =C_U(t)-D_S^U(t)+A_{S,y}^U(t)                            \tag{6.3}
\]

is exact.  Notice that \(D_S\) counts the union of affected intervals, not
the sum of the one-cell deletion ledgers.  Put

\[
 \delta_{S,y}(t)=A_{S,y}^U(t)-D_S^U(t),\qquad
 s_t=C_U(t)-1\quad(t\ne H).                                \tag{6.4}
\]

Since \(C_U(H)=0\), the packet completes the portal state exactly when

\[
 \delta_{S,y}(H)\ge1,\qquad
 \delta_{S,y}(t)\ge-s_t\quad(t\ne H).                      \tag{6.5}
\]

This retains multiplicities and is strictly sharper than merely counting
singleton targets.

There is also an exact Hall-type relaxation for separated packet catalogues.
Let \(\Omega=2^{16}-1\).  Suppose \(S_1,\ldots,S_r\) are disjoint collars
such that every cyclic interval meeting two collars contains an unchanged
subinterval of OR \(\Omega\).  At collar \(j\), let \({\cal C}_j\) be a
finite catalogue of literal choices, including the identity, and let
\(\delta_c(t)\) be the exact ledger of choice \(c\).  A cross-collar
interval has label \(\Omega\) both before and after every catalogue choice;
its contribution to every delta is therefore zero.  Hence every target
ledger is the sum of the collar ledgers.

### Theorem 6.2 (separated-collar compiler ILP and Hall dual)

Within these catalogues, a literal completion exists if and only if there
are \(x_c\in\{0,1\}\) satisfying

\[
 \sum_{c\in{\cal C}_j}x_c=1\quad(1\le j\le r),             \tag{6.6}
\]

\[
 \sum_c\delta_c(H)x_c\ge1,\qquad
 \sum_c\delta_c(t)x_c\ge-s_t
       \quad(1\le t\le\Omega,\ t\ne H).                    \tag{6.7}
\]

The same system with \(x_c\ge0\) is the exact fractional packet relaxation.
It is feasible if and only if, for every nonnegative target weighting
\(y=(y_t)_{1\le t\le\Omega}\),

\[
 \sum_{j=1}^r\max_{c\in{\cal C}_j}
       \sum_{1\le t\le\Omega}y_t\delta_c(t)
 \ \ge\ y_H-\sum_{t\ne H}y_ts_t.                          \tag{6.8}
\]

#### Proof

The full-OR separator makes all proper-target deltas additive, so (6.6)--
(6.7) are precisely (6.5) plus one literal choice per collar.  For the
fractional claim, the achievable delta vectors form the Minkowski sum
\(K=\sum_j\operatorname{conv}\{\delta_c:c\in{\cal C}_j\}\).  Feasibility is
\(K\cap(b+\mathbb R_{\ge0}^{\Omega})\ne\varnothing\), where
\(b_H=1\) and \(b_t=-s_t\) otherwise.  If the sets are disjoint, a separating
normal must be nonnegative because the second set is upward closed.  Its
support function on \(K\) is the left side of (6.8), and its infimum on the
second set is the right side.  This proves both directions. \(\square\)

Because every catalogue contains the identity, a violating weight has
\(y_H>0\); normalize it to \(y_H=1\).  The exact reduced-price score of a
choice is then

\[
 \delta_c(H)+\sum_{t\ne H}y_t\delta_c(t),                 \tag{6.9}
\]

and (6.8) is the useful weighted Hall separator.  It prices creation of the
one named blocker against the actual witness slack it consumes.  Passing all
such rows proves only fractional feasibility; the integral catalogue system
and literal replay remain necessary.

For interacting packets outside the separated-collar hypothesis, the
proof-safe annealing objective is the lexicographic pair

\[
 \left(
   \max\{0,1-\delta(H)\},
   \sum_{t\ne H}\max\{0,-s_t-\delta(t)\}
 \right).                                                   \tag{6.10}
\]

Its second coordinate is exactly the number of collateral holes after the
named blocker is supplied.  A purported zero still requires complete
physical replay; (6.10) is not an additive surrogate when collars interact.

## 7. Exact support-56 budget-two CNF

Let \(S_{55}\) be the union of every physical interval witnessing one of the
16 Hamming-distance-one neighbours of \(E\).  The exact census gives 20
provider intervals on 55 positions.  Put

\[
                         S=S_{55}\cup\{12873\},\qquad |S|=56. \tag{7.1}
\]

This support is a focused physical catalogue, not a theorem that all
multi-cell repairs lie in \(S\).

For arbitrary nonzero final values on \(S\), the dynamic CNF is exact for
**exactly two** actual substitutions.  Targets having an interval wholly in
a fixed run survive automatically.  Every other interval meets \(S\) in a
nonempty consecutive block of editable positions.  For each such block, the
encoder lists every fixed suffix/full-gap/prefix OR base \(b\).  A witness of
target \(t\) is equivalent to

\[
 b\subseteq t,qquad x_i\subseteq t\ (i\text{ in the block}),qquad
 t\setminus b\subseteq\bigvee_i x_i.                         \tag{7.2}
\]

The CNF encodes (7.2), nonempty cells, change-bit equivalence, and an exact
cardinality-two prefix counter.  Therefore it is SAT if and only if some
literal word obtained by exactly two substitutions inside \(S\) is
universal.

The frozen instance has

```text
52,299 variables
1,355,933 clauses
3,253,396 literals
314 nonautomatic targets
51,182 witness terms.
```

Kissat 4.0.4 returned `UNSATISFIABLE` in 27.36 seconds using 70,680 KiB RSS.
The initial run emitted no proof.  A later proof-producing rerun emitted a
50 MiB ASCII DRAT trace and returned UNSAT again; bounded `drat-trim` checks
had not produced `s VERIFIED` at the time this note was frozen.  Accordingly
the current formal status is:

> **Solver verdict 7.3.** Exact-two substitutions inside the fixed support
> \(S\) are solver-UNSAT.  This is exact solver evidence but not yet a checked
> UNSAT theorem.  It says nothing about positions outside \(S\), other edit
> budgets, or global radius two.

## 8. Reproducible artifacts

```text
scratch/audit_l_k16_fivephase_onehole_census_20260730.py
  SHA 4d6578d02f7c1883798786d483722309d631974b2b5c39a17098a65e944c9c58
scratch/k16_fivephase_onehole_census_20260730.audit.json
  SHA f58530463096029724da981522356b8d23d610e8b256d58b52cd1ae429b73a29
  payload 4dbd9f4e75ab161014090e6e5745e95630769608466fbd3485da0cf6a4cb2d19

scratch/audit_l_k16_fivephase_return_graph_20260730.py
  SHA 1a995733c9157a294a053c79bb9b47a65bd2b2ffd7845b565f3248a47597619c
scratch/k16_fivephase_return_graph_20260730.audit.json
  SHA 3948e904d00ac17024277a0e7010de90ebf70a07e3c3cf00a14a257886962d95
  payload 32adfea4fe0b24604402b14ebdc7370f83ce46c4b6f835cafe5e1d10cde807c3

scratch/k16_fivephase_radius3_sharp_fibre_exact_20260730.audit.json
  SHA b164a2067d03fc968659ba89bf9c41b3fae242d81bbecb865651944b33efb629

scratch/threadD_k16_fivephase_external_low5_pair_census_20260730.audit.json
  SHA f03e64eb3fba95fc15c1f64d76a444c9917e3aa89e8c27095e2a88f06e5a42a8
  payload b6184a5cda95a01b2d513910bbba37865fe3c21b4a1e647321267563b42dc4c7

scratch/audit_l_k16_fivephase_named_blocker_20260730.py
  SHA 4bf5c686c24bc9d47665d94eb4f2157f70a65ed28ada5d4fda5093a868f01837
scratch/k16_fivephase_named_blocker_20260730.audit.json
  SHA d19f4415031b0db44bd3faaed011b609c79b1fab1c53e958f4bcce577179fd19
  payload f0a9b7425cd3092d87848d03a15011a6d5ce85f1aac3879be6a5c299cab32c3b

scratch/audit_l_k16_fivephase_support56_b2_solver_20260730.py
  SHA a460c15dd5e34ba644dbf863f68d8ffc98afe538eaf330d2af84cdc9c9fc9323
scratch/k16_fivephase_support56_b2_20260730.audit.json
  SHA e1905567ec279e001764fe4a3a672998a5b44037586e87dad8eeb8a18367e19e
  payload 676673cc2a81854ac52a184eb20df4c2c53248c88e144ad066ecb04e044f9d99

scratch/k16_fivephase_support56_b2_20260730/
  binary a80d081a982a61236b42743592aaf4abc69cde865c7bf59a8a6b9a449a9c4b4d
  CNF    de673c90ed5713263c3d60546ee2c7d9e0607641a3b463b79e1f58804e3f75a6
  map    8662d5199352f3023e7e1dbb56769aea1351ebd152926e11a09183d5d0322514
  solve  bde6e1eede96772c07c8ce29fd18088863815bd043aa59a06f11f5838cf8a162
  DRAT   eda96cfe6f7a1987a87ca0264da1f9f1199d62c7923f5a6e25efe46289be62df
  longest checker resource log
         9670c0d5699a8c666e1dc9b9fc06c07d9449b39b0a4b2afea4c4c9dcabb2cf63
```

Every claimed minimum row in the Python ledgers is independently materialized
and replayed on all 65,535 nonzero masks.  No completion artifact was emitted.

## 9. Exact remaining boundary

The strongest proved constructive target is now a compound version of
(5.3): create a nonterminal \(H\)-witness while retaining \(A\), or first
create an avoiding \(A\)-witness and then use the central \(H\)-blocker.
Lemma 6.1 gives the complete interval-support catalogue, while Theorem 6.2
gives the exact separated-collar ILP and its fractional Hall pricing oracle.
The entire sharp radius-three fibre and the unrestricted two-port fibre are
closed, so this packet must recruit at least one outside coordinate.
The support-56 budget-two face is closed only at solver-evidence level.
Edits outside that support, higher edit budgets, the 42 collateral-two direct
\(E\)-services, and joint-only \(E\)-witnesses remain open.  The global
bracket remains

\[
                         12873\le\nu(16)\le12875.             \tag{8.1}
\]
