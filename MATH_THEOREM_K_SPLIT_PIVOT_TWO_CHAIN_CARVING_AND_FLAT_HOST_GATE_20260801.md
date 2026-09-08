# Split-pivot insertion carves both coatom chains, but a flat host pays a linear plateau

Date: 2026-08-01  
Lane: K, additive-one mixed-coatom compiler repair  
Status: exact all-width insertion theorem, exact two-chain label
characterization, explicit all-`d` split socket, and a linear flat-host
obstruction.  The result gives a conditional one-position terminal theorem
(and gives `B(k)+1` only when the reference word has length `B(k)`).  It does
not construct the required nonflat Pascal host.

## 0. Verdict

Let `A=(A_0,...,A_(N-1))` be a nonzero set word and insert a nonempty
letter `X` between `A_p` and `A_(p+1)`.  The exact occurrencewise-safe
condition is

\[
                         X\subseteq A_p\cup A_{p+1}.       \tag{0.1}
\]

The formerly proposed condition `X subseteq A_p` is sufficient but too
strong: it makes the entire left pivot ray inert.  Under (0.1), the only
potentially new interval-union values are the singleton `X` and the two
rays

\[
 X\cup\bigcup_{t=i}^{p}A_t,
 \qquad
 X\cup\bigcup_{t=p+1}^{j}A_t.                             \tag{0.2}
\]

There is an exact all-`d` split socket for the two mixed-coatom chains.  If

\[
 J=K\cup\{\infty,c\},\qquad F=\{f_1,\ldots,f_d\},          \tag{0.3}
\]

then one may take `X=J`, split `J=J_L union J_R` across the two adjacent
letters, and obtain simultaneously

\[
\begin{aligned}
 P_h&=J\cup\{b,f_1,\ldots,f_h\},\\
 S_h&=J\cup\{a,f_{d-h+1},\ldots,f_d\},
                    \qquad 1\le h\le d-1.                 \tag{0.4}
\end{aligned}
\]

All old interval-OR targets survive.  If neither endpoint contains all of
`J`, both displayed ray occurrences are locally new relative to their
corresponding old one-sided intervals, so one physical position births all
`2(d-1)` chain occurrences plus the singleton `J`.  Their set values can
still have unrelated old witnesses elsewhere in the word.

This does not give an in-place flat Pascal recursion.  Let `C_i` be the old
length-`d` interval crossing the pivot cut with `i` letters on the left and
`d-i` on the right.  Equations (0.1) and (0.4) force

\[
 C_i=J\cup\{a,b\}\cup F=:G
                    \qquad(1\le i\le d-1).                \tag{0.5}
\]

If `|G|=r` and the parent depth-`d` row is flat of rank `r`, every existing
parent owner window crossing the cut equals `G`.  If the cut is fully
interior, there are `d` such windows, and any owner-complete flat host with
`M` owner windows and `W` distinct owners must already satisfy

\[
                              M-W\ge d-1.                  \tag{0.6}
\]

In general, if `c_p` depth-`d` owner windows cross the cut, the exact tax is
`M-W>=c_p-1`.  The full two-ray socket itself gives `c_p>=d-2`, hence the
unconditional tax `M-W>=d-3`; one additional exterior source on each shore
raises this to the displayed sharp `d-1`.  Thus no flat `B(k)+O(1)` family
with an interior socket survives as `d` grows.  The escape is genuinely
nonflat: every old crossing target remains witnessed, but its canonical
witness is one letter longer.  Fixed-width/common-cap addresses are not
preserved.

## 1. Exact pivot insertion

Write `A^X` for the word after insertion.  For an old interval `I`, let
`hat I` be the same interval in `A^X`, enlarged by the pivot exactly when
`I` crossed the old cut.

### Theorem 1.1 (canonical occurrence transport)

Every old occurrence has the same union on `hat I` if and only if (0.1)
holds.

#### Proof

A noncrossing interval is copied literally.  A crossing interval contains
both `A_p` and `A_(p+1)`, so its new union is its old union together with
`X`.  The smallest crossing interval is the adjacent pair.  Therefore all
crossing unions are unchanged exactly when
`X subseteq A_p union A_(p+1)`.  \(\square\)

This is an occurrencewise statement.  For target-set preservation in one
fixed word, let `E_p` be the old targets having no witness wholly on either
side of the cut.  The weaker exact condition is

\[
 \operatorname{Cov}(A)\subseteq\operatorname{Cov}(A^X)
 \quad\Longleftrightarrow\quad
 X\subseteq\bigcap_{T\in E_p}T,                            \tag{1.1}
\]

with the empty intersection interpreted as the whole ground set.  Indeed,
a cut-essential target containing `X` transports on any old crossing
witness, while one omitting a coordinate of `X` has neither a crossing nor
a one-sided witness after insertion.

### Corollary 1.2 (exact new deck)

Assume (0.1), and put

\[
 L_h=\bigcup_{t=0}^{h-1}A_{p-t},\qquad
 R_h=\bigcup_{t=1}^{h}A_{p+t}.                             \tag{1.2}
\]

Then

\[
 \operatorname{Cov}(A^X)
 =\operatorname{Cov}(A)\cup\{X\}
   \cup\{X\cup L_h:h\ge1\}
   \cup\{X\cup R_h:h\ge1\}.                             \tag{1.3}
\]

If `X subseteq A_p`, then `X union L_h=L_h` for every `h`; hence only the
right ray can be genuinely new.  The reflected assertion holds when
`X subseteq A_(p+1)`.

The formula concerns OR values, not their widths.  Every old crossing
witness becomes one position longer.

## 2. Necessary and sufficient two-chain equations

Fix prescribed targets `P_h` on the left ray and `S_h` on the right ray.

### Theorem 2.1 (Boolean interval criterion)

For a fixed cut, a nonempty occurrencewise-safe `X` realizes

\[
                         X\cup L_h=P_h,\qquad
                         X\cup R_h=S_h                    \tag{2.1}
\]

for all declared `h` if and only if

\[
                         L_h\subseteq P_h,\qquad
                         R_h\subseteq S_h                 \tag{2.2}
\]

and

\[
 X_{\min}\subseteq X\subseteq X_{\max},\qquad X\ne\varnothing, \tag{2.3}
\]

where

\[
\begin{aligned}
 X_{\min}
   &=\bigcup_h(P_h-L_h)\cup\bigcup_h(S_h-R_h),\\
 X_{\max}
   &=(A_p\cup A_{p+1})
      \cap\bigcap_hP_h\cap\bigcap_hS_h.                  \tag{2.4}
\end{aligned}
\]

#### Proof

Equation `X union L_h=P_h` is equivalent to
`L_h subseteq P_h`, `P_h-L_h subseteq X`, and `X subseteq P_h`.
Intersect these conditions over both rays.  The remaining upper bound in
(2.4) is exactly the safe-insertion condition (0.1).  \(\square\)

There is an equivalent source-by-source form when the prescribed chains are
nested.  Put `P_0=S_0=X` and assume
`P_(h-1) subseteq P_h`, `S_(h-1) subseteq S_h`.  Exact carving is equivalent
to

\[
\begin{aligned}
 P_h-P_{h-1}&\subseteq A_{p-h+1}\subseteq P_h,\\
 S_h-S_{h-1}&\subseteq A_{p+h}\subseteq S_h,              \tag{2.5}
\end{aligned}
\]

for every `h`, together with (0.1).  Under source caps `E_t`, replace the
right-hand sets in (2.5) by `P_h cap E_(p-h+1)` and
`S_h cap E_(p+h)`.  These inclusions, nonemptiness, and the requirement
that the first two sources jointly cover `X` are necessary and sufficient.

## 3. The mixed-coatom specialization

Assume all labels outside `J` in (0.3)--(0.4) are distinct.  Then

\[
             \bigcap_{h=1}^{d-1}P_h
              \cap\bigcap_{h=1}^{d-1}S_h=J.               \tag{3.1}
\]

Thus every common pivot obeys `X subseteq J`.  It cannot itself supply the
exclusive active label `b` on the left or `a` on the right; those labels and
the filler chronology must already occur in the side traces.  More exactly,
(2.1) becomes

\[
\begin{aligned}
 (J-X)\cup\{b,f_1,\ldots,f_h\}
       &\subseteq L_h\subseteq P_h,\\
 (J-X)\cup\{a,f_{d-h+1},\ldots,f_d\}
       &\subseteq R_h\subseteq S_h.                       \tag{3.2}
\end{aligned}
\]

These are the exact all-`d` host equations.

This is the same chain pair as the canonical mixed-screen notation
`A union P_q, B union S_q` after the reindexing `h=d+1-q` on both shores.

### Theorem 3.1 (explicit split socket)

Suppose `|J|>=2`.  Take `X=J` and choose proper nonempty sets `J_L,J_R`
with

\[
                     J_L\cup J_R=J,\qquad
                     J\nsubseteq J_L,\quad J\nsubseteq J_R. \tag{3.3}
\]

Set

\[
\begin{aligned}
 A_p&=J_L\cup\{b,f_1\},\\
 A_{p+1}&=J_R\cup\{a,f_d\},\\
 A_{p-h+1}&=\{f_h\} &&(2\le h\le d-1),\\
 A_{p+h}&=\{f_{d-h+1}\} &&(2\le h\le d-1).              \tag{3.4}
\end{aligned}
\]

Then (0.1) holds and the two pivot rays are exactly (0.4) for every
`d>=2`.  Before insertion, every corresponding left ray omits `J-J_L` and
every corresponding right ray omits `J-J_R`; hence the two displayed ray
occurrences are locally new.  Global novelty of the target values requires
the additional absence of unrelated old witnesses.

#### Proof

The adjacent union contains `J=X`.  Cumulative union on the left gives
`J_L+b+f_1+...+f_h`; adjoining `X` completes it to `P_h`.  The right side
is symmetric.  Properness in (3.3) proves genuine birth.  \(\square\)

A singleton pivot can never genuinely birth both rays: under (0.1) its
sole coordinate lies in at least one adjacent endpoint, making that ray
inert.  The canonical mixed-coatom base contains the two distinguished
labels `infinity,c`, so (3.3) is available abstractly.

If instead the desired chains are the phase-swapped targets over side rays
which already contain the opposite exclusive bases, monotonicity (2.2)
fails: insertion can add labels but cannot remove the wrong active label.
Thus the pivot exposes a prepared split return bank; it does not manufacture
the phase switch from unprepared native rays.

## 4. Flat-host plateau obstruction

Let

\[
 C_i=L_i\cup R_{d-i}\qquad(1\le i\le d-1)                \tag{4.1}
\]

be the old length-`d` crossing values.  From (2.1) and (0.4),

\[
 X\cup C_i=P_i\cup S_{d-i}
   =J\cup\{a,b\}\cup F=G.                                \tag{4.2}
\]

But every `C_i` contains both adjacent sources and therefore contains `X`
by (0.1).  Hence (0.5) follows.

### Theorem 4.1 (linear flat duplicate tax)

Assume `|G|=r` and every old depth-`d` owner window has rank `r`.  Let `c_p`
be the number of existing length-`d+1` windows crossing the pivot cut.  All
of them equal `G`.  Consequently a flat host with `M` such windows which
covers `W` distinct middle owners satisfies

\[
                              M-W\ge c_p-1.                 \tag{4.3}
\]

If the word has `N` source positions and the cut follows position `p`
(zero based), then

\[
c_p=\max\!\left(0,
 \min(p,N-d-1)-\max(0,p-d+1)+1\right).                    \tag{4.4}
\]

In particular, a fully interior cut has `c_p=d` and gives (0.6).

#### Proof

A crossing owner window contains `d+1` sources.  Every existing case
contains one of `C_1,...,C_(d-1)`; at a fully interior cut the two extreme
windows contain `C_1` or `C_(d-1)`.  Its union is therefore a superset of the
rank-`r` set `G`.  Flat rank `r` forces equality.  The start-index interval
of crossing windows gives (4.4).  These `c_p` occurrences contribute only
one distinct owner, so at least `c_p-1` of the `M` slots are duplicate
excess.  \(\square\)

For a flat `B(k)+C` source word with a fully interior socket, the central
row has `M=W+C`; hence `C>=d-1`.  The literal two-ray socket already supplies
`d-1` source positions on each shore, so without any additional exterior
source it still gives `c_p>=d-2` and `C>=d-3`.  Either form rules out a flat
additive-constant spine as `d` grows.

The theorem is deliberately not a nonflat no-go.  By Theorem 1.1 every old
crossing owner still occurs after insertion on its length-`d+2` convex
hull.  The pivot trades a flat row for a one-unit deadline staircase.

## 5. Exact conditional `B+1` implication and remaining gate

### Theorem 5.1 (conditional terminal repair)

Suppose a terminal source word `A` covers every required mask except the
two chains (0.4), and contains the actual local construction (3.4), hence
in particular the safety condition (0.1), together with all literal source
caps.  Then inserting `X=J` produces a universal word of length `|A|+1`.
If additionally `|A|=B(k)`, this is a `B(k)+1` word.

#### Proof

Theorem 1.1 preserves every old target.  Theorem 3.1 supplies every missing
chain target on the two new rays.  \(\square\)

This is a genuine terminal-support escape from the former triangular
return ledger: no old crossing target is lost.  It does not preserve fixed
widths.  For example, in

```text
{ell}, {a} | {b}
```

insert `X={a}` after `{a}`.  The old target `{ell,a,b}` survives only on a
length-four interval; neither new length-three interval realizes it.
Therefore flat-row addresses, residence deadlines, occurrence-labelled
common-cap pins, and regenerative export remain separate checks.

The exact missing construction is now a **nonflat prepared split-pivot
host**: rethread a safe mixed-coatom terminal phase so that (3.4), its caps,
and its two chain deficits coexist, without requiring the forbidden flat
owner row.  The canonical maximal-erosion packet does not supply this cut
in place; its two first active/filler events are separated by the packet
interior.  No unconditional `nu(k)<=B(k)+1` conclusion is claimed.

## 6. Audit

The dependency-free audit

```text
scratch/audit_k_split_pivot_two_chain_20260801.py
```

exhausts all nonempty words of length at most four over a three-coordinate
ground for the safe-insertion/deck identity, checks the fixed-width
counterexample, and verifies (0.4)--(0.6) symbolically for every
`2<=d<=100`.

The frozen summary is

```text
scratch/k_split_pivot_two_chain_20260801.audit.json
```
