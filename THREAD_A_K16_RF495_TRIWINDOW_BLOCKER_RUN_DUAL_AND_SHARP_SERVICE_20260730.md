# RF495 tri-window: exact blocker-run dual and sharp three-port service

**Date:** 2026-07-30  
**Lane:** A  
**Status:** exact source-relative theorems and construction; the full
nonmonotone tri-window completion remains open

## 1. Verdict and frozen scope

Let `P` be the repeat-free K15 parent

```text
scratch/k15_repeatfree_parents_20260730/K15_REPEATFREE_SEED.word
SHA-256 4e9afded73e1ebad4c53408839e755e15e89ce0ed7888cf788c6db1a92bf2ca6
```

and form the length-12,873 RF495 word

\[
 [c_0,c_1,c_2,c_3]\;P[6:6436]\;
 [c_4,\ldots,c_{12}]\;
 (0x8000\mathbin\lor P[7:6432])\;
 [c_{13},\ldots,c_{17}].                 \tag{1.1}
\]

The editable physical positions are

\[
 Q=[0,3]\cup[6434,6442]\cup[12868,12872].             \tag{1.2}
\]

The frozen free cells are

```text
j       0     1     2     3 |    4     5     6     7     8     9    10    11    12 |   13    14    15    16    17
c_j 18e6  1846  1986  3186 | 1e40  8000  1460  0863  1866  9846  9886  9182  b104 | 8b42  9b00  0a50  0a44  1e20
```

They are frozen in

```text
scratch/k16_rf495_triwindow_score3_20260730.cells
SHA-256 6f90ca3f682ad1565977d53f0d3a30496ae01f38a7816f411375e5f6b415745c

scratch/k16_rf495_triwindow_score3_20260730.word
SHA-256 9771f928d2a405308eabbbc780a2f810f77d8faef4f10d56cbb4e50381f518d6
```

Exact compressed ending-OR replay gives precisely three holes

\[
 H=\{A,B,C\}
  =\{0x18e7,0x3de7,0x9e20\}.                         \tag{1.3}
\]

The results of this note are as follows.

1. The unrestricted RF495 completion problem has an exact order-sensitive
   blocker-run formulation on 70 targets and 395 literal interval classes.
   It includes all protected old labels, not only the three holes.
2. Merely making all three members of `H` occur requires at least three
   changed free cells.
3. Three changes suffice for this service problem, and an explicit sharp
   service macro is given below.  It leaves exactly twelve protected debts.
4. The independently authenticated active-kernel recurrence applied to the
   exact blocker criterion excludes every support of size at most three.
   Thus a full RF495 completion changes at least four cells.
5. No coordinatewise bit-addition surgery, of any support size, completes
   RF495.  Every completion must delete at least one incumbent one-bit.

This does **not** prove that arbitrary reassignment of the 18 free cells is
impossible, and the displayed service macro is not a universal word.

## 2. Exact body complement and locality

Put

\[
 L=P[6:6436],\qquad
 U=0x8000\mathbin\lor P[7:6432].
\]

Their lengths are 6,430 and 6,425.  Direct OR gives

\[
 \bigvee L=0x7fff,\qquad \bigvee U=0xffff.             \tag{2.1}
\]

The shortest saturating prefix/suffix lengths are respectively

\[
 (11,19)\quad\hbox{for }L,qquad (13,20)\quad\hbox{for }U.   \tag{2.2}
\]

Let `R` be the nonzero masks having no interval witness wholly inside either
fixed body.  The exact ending-OR recurrence gives

\[
 |R|=70.                                                \tag{2.3}
\]

Every target outside `R` remains covered under every reassignment of `Q`.
Conversely every witness for a member of `R` meets `Q`.  Such a witness
cannot meet two of the three free windows: crossing the first fixed body
contains all of `L`, while crossing the second contains all of `U`; the
resulting saturated label is already a fixed-body label, not a member of
`R`.  Hence every relevant witness is local to exactly one of the three
windows.

By (2.2), fixed extension radius 20 already captures every relevant interval
class.  Collapsing intervals by their fixed OR and their set of free cells
gives exactly 395 classes; radius 40 gives the same catalogue.  This proves
that the following theorem is literal, not a truncated-collar relaxation.
Exactly 227 of the 395 classes are legal for at least one member of `R`; the
other 168 are retained generic geometry rows but cannot host a residual
target.

For reference, the 70-target source multiplicity histogram is

```text
0^3  1^60  2^6  3^1.
```

The three zeroes are exactly (1.3).

## 3. Protected-label interval dual

The host-intersection equivalence itself is the fixed-support specialization
of the already-audited arbitrary-collar core gate.  It is restated here to
make the RF495 protected-label and blocker-run quantifiers explicit; it is
not claimed as a second independent discovery of that abstract lemma.

Fix a permitted edit set \(E\subseteq Q\); values outside `E` remain those of
the frozen word `w`.  Let

\[
 D_E=\{T\in R\setminus H:\text{ every old witness for }T\text{ meets }E\}
\]

and put

\[
 \mathcal R_E=H\cup D_E.                               \tag{3.1}
\]

These, and only these, are the at-risk labels that must be rehosted.

For every literal interval \(J\) meeting `E`, define

\[
 S_E(J)=J\cap E,qquad
 F_E(J)=\bigvee_{i\in J\setminus E}w_i.                \tag{3.2}
\]

Two intervals are in one *class* when their pairs `(S_E,F_E)` agree.  For
\(T\in\mathcal R_E\), define

\[
 \mathcal C_E(T)=
 \{(S,F): (S,F)=(S_E(J),F_E(J))\text{ for some }J, F\subseteq T\}.
                                                               \tag{3.3}
\]

### Theorem 3.1 (exact fixed-support blocker-run criterion)

There is a universal RF495 assignment whose change support is contained in
`E` if and only if one can choose pairwise distinct classes

\[
 c_T=(S_T,F_T)\in\mathcal C_E(T),qquad T\in\mathcal R_E,       \tag{3.4}
\]

such that, on putting

\[
 K_p=\bigcap_{T:p\in S_T}T,                                  \tag{3.5}
\]

the following conditions hold:

\[
 K_p\ne\varnothing\quad\text{for every used }p,               \tag{3.6}
\]

and

\[
 F_T\mathbin\lor\bigvee_{p\in S_T}K_p=T
       \quad\text{for every }T\in\mathcal R_E.                \tag{3.7}
\]

In particular every completion obeys all ordinary Hall cuts

\[
 |X|\le
 \left|\bigcup_{T\in X}\mathcal C_E(T)\right|
       \quad(X\subseteq\mathcal R_E).                          \tag{3.8}
\]

**Proof.**  A new witness of a member of \(\mathcal R_E\) must meet `E`:
otherwise its OR is unchanged, contradicting either that it was originally
missing or that every old witness meets `E`.  Distinct target labels cannot
use the same class, because a fixed assignment gives every interval in one
class the same OR.  This proves (3.4) and (3.8).

Suppose replacement masks \(x_p\) realize chosen witnesses.  Whenever
\(p\in S_T\), the interval OR `T` forces \(x_p\subseteq T\); hence
\(x_p\subseteq K_p\).  The realized equality

\[
 F_T\mathbin\lor\bigvee_{p\in S_T}x_p=T
\]

and \(K_p\subseteq T\) then imply (3.6)--(3.7).

Conversely, assign \(x_p=K_p\) at every used position and leave unused
positions unchanged.  Conditions (3.6)--(3.7) make every selected interval
an exact witness.  Every target outside \(\mathcal R_E\) retains an old witness
disjoint from `E`, and every target outside `R` retains a fixed-body witness.
Thus the word is universal.  QED.

The higher-order run form is especially transparent.  For each coordinate
`b`, define the blocker set

\[
 B_b=\bigcup_{T:b\notin T}S_T.                                \tag{3.9}
\]

Then \(b\in K_p\) exactly when \(p\notin B_b\).  Therefore (3.6)--(3.7) are
equivalent to

\[
 \begin{split}
 &\text{every used }p\text{ lies outside }B_b
      \text{ for at least one }b,\\
 &S_T\setminus B_b\ne\varnothing
      \quad\text{for every }b\in T\setminus F_T.
 \end{split}                                                  \tag{3.10}
\]

Each `S_T` is a literal consecutive block inside one of the `4,9,5`
windows, so each `B_b` is a union of selected runs.  Equation (3.10) is the
order-sensitive part discarded by independent Hall or marginal balancing.
For \(E=Q\), one has \(\mathcal R_Q=R\), so Theorem 3.1 is an exact
necessary-and-sufficient formulation of unrestricted RF495 completion.

### Corollary 3.2 (authenticated support-four floor)

No universal assignment differs from the RF495 source at at most three
positions of `Q`.

**Proof.**  For a fixed support `E`, aggregate selected classes with the same
nonempty incidence set `S`.  Put

\[
 U_p=\bigcap_{T:p\in S_T}T,
 \qquad
 R_S=\bigvee_{T:S_T=S}(T\setminus F_T).                       \tag{3.11}
\]

Theorem 3.1 is equivalently

\[
 U_p\ne0,qquad
 R_S\subseteq\bigvee_{p\in S}U_p
       \quad(\varnothing\ne S\subseteq E).                    \tag{3.12}
\]

Intersections in (3.11) only shrink and required unions only grow as targets
are inserted.  Thus a failed partial state can never recover.  The frozen
active-kernel recurrence checks exactly the state

\[
 (U_p:p\in E;\ R_S:\varnothing\ne S\subseteq E)
\]

for all `18+153+816` supports of sizes one, two and three.  Its maximum live
state counts are respectively `2,5,34`, and every terminal state set is
empty.  By (3.12), this is an exact Boolean-lattice proof, not a SAT,
stochastic, or marginal relaxation.  The independently replayed theorem and
catalogue are

```text
MATH_THEOREM_K16_RF495_TRIWINDOW_ACTIVE_KERNEL_SUPPORT3_NOGO_20260730.md
SHA-256 16fd16c7f44a97f2488cb91f3287236cd05ea57700d43be5018741f6351f3303

scratch/k16_rf495_triwindow_provider_kernel_20260730.audit.json
SHA-256 9977f324091c662e50c88e98122421ca1d28c819c3045fcf5588359419447486

scratch/k16_rf495_triwindow_exact_form_quotient_20260730.catalogue.json
SHA-256 63bac356c732a6097d8472445cfeb01bcedae6d13098eaf39d6ced8df3862943
```

Therefore any completion inside the 18-cell fibre changes at least four
cells.  QED.

## 4. A one-port lower-pair obstruction

Write

\[
 A=0x18e7\subset B=0x3de7,qquad B\setminus A=0x2500.          \tag{4.1}
\]

The three extension coordinates in \(B\setminus A\) are bits 8, 10 and 13.

### Lemma 4.1

With the other 17 free cells fixed, no replacement of one free cell can
create both `A` and `B`.

**Proof.**  Since `A` is absent initially, its new witness contains the
changed cell `p`; its replacement value is therefore a submask of `A`.
Consequently a `B`-witness through the same cell must obtain all of
`0x2500` from the unchanged `B`-compatible component around `p`.

Deleting `p` and extending left and right until the first incumbent cell not
contained in `B` gives the following complete table.  Indices are the free
indices `j` from Section 1.

```text
j                         available part of 0x2500
0,1,2,3                   0x2100
5,7,8,9                   0x0400
4,6,10,11,12,13,14,15,16,17
                          0x0000
```

No row supplies `0x2500`.  QED.

## 5. Sharp three-port service theorem

### Theorem 5.1

Every reassignment of the RF495 free cells in which all three masks
`A,B,C` occur changes at least three cells.

**Proof.**  The four fixed cells immediately outside the three free windows
are

\[
 0x3104,\quad0x0004,\quad0xb088,\quad0x8a4a.                   \tag{5.1}
\]

Their parts outside `C=0x9e20` are respectively

\[
 0x2104,\quad0x0004,\quad0x2088,\quad0x004a,                  \tag{5.2}
\]

all nonzero.  Thus a new `C`-witness lies wholly in one free window.

If bit 15 of `C` is supplied by an edited cell `e`, that cell cannot occur
in an `A`- or `B`-witness, because both lower masks omit bit 15.  If bit 15
is unchanged, the only incumbent `C`-compatible high cell in a free window
is `c_5=0x8000`.  Its window has no unchanged compatible source of bit 9,
so an edited cell `e` must supply bit 9; again `e` cannot occur in an `A`-
or `B`-witness.  Hence at least one edit is exclusive to `C`.

With at most two edits, only one edit remains available to the two lower
holes.  The `C`-exclusive edit carries bit 9 or bit 15 and is therefore
incompatible with both lower targets.  Relative to the one-port table it
either leaves an incumbent blocker in place or turns an incumbent clean cell
into a blocker; it cannot enlarge the unchanged `B`-compatible component of
the sole lower edit.  Since both lower masks were initially absent, that
sole edit would have to create both, contrary to Lemma 4.1.  QED.

The bound is sharp for service.  Make the three changes

\[
 \begin{array}{rcl}
 w_0&:&0x18e6\longmapsto0x18e7,\\
 w_2&:&0x1986\longmapsto0x1d86,\\
 w_{12872}&:&0x1e20\longmapsto0x9e20.
 \end{array}                                                  \tag{5.3}
\]

Then

\[
 \bigvee[0,0]=0x18e7,qquad
 \bigvee[0,3]=0x3de7,qquad
 \bigvee[12872,12872]=0x9e20.                                \tag{5.4}
\]

The materialized word is

```text
scratch/k16_rf495_triwindow_threehole_service3_20260730.word
SHA-256 2adc27595d03b4cff964760dbc3c1dc9bfccd922929eeaab2fc0e30764c37143
```

Exact replay leaves precisely the twelve debts

\[
 \begin{gathered}
 0x18e6,0x1986,0x19c6,0x19e6,0x1e20,0x1e64,0x1e74,\\
 0x3986,0x398e,0x39c6,0x39e6,0x3bde.
 \end{gathered}                                                \tag{5.5}
\]

Thus (5.3) is a sharp hole-service macro, not a completion.

## 6. All-support monotone no-go

### Theorem 6.1

No RF495 completion can be obtained solely by adding bits to free cells.
Equivalently, every completion deletes at least one incumbent one-bit.

**Proof.**  Under coordinatewise additions, a new interval with OR `C`
must have had old OR contained in `C`.  Inspecting the three free windows
and the four dirty boundary cells (5.1), the only old intervals meeting `Q`
whose OR is contained in `C` are

\[
 [6435,6435]=0x8000,qquad [12872,12872]=0x1e20.                \tag{6.1}
\]

So a new `C` witness upgrades one of these two singletons to `C`.

The first singleton is also the only old interval meeting `Q` whose OR is
contained in `0x8000`; the second is the only one whose OR is contained in
`0x1e20`.  After the corresponding upgrade, monotone changes cannot create
a new witness for the displaced target `0x8000` or `0x1e20`, respectively.
Both targets lie in `R`, so no fixed-body witness exists.  Universality is
impossible.  QED.

## 7. One protected support-three branch

The blocker mechanism already closes one natural sharp-support branch.

If `w_6434` is changed from `0x1e40` to `0x1e20`, then
`[6434,6435]` realizes `C` but the unique target `0x1e40` is lost.
After this edit, no unchanged cell in a free-window corridor is both a
submask of `0x1e40` and a carrier of bit 9; the four fixed boundary cells are
dirty for this target.  Thus any new `0x1e40` witness needs another edited
cell whose new value carries bit 9.  Such a cell cannot serve `A` or `B`.
Only one lower edit remains, contradicting Lemma 4.1.

This is a genuine protected-label exclusion, not a service-only argument.
It does not exhaust singleton-`C` placements or witnesses using several
edited cells.  In particular, no analogous claim is made for the terminal
route: a separate edit can combine the fixed `0x0004`, incumbent `0x1e40`,
and a new `0x0020` to rehost `0x1e64`, so the naive exclusive-bit argument
there is invalid.

## 8. Exact remaining gate

The full RF495 question is now the following finite mathematical statement,
with no marginal ambiguity:

> Choose one legal class for each of the 70 targets from the complete
> 395-class catalogue (227 classes are residual-relevant), so that the
> choices are injective and satisfy the sixteen blocker-run conditions
> (3.10).

A deficient target family in (3.8) is an immediate interval-Farkas
certificate.  If Hall holds, a no-go must show that every injection violates
some blocker demand in (3.10).  Conversely one injection satisfying (3.10)
constructs the free cells by (3.5) and gives a literal universal word.

Corollary 3.2 and Theorem 6.1 show that any such construction is a genuinely
nonmonotone exchange on at least four cells and must rehost an old protected
witness bank.  This is the precise proved/conditional boundary; no
unrestricted K16 conclusion is claimed.
