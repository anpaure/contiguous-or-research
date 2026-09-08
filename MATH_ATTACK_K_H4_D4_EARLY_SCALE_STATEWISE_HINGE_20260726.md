# The early-scale `D_4/H_4` statewise hinge: exact zero-gain theorem

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.  The two displayed exact `D_4` factors and their audited
six-start ledgers are taken as input.

## 0. Result

Let `p` be the odd prime cap, and write

\[
 C_t=\operatorname {Cat}_t,\qquad
 s=\min\{t:C_t\ge p\},\qquad
 d=C_s,\quad c=C_{s-1},\quad f=C_{s-2},\quad g=C_{s-3}.
 \tag{0.1}
\]

Inside one canonical size-`s+1` parent, the complete canonical loads on
the local targets `2,...,8` are

\[
 \boxed{\Lambda=(d,c,c,2f,2f,5g,5g).}                \tag{0.2}
\]

Thus target `2` is at or above cap, while, for `s>=4`, all the other
displayed targets are strictly below cap.

Let `F` be the canonical `D_4` port factor and `G` the audited
pair-2-to-pair-3 factor.  Put

\[
 H_4=\langle(2\ 3),(4\ 5),(6\ 7)\rangle,
 \qquad
 h_{\alpha\beta\gamma}
  =(2\ 3)^\alpha(4\ 5)^\beta(6\ 7)^\gamma .          \tag{0.3}
\]

For the six open starts, the signed profile of `hG` relative to the fixed
canonical factor is

\[
 \boxed{
 \Delta_{\alpha\beta\gamma}
 =2(1-\alpha)e_2+(-3+2\alpha)e_3
   +(-3+4\gamma)e_6+4(1-\gamma)e_7.}                 \tag{0.4}
\]

The bit `beta` is invisible.  For the hinge statement, assume the
parent-aligned occurrence map sends this complete six-start aggregate to
one common physical carrier slice labelled `2,...,8`, and that its fixed
canonical background makes the total load equal to (0.2).  Define cap
descent with the positive sign by

\[
 \mathsf G_{\alpha\beta\gamma}
 =\sum_{i=2}^8(\Lambda_i-p)_+
  -\sum_{i=2}^8(\Lambda_i+\Delta_{\alpha\beta\gamma}(i)-p)_+.
 \tag{0.5}
\]

For every `s>=5`,

\[
 \boxed{
 \mathsf G_{\alpha\beta\gamma}=-2(1-\alpha).}        \tag{0.6}
\]

Hence four conjugates have gain `-2`, four have gain `0`, and

\[
 \boxed{\max_{h\in H_4}\mathsf G_h=0.}               \tag{0.7}
\]

The same maximum is zero in the finite early case `s=4`; its exact small
correction is displayed in Section 3.  In particular (0.7) remains true
uniformly for every Catalan overshoot

\[
                         1\le\theta={C_s\over p}<4,    \tag{0.8}
\]

and hence throughout the requested open subrange `1<theta<4`, including
the regime `p-C_(s-1)=O(1)`.  Depleting a target whose load is
`p-O(1)` but still below `p` earns no hinge gain.

The three complementary starts have signed profile
`-Delta_(alpha beta gamma)`.  If open starts and complementary starts have
the same physical carrier, their complete singleton histogram is therefore
unchanged pointwise, and the full cap gain is exactly zero for every cap
and every background.  If their carriers are separated, (0.4) is only the
open contribution and no background-independent sign follows.

Consequently the eight-state `H_4` conjugate library does not solve the
early-scale capacity gate.  Above the exact four-cell threshold it supplies
no certified local descent; below that threshold the separately audited
`V_4` coordinate menu still has no discrepancy freedom.  A successful
parent atom must
either decrease the open load at the already saturated target `2`, or
prove a physical carrier separation which places the compensating
complementary profile against a different, favourable residual-capacity
vector.

## 1. The complete canonical Catalan background

In a size-`s+1` parent, write a Dyck filling in first-return form

\[
                            x=1u0v.                    \tag{1.1}
\]

If `u` has semilength `j-1`, the first entry of the canonical MSW
permutation is `2j`.  There are

\[
                  w_j=C_{j-1}C_{s+1-j}                \tag{1.2}
\]

such fillings.  The windows meeting the opposite boundary give the odd
copy with the same multiplicity.  Hence targets `2j` and `2j-1` have
canonical multiplicity `w_j`.  For `j=1,2,3,4`, this gives

\[
\begin{array}{c|ccccccc}
\text{target}&2&3&4&5&6&7&8\\ \hline
\text{load}&C_s&C_{s-1}&C_{s-1}&2C_{s-2}&2C_{s-2}
            &5C_{s-3}&5C_{s-3}.
\end{array}                                             \tag{1.3}
\]

This proves (0.2).  It is the full parent load, not merely the marked
`C_s` fibre.  In particular it contains both `C_(s-1)` collars and the
`C_(s-2)` background families; the entries `2C_(s-2)` and the later
Catalan entries also retain the other canonical starts which a marked-only
calculation would omit.  Thus `Lambda` and the four-stratum total `M_s`
below are different ledgers; no entry `2C_(s-2)` is being identified with
the single tagged double-collar family.

Minimality of `s` gives

\[
                         c<p\le d.                    \tag{1.4}
\]

Moreover

\[
 {c\over f}={2(2s-3)\over s}\ge2\quad(s\ge3),        \tag{1.5}
\]

and

\[
 {c\over g}
 ={4(2s-3)(2s-5)\over s(s-1)}\ge5\quad(s\ge4).       \tag{1.6}
\]

Thus

\[
                 2f\le c<p,\qquad5g\le c<p           \tag{1.7}
\]

for `s>=4`.  Target `2` is consequently the only displayed target which
can meet or exceed cap (its hinge is zero when `d=p`).

For comparison with the occurrence-mass audit, the four distinguished
two-boundary strata have mass

\[
 M_s=d+2c+f,
 \qquad
 {M_s\over d}
 ={5s(5s-7)\over4(2s-1)(2s-3)}.                      \tag{1.8}
\]

If all four strata are forced into four physical cells, total capacity
requires

\[
 {d\over p}\le
 \tau_s:={16(2s-1)(2s-3)\over5s(5s-7)}
 \longrightarrow {64\over25}.                        \tag{1.9}
\]

Equation (1.3) is stronger data than the scalar total (1.8): it specifies
where the complete local canonical background sits before a hinge is
taken.

## 2. All eight open-start profiles

The audited six-open-start histograms of `F` and `G` on coordinates
`1,...,8` are

\[
 u_F=(9,9,12,12,12,12,9,9),
 \qquad
 u_G=(9,11,9,12,12,9,13,9).                          \tag{2.1}
\]

Conjugating the factor relabels this histogram.  The six-start sector is
defined by word positions, so it is preserved by coordinate relabelling;
after reindexing the Dyck ports,

\[
                         u_{hG}=h u_G.                 \tag{2.2}
\]

On the pair `{2,3}`, the two possibilities are

\[
 (11,9)-(9,12)=(2,-3),
 \qquad
 (9,11)-(9,12)=(0,-1).                               \tag{2.3}
\]

The pair `{4,5}` contributes `(0,0)` in either orientation.  On
`{6,7}`, the two possibilities are

\[
 (9,13)-(12,9)=(-3,4),
 \qquad
 (13,9)-(12,9)=(1,0).                                \tag{2.4}
\]

Equations (2.3)--(2.4) prove (0.4).  Explicitly:

\[
\begin{array}{c|c|c}
(\alpha,\beta,\gamma)&u_{hG}(2),\ldots,u_{hG}(8)
 &\Delta_{\alpha\beta\gamma}\\ \hline
(0,0,0),(0,1,0)&(11,9,12,12,9,13,9)
 &2e_2-3e_3-3e_6+4e_7\\
(0,0,1),(0,1,1)&(11,9,12,12,13,9,9)
 &2e_2-3e_3+e_6\\
(1,0,0),(1,1,0)&(9,11,12,12,9,13,9)
 &-e_3-3e_6+4e_7\\
(1,0,1),(1,1,1)&(9,11,12,12,13,9,9)
 &-e_3+e_6.
\end{array}                                             \tag{2.5}
\]

Every row of the last column has coefficient sum zero.  Most importantly,

\[
                         u_{hG}(2)\ge u_F(2)=9         \tag{2.6}
\]

for all eight states.  Thus this library never removes a unit from the
only canonical local target which can meet or exceed cap.

Under the common-carrier alignment stated before (0.5), if the unaffected
canonical load is written as a residual background, then, for large enough
`s`,

\[
 \beta_i=\Lambda_i-u_F(i),\qquad2\le i\le8.           \tag{2.7}
\]

Adding the same `beta` to `u_(hG)` gives exactly
`Lambda+Delta_h`; under that hypothesis the computation is a literal
residual-capacity hinge rather than a comparison of the isolated small
histograms in (2.1).  Without the alignment, (2.7) is only an algebraic
decomposition and has no occurrence-level meaning.

## 3. Exact cap gains

Assume first `s>=5`.  Equations (1.4)--(1.7) show that the negative
entries at targets `3` and `6` drain sub-cap loads.  Also

\[
                         2f+1\le p,\qquad5g+4\le p.   \tag{3.1}
\]

Indeed the exact differences are

\[
 c-2f={2(s-3)\over s}f,
 \qquad
 c-5g={(s-4)(11s-15)\over s(s-1)}g.                  \tag{3.1a}
\]

The first is at least one for `s>=4`; the second is four at `s=5` and
larger thereafter.  Thus `2f+1<=c<p`, while equality `5g+4=c` holds at
`s=5` and the left side is smaller than `c` thereafter.  Therefore no
positive entry of
(0.4), except the one at target `2`, crosses cap.  Since `d>=p`,

\[
\begin{aligned}
 \sum_{i=2}^8(\Lambda_i-p)_+&=d-p,\\
 \sum_{i=2}^8(\Lambda_i+\Delta_h(i)-p)_+
        &=d-p+2(1-\alpha).
\end{aligned}                                          \tag{3.2}
\]

This proves (0.6).

For an exact formula retaining the only small-scale correction, `s>=4`
gives

\[
 \boxed{
 \mathsf G_{\alpha\beta\gamma}
 =-2(1-\alpha)
  -(1-\gamma)(5g+4-p)_+.}                             \tag{3.3}
\]

Indeed `2f+1<=p` already holds at `s=4`.  At `s=4`, one has

\[
 (d,c,f,g)=(14,5,2,1),\qquad p\in\{7,11,13\}.       \tag{3.4}
\]

For `p=7`, the second penalty in (3.3) is two when `gamma=0`; for
`p=11,13` it vanishes.  Choosing `alpha=gamma=1` still gives exact gain
zero.  Thus (0.7) holds in every finite `s>=4` early case.

### 3.1 Whole prefix-bank normalization

If one state is repeated on `N` aligned suffix packets whose pushed-forward
profiles share the same physical targets, the signed increment is
`N Delta_h`.  The exact open-sector new-minus-old hinge is

\[
\boxed{
 \Xi_U(N)=2N(1-\alpha)
 +(1-\gamma)(5g+4N-p)_+
 +\gamma(2f+N-p)_+.}                                  \tag{3.4a}
\]

The natural right-concatenated `D_4` prefix bank has

\[
                              N=C_{s-4}.               \tag{3.4b}
\]

Its two possible off-primary deposits remain below cap.  Precisely,

\[
 2C_{s-2}+C_{s-4}\le C_{s-1}\quad(s\ge4),            \tag{3.4c}
\]

and

\[
 5C_{s-3}+4C_{s-4}\le C_{s-1}\quad(s\ge5).           \tag{3.4d}
\]

The first difference vanishes only at `s=4`; the second vanishes at
`s=5`.  Since `C_(s-1)<p`, (3.4a) reduces, for `s>=5`, to

\[
                         \Xi_U(C_{s-4})
                           =2C_{s-4}(1-\alpha).        \tag{3.4e}
\]

Thus the whole canonical prefix bank has the same zero best relief as one
atom; the normalization changes `2` to `2C_(s-4)`, not the conclusion.
Independent suffix choices are covered by taking their final aggregate:
target `2` never decreases, while every other canonical target begins
below cap.

The near-saturated-collar regime causes no exception.  Even if

\[
                         p-c=O(1),                    \tag{3.5}
\]

target `3` has load strictly below cap, and every state in (2.5) decreases
that load.  The hinge is flat below cap, so this depletion has value zero.

There is a useful aggregate strengthening.  Consider any legal collection
of these `H_4`-conjugate atoms whose open profiles have one common physical
carrier slice.  Its total increment at target `2` is nonnegative.  Every
other target starts below cap.  Hence the final cap excess cannot be less
than the original excess at target `2`.  Arbitrarily many states from this
menu therefore still have nonpositive total descent; (0.7) is not merely a
failure of choosing the best single conjugate.

## 4. Complementary starts and full background repayment

Let `v_F,v_G` be the histograms of the three complementary cyclic starts.
The audited local permutation-word identity gives

\[
 u_F+v_F=u_G+v_G=14\sum_{i=1}^9e_i.                  \tag{4.1}
\]

After any `h in H_4`, the right side is unchanged.  Consequently

\[
                  v_{hG}-v_F=-\Delta_h.               \tag{4.2}
\]

If all nine starts have one common exterior carrier and local injection,
then the open and complementary signed measures cancel before the cap
hinge is evaluated.  Thus

\[
 \boxed{
 \text{complete matched singleton gain}=0}            \tag{4.3}
\]

for every `h`, every cap, and every additional background histogram.  This
is the exact collar/background statement.  It is stronger than (0.7).

If the six open starts and the three complementary starts have disjoint
physical carrier images, their signed profile is instead

\[
                     \iota_U(\Delta_h)-\iota_V(\Delta_h).          \tag{4.4}
\]

Its sign depends on the two residual-capacity vectors.  Formula (4.4)
cannot be credited as descent without a parent atlas proving both carrier
separation and the favourable placement of canonical background.  In
particular, common-carrier cancellation supplies a legitimate zero-gain
realization and rules out any state-independent uniformly positive theorem
for this menu.

There is one further exact canonical test.  Suppose the two carrier images
are disjoint but each is loaded by a copy of the canonical vector (0.2).
Put

\[
 R=d-p,\qquad A=p-c,\qquad B=p-2f,\qquad C=p-5g.       \tag{4.5}
\]

All four numbers are nonnegative and `A>=1`.  Let `Xi_U` and `Xi_V`
denote new-minus-old hinge on the open and complementary images.  Direct
substitution of `Delta_h` and `-Delta_h` gives

\[
 \Xi_U=2(1-\alpha)+(1-\gamma)(4-C)_+,                 \tag{4.6}
\]

\[
 \Xi_V=-\min\{2(1-\alpha),R\}
       +(3-2\alpha-A)_+
       +(1-\gamma)(3-B)_+.                            \tag{4.7}
\]

Consequently

\[
\begin{aligned}
 \Xi_U+\Xi_V={}&2(1-\alpha)-\min\{2(1-\alpha),R\}
 +(3-2\alpha-A)_+\\
 &+(1-\gamma)\bigl((4-C)_++(3-B)_+\bigr)\ge0.        \tag{4.8}
\end{aligned}
\]

Thus even ideal separation into two identically loaded canonical carrier
slices has no positive relief; `alpha=gamma=1` is exactly neutral.  This
includes `A=p-C_(s-1)=1`.  Only genuinely unequal or row-dependent
backgrounds escape (4.8), and those require a new carrier theorem.

At higher local interval lengths the complete `D_4` carrier tensor is
nonzero at lengths `2,3,6,7`; the present theorem does not obstruct a
higher-context construction using those profiles.  It closes only the
requested early matched/six-open-start `H_4` statewise hinge.

There is one indispensable alignment caveat.  The Catalan census (0.2)
comes from two distinguished boundary-window families, whereas `u_h`
aggregates six local cyclic starts.  Equations (0.5), (3.2), and (3.4a)
are exact physical hinges only under the common-carrier parent alignment
stated before (0.5).  With row- or start-dependent carriers, the exact
occurrence-resolved push-forward is mandatory; the aggregate vector
`Delta_h` alone does not determine a cap sign.

## 5. The full `F/G` ownership overlay is one fourteen-row atom

The non-coordinate replacement does not secretly decompose into smaller
independent row packets.  Contract the common root-port edge between the
old and new copies of each row.  Equality of any old `X`-state and new
`X`-state then joins the corresponding roots in the ownership overlay.
The following thirteen shared states form a spanning tree on all fourteen
Dyck roots:

\[
\begin{array}{c|c|c}
\text{old `F` root}&\text{shared `X` state}&\text{new `G` root}\\ \hline
1234&1348&1346\\
1235&1458&1346\\
1236&1238&1234\\
1237&1467&1236\\
1245&1268&1237\\
1246&1278&1237\\
1247&1267&1236\\
1247&1567&1256\\
1257&3467&1256\\
1256&1456&1345\\
1347&2347&1247\\
1347&2367&1356\\
1357&2467&1356.
\end{array}                                             \tag{5.1}
\]

Every equality in (5.1) follows directly from the canonical `q_F` word
table and the displayed `G` path table.  The graph in (5.1) is connected
and has thirteen edges, so the
complete `X/Y` ownership overlay is connected as well.  Therefore:

\[
 \boxed{
 \text{a component shore choice between `F` and `G` switches all fourteen
 rows at once.}}                                       \tag{5.2}
\]

Contextual copies on disjoint row slabs may still be selected independently,
but one direct `F/G` copy is an indivisible fourteen-row atom.  This proves
that the direct two-factor overlay has no proper component subtrade; it does
not rule out a subtrade using a third factor, a recomputed multi-factor
overlay, or a bank of contextual copies.  In particular it does not give
fourteen independently routable marked rows.  Any claimed discrepancy
rounding must use the actual fourteen-row carrier vector of each atom and
must separately prove coverage of the entire four-stratum occurrence
tensor.

### 5A. A local multi-state rectangle exists, but its companion rows are compulsory

There is a second exact `D_4` port factor, call it `H`, displayed with its
complete `X/Y` ledgers in
`MATH_ATTACK_D4_PAIR23_PORT_FACTOR_GATE_20260726.md`.  An independent
ledger audit gives its first-insertion vector, in the standard root order,

\[
 (8,8,8,6,8,8,6,3,4,2,2,2,4,2).                    \tag{5.3}
\]

For comparison, the rowwise labels under `F,H,G` are

\[
\begin{array}{c|ccc@{\qquad}c|ccc}
P&F&H&G&P&F&H&G\\ \hline
1234&8&8&8&1256&4&3&7\\
1235&8&8&8&1257&4&4&3\\
1236&8&8&7&1345&2&2&6\\
1237&6&6&8&1346&2&2&8\\
1245&8&8&3&1347&2&2&8\\
1246&8&8&3&1356&2&4&2\\
1247&6&6&3&1357&2&2&4.
\end{array}                                             \tag{5.4}
\]

Thus `1256` is the unique row in this three-factor library with three
distinct marked labels.  In two coordinate-disjoint active contexts one
may use `1256` on the left, giving labels `{4,3,7}`, and `1345` on the
right, giving `{2,6}` under `F/G`.  With a common core these give a literal
`3 by 2` rectangle of six distinct physical targets.  Two disjoint copies
of the `1256` context similarly give a literal `3 by 3` rectangle.

This does not supply a six- or nine-cell routing of every row.  A state is
a complete factor choice, so all companion transitions in (5.4) occur at
once.  The exact six-open-start profile of `H` is

\[
 u_H=(9,10,12,11,12,11,10,9),
 \qquad
 u_H-u_F=e_2-e_4-e_6+e_7.                             \tag{5.5}
\]

Its complementary three-start profile is the negative of (5.5).  On the
canonical load vector (0.2), the open-sector new-minus-old hinge is exactly
`+1`: the factor adds one unit to the saturated target `2`, while its
negative companion units lie below cap.  Therefore `H` supplies a genuine
local alphabet enlargement but no statewise cap descent.  It cannot be
used as an all-occurrence multi-state block until a parent atlas proves
both row coverage and favourable separation of the complete companion
carrier tensor.

The direct `F/H` overlay does have smaller component trades.  Its nonzero
open-start pieces may be taken on the root sets

\[
 \{1236,1246\}:e_3-e_4,
 \qquad
 \{1256,1257,1356\}:e_2-e_3-e_6+e_7,                 \tag{5.6}
\]

while the component on `{1234,1235}` has zero open profile.  The active
three-row component is the exact source of `1256:4 -> 3` (with the
companion `1356:2 -> 4`).  It still adds one unit to target `2`, so its
canonical new-minus-old hinge is `+1`.  Reanchoring it by `H_4` makes its
target-`2` coefficient either `+1` or `+2`, never negative.  Thus genuine
fragmentation reduces packet size but does not reveal a hidden drain of the
Catalan source.

## 6. Exact implication scope

Combining the audited occurrence mass with the present statewise theorem
gives the following precise boundary.

1. If the four tagged Catalan strata collapse into four physical cells,
   `theta>tau_s` in (1.9) is a statewise capacity obstruction.
2. If `theta<=tau_s`, scalar capacity alone is not enough: the audited
   coordinate `V_4` overlay has one component on all four strata, so its
   shore choices only permute the cells.
3. Replacing the coordinate state by any of the eight factors `hG` does
   not give positive six-open-start cap gain on the complete canonical
   early background; the best gain is exactly zero.
4. The direct `F/G` ownership overlay is connected, so that particular
   two-shore contextual copy is an indivisible fourteen-row atom.  This
   says nothing universal about a three-factor or recomputed overlay.  A
   positive result still needs an occurrence-covering bank of legal atoms
   with a favourable full carrier map, or a different parent-aligned factor
   whose open profile actually drains target `2`.

No coefficient-one conclusion is claimed.  The proved no-go is exact for
the `H_4` conjugate `D_4` singleton/open-start architecture and leaves the
audited nonzero higher-length carrier profiles as a separate route.
