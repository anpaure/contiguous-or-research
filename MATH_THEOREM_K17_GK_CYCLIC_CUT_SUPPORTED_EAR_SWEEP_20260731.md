# All cyclic two-cut GK forests and the adjacent-cut provider bank

Date: 2026-07-31
Status: symbolic path-forest and all-window theorem for every cyclic
separation; exact finite **marginal Hall** result at `s=1,16` and
old-endpoint-anchored immutable-forest Hall no-go at every `s=2,...,15`.
The adjacent seed is
classified in closed form as a ballot matching.  Its provider perfect
matching has a twice-up/ballot-reroute formula; wedge survival is certified
literally rather than by a uniform symbolic support lemma.
No ear completion or `K17` word is claimed.

## 0. Outcome

Let `p_s(C)` be the Greene--Kleitman upward pivot of a rank-six mask `C`
when the cyclic coordinate order starts at `s`.  For each
`s in {1,...,16}`, retain the edge

\[
       (C+p_0(C))(C+p_s(C))                            \tag{0.1}
\]

when the two pivots differ.  Every resulting graph `F_s` was reconstructed
literally.  Each is a path forest; for every internal window width, all
window unions have the expected rank and are globally distinct.

For each `F_s`, the complete locally allowed endpoint/unused Johnson-edge
catalogue was built, unsupported edges were peeled to the greatest
edge/wedge fixed point, and the missing-rank-six to fresh-rank-eight
provider matching was computed exactly.  The verdict is

\[
 \boxed{\nu(B_s)=|M_s|\quad\Longleftrightarrow\quad s\in\{1,16\}.} \tag{0.2}
\]

Thus the old half-rotation choice `s=9` is not representative: its rank is
only `1780/2224`, whereas the adjacent-cut choices `s=1,16` have exact rank
`8736/8736` and no zero provider row.  This closes only the first marginal
Hall gate.  It does **not** select a resource-disjoint ear family, join the
components, enforce global turn injectivity, place the `4534` repeated
payloads, or solve upper coverage, residence, and compilation.

## 1. Symbolic product-SCD theorem for every shift

Put

\[
       A=[0,s),\qquad B=[s,17),\qquad |B|=17-s.       \tag{1.1}
\]

Restrict the ordinary Greene--Kleitman SCD to the two coordinate intervals.
For a segment chain of length `ell` and bottom rank `q`, write its members as

\[
       X_q\subset X_{q+1}\subset\cdots\subset X_{\ell-q}. \tag{1.2}
\]

Let a rank-six source be

\[
             C=(A_a,B_{6-a}),                         \tag{1.3}
\]

where the two segment chains have bottom ranks `q,r`.  The maximum prefix
heights within the two segment words are

\[
           m_A=a-q,\qquad m_B=6-a-r,                  \tag{1.4}
\]

and the displacement of the first segment is `d_A=2a-s`.  In the order
`AB`, the last-maximum convention chooses its pivot in `A` exactly when

\[
                       m_A>d_A+m_B.                   \tag{1.5}
\]

Put

\[
                       d_B=2(6-a)-(17-s).             \tag{1.5a}
\]

In the order `BA`, it chooses its pivot in `B` exactly when

\[
                       m_B>d_B+m_A.                   \tag{1.6}
\]

Here `d_A+d_B=12-17=-5`.  Therefore the two pivots differ exactly when

\[
 \boxed{1\le m_A-d_A-m_B=s-6-q+r\le4.}               \tag{1.7}
\]

The strict endpoints in (1.7) are important.  At value zero the later `B`
maximum wins in `AB`, and both orders choose the same `B` pivot.  At value
five the later `A` maximum wins in `BA`, and both orders choose the same `A`
pivot.

For a chain pair satisfying (1.7), sources exist for

\[
 L=\max(q,s+r-10)\le a\le
 U=\min(s-q-1,6-r).                                  \tag{1.8}
\]

The corresponding edge has endpoints

\[
 L_a=(A_{a+1},B_{6-a}),\qquad
 R_a=(A_a,B_{7-a})=L_{a-1}.                          \tag{1.9}
\]

Thus one qualifying pair of segment chains gives one path, with the edges
indexed consecutively by `a=L,...,U`.  Different chain pairs are disjoint,
because a rank-seven vertex has unique membership in each segment SCD.
This proves, without enumeration, that every `F_s` is a path forest.

More is true.  A window of `w` consecutive path vertices beginning at
`L_a` has union

\[
 L_a\cup L_{a-1}\cup\cdots\cup L_{a-w+1}
       =(A_{a+1},B_{5-a+w}).                          \tag{1.10}
\]

Its rank is exactly `6+w`.  Its `A`-rank recovers `a`, and unique segment-SCD
membership then recovers both chains and the occurrence.  Hence every
available consecutive-window union is globally injective.  Different
widths cannot collide because their ranks differ.  In particular, the
rank-eight edge unions and all higher internal window unions are globally
private.

Let

\[
 \gamma_\ell(j)=\binom{\ell}{j}-\binom{\ell}{j-1},
 \qquad \lambda_{s,q,r}=(U-L+1)_+,                   \tag{1.11}
\]

with the binomial coefficient interpreted as zero outside its range.  The
number of components, edges, and `w`-vertex windows is therefore, with all
three sums restricted to

\[
             0\le q\le\lfloor s/2\rfloor,
 \qquad 0\le r\le\lfloor(17-s)/2\rfloor,             \tag{1.11a}
\]

\[
C_s=\sum_{\substack{0\le q\le\lfloor s/2\rfloor\\
                    0\le r\le\lfloor(17-s)/2\rfloor}}
      \gamma_s(q)\gamma_{17-s}(r)
      {\bf1}_{1\le s-6-q+r\le4}{\bf1}_{\lambda>0},   \tag{1.12}
\]

\[
E_s=\sum_{\substack{0\le q\le\lfloor s/2\rfloor\\
                    0\le r\le\lfloor(17-s)/2\rfloor}}
      \gamma_s(q)\gamma_{17-s}(r)
      {\bf1}_{1\le s-6-q+r\le4}\lambda_{s,q,r},      \tag{1.13}
\]

\[
N_{s,w}=\sum_{\substack{0\le q\le\lfloor s/2\rfloor\\
                        0\le r\le\lfloor(17-s)/2\rfloor}}
      \gamma_s(q)\gamma_{17-s}(r)
      {\bf1}_{1\le s-6-q+r\le4}
      (\lambda_{s,q,r}-w+2)_+.                       \tag{1.14}
\]

Finally `V_s=E_s+C_s` and `T_s=N_{s,3}=E_s-C_s`.

## 2. Exact census and audit of the formulas

Write `E,V,C,T` for the numbers of old edges, used rank-seven vertices,
components, and internal rank-nine turns of `F_s`.  The component column
uses `a^b` to mean `b` paths on `a` vertices.  The width column lists the
numbers of internal windows at widths `2,3,...`; each displayed number is
also the number of distinct unions, and every width-`w` union has rank
`w+6`.

| shifts | `E` | `V` | `C` | `T` | component sizes | protected internal widths |
|---|---:|---:|---:|---:|---|---|
| `1,16` | 3640 | 7280 | 3640 | 0 | `2^3640` | `3640` |
| `2,15` | 5278 | 8918 | 3640 | 1638 | `2^2002 3^1638` | `5278,1638` |
| `3,14` | 6916 | 11557 | 4641 | 2275 | `2^3003 3^1001 4^637` | `6916,2275,637` |
| `4,13` | 7982 | 12623 | 4641 | 3341 | `2^2145 3^1859 4^429 5^208` | `7982,3341,845,208` |
| `5,12` | 8916 | 13975 | 5059 | 3857 | `2^2563 3^1397 4^891 5^154 6^54` | `8916,3857,1361,262,54` |
| `6,11` | 9520 | 14579 | 5059 | 4461 | `2^2145 3^1815 4^715 5^330 6^44 7^10` | `9520,4461,1547,448,64,10` |
| `7,10` | 9956 | 15180 | 5224 | 4732 | `2^2310 3^1590 4^940 5^285 6^89 7^9 8^1` | `9956,4732,1818,494,110,11,1` |
| `8,9` | 10152 | 15376 | 5224 | 4928 | `2^2184 3^1716 4^876 5^349 6^83 7^15 8^1` | `10152,4928,1888,564,116,17,1` |

The symbolic formulas (1.12)--(1.14) give the table, and the independent
literal sweep gives the same table.  The replay also checks the identities

\[
                 E=V-C,\qquad T=E-C,                 \tag{2.1}
\]

as well as maximum degree at most two, exactly `2C` endpoints, no cyclic
component, and collision-free union maps at every displayed width.  These
are direct finite checks, not deductions from the scalar counts alone.

## 3. The tail scalar ledger is cut-invariant

The target tail has `16911` rank-seven owners and `16910` edges.  For a
fixed `s`, the unoccupied internal-owner budget and number of component
joins are

\[
                  I_s=16911-V_s,\qquad J_s=C_s-1.     \tag{3.1}
\]

Using (2.1), the required number of new edges is

\[
 I_s+J_s=16910-(V_s-C_s)=16910-E_s.                  \tag{3.2}
\]

The old edge intersections are distinct, so the number of missing
rank-six colours is `12376-E_s`.  Consequently the number of new edges
which must repeat a geometric rank-six colour is always

\[
 (16910-E_s)-(12376-E_s)=\boxed{4534}.                \tag{3.3}
\]

Thus changing `s` changes the forest, endpoint bank, and number of missing
rank-six colours, but not the repeated-payload scalar.  In particular, the
positive `s=1` face has

\[
 (E,V,C,T)=(3640,7280,3640,0),\quad
 I=9631,\quad |M|=8736,\quad 13270\text{ new edges}.  \tag{3.4}
\]

## 4. Exact supported-ear Hall projection

For each shift, classify rank-seven vertices as old endpoints, old
internals, or unused.  An allowed new edge has both ends among endpoints
and unused vertices, has a fresh rank-eight union, has fresh boundary
rank-nine turns, and does not directly close an old component.  At an
unused vertex, two allowed incident edges form a wedge exactly when their
unions and all forced local rank-nine turns are distinct and fresh.

Repeatedly delete a wedge when one of its edges is deleted, and delete an
edge when it has no surviving wedge at an unused endpoint.  Every locally
clean arbitrary-length ear family whose ears are anchored at old endpoints
and hence have no terminal unused ray is a post-fixed point of this
operator, so all its edges survive the greatest fixed point.  A completion
allowed to terminate at an unused vertex lies outside this implication.

Let `B_s` join a missing rank-six colour to the fresh rank-eight union of
each surviving edge carrying it.  A locally clean completion with globally
distinct rank-eight unions would choose one different neighbour for every
missing colour.  Hence it necessarily gives a matching saturating the left
side of `B_s`.

The exact ranks are:

| shifts | missing rows | provider rights | incidences | zero rows | rank | deficiency |
|---|---:|---:|---:|---:|---:|---:|
| `1,16` | 8736 | 13817 | 272992 | 0 | **8736** | **0** |
| `2,15` | 7098 | 13741 | 240187 | 550 | 6459 | 639 |
| `3,14` | 5460 | 8730 | 131567 | 220 | 5208 | 252 |
| `4,13` | 4394 | 9136 | 116616 | 520 | 3794 | 600 |
| `5,12` | 3460 | 7910 | 66501 | 232 | 3199 | 261 |
| `6,11` | 2856 | 7221 | 57843 | 432 | 2365 | 491 |
| `7,10` | 2420 | 6714 | 36427 | 360 | 2046 | 374 |
| `8,9` | 2224 | 6530 | 33564 | 416 | 1780 | 444 |

It follows that old-endpoint-anchored immutable locally clean ear completion
is impossible for all `s=2,...,15`, already in this relaxed marginal
projection.  This does not rule out architectures with terminal unused
rays or changes to the old forest.  The
`s=9` bounded length-five census is consistent with, and strictly subsumed
by, the stronger `1780/2224` all-length obstruction.  That length-five
census must not be transferred to the different endpoint banks at
`s=1,16`.

For `s=1`, an explicit `8736`-row certificate records every provider menu
and one distinct matched rank-eight union.  A second implementation
materializes all `458934` raw edges and `20973132` raw wedges, peels to
`454930` edges and `20772564` wedges in three rounds, reconstructs rank
`8736`, and replays every row and every selected pair of that certificate.
This independent replay rules out an edge-only support-closure artefact.

## 5. The adjacent seed is a ballot matching

There is a dimension-uniform explanation for the exceptional row.  For a
rank-`r` word `C` of length `N` with `r<N/2`, put

\[
 h_j=\sum_{i<j}(2{\bf1}_{i\in C}-1),\qquad h_N=2r-N. \tag{5.1}
\]

The pivot `p_0` is the last maximizer among `h_0,...,h_{N-1}`, while `p_1`
is the last maximizer among `h_1,...,h_N`.  The two differ if and only if

\[
                         h_j<0\quad(1\le j<N).        \tag{5.2}
\]

Indeed, if an interior maximum is at least zero then the same last interior
maximum is seen from both cuts.  Under (5.2), `p_0=0`, while `p_1` is the
last `j` with `h_j=-1`.  In particular `p_0` and `p_1` are both zero
coordinates, the first lifted endpoint contains coordinate zero, and the
second does not.  Each upward map is injective, and their images lie on
opposite coordinate-zero shores.  Hence `F_1` is a matching.

The cycle lemma counts the strict-negative rotations:

\[
 |E(F_1)|=\frac{N-2r}{N}\binom Nr.                   \tag{5.3}
\]

At `N=17,r=6`, this is

\[
 \frac5{17}\binom{17}{6}
  =\binom{16}{6}-\binom{16}{5}=3640.                 \tag{5.4}
\]

Equivalently, (1.7)--(1.8) leave only the segment type `(q,r)=(0,6)`
and one source rank per chain pair.  Thus the positive seed is exactly
`3640` disjoint GK edges, not merely a forest whose census happened to have
zero turns.

This removes the geometric internal-vertex obstruction completely.  If `D`
is a missing rank-six colour and

\[
 A_s(D)=\{a\notin D:\deg_{F_s}(D+a)\le1\},           \tag{5.5}
\]

then the Johnson carrier with lower colour `D` and upper colour
`D+{a,b}` is geometrically usable without cutting the old forest exactly
when `a,b` are distinct members of `A_s(D)`.  At `s=1`, every rank-seven
vertex has degree zero or one, so

\[
                         |A_1(D)|=11                 \tag{5.6}
\]

for every missing `D`.  By contrast, every representative `s=2,...,8` has
missing rows with only two geometrically usable supersets, and its supported
peel subsequently has literal zero rows.

## 6. Why the adjacent provider graph has a perfect matching

Let `R_1` be the relation whose left shore is the `8736` missing rank-six
colours and whose right shore consists of fresh rank-eight unions.  Put
`D R_1 Q` when the unique Johnson edge with lower colour `D` and upper
colour `Q` survives the greatest locally wedge-supported peel of Section 4.

There is in fact a formula-level SDR, apart from one rowwise support check.
Let `U` be the order-zero GK upward map.  For exactly `8164` missing colours,

\[
                           Q(D)=U^2(D)                 \tag{6.1}
\]

is a surviving provider.  The remaining `572` colours are precisely

\[
 \mathcal E=\left\{D=\{0\}\cup S:
   S\in\binom{\{5,\ldots,16\}}5,
   \sum_{i=4}^t(2{\bf1}_{i\in D}-1)\le0
   \text{ for }4\le t\le16\right\}.                 \tag{6.2}
\]

The ballot reflection count is

\[
                         |\mathcal E|
  =\binom{13}{5}-\binom{13}{4}=572.                  \tag{6.3}
\]

For `D in E`, let `j(D)` be the first coordinate after the last zero-height
prefix of the word on coordinates `4,...,16`; the empty prefix ends at
coordinate three.  Then

\[
 j(D)\in\{4,6,8,10,12,14\},\qquad
 Q(D)=D+\{2,j(D)\}.                                  \tag{6.4}
\]

Put `X_D=D+2` and `Y_D=D+j(D)`.  Both are containing-zero endpoints of old
seed dominoes.  Their old partners are respectively

\[
 (X_D-0)+3,\qquad (Y_D-0)+1,                         \tag{6.5}
\]

so the new direct edge has fresh boundary turns `Q(D)+3` and `Q(D)+1`.
The `X` bank contains coordinate two and the `Y` bank omits it, hence the
banks are disjoint.  The `X` map is injective.  From `Y_D`, the modified
word on coordinates `4,...,16` first reaches height `+1` exactly at `j(D)`,
so `j(D)` and then `D` are recoverable; the `Y` map is injective as well.
Thus the `572` edges use `1144` distinct old endpoints and hence `1144`
distinct seed components.

The same recovery proves the `572` upper masks distinct.  Their full
order-zero prefix maximum is one, so they lie in GK chains of bottom rank
seven.  No mask `U^2(D')` coming from rank six lies in such a chain.
Consequently (6.1) and (6.4) together give `8736` distinct rank-eight
providers.  The boundary turns are also globally distinct: the two banks
are separated by presence of coordinate one versus coordinate three, and
within each bank injectivity follows from injectivity of `Q(D)`.

The finite provider replay is still used for one statement: every one of the
`8164` standard edges (6.1), and every exceptional edge (6.4), survives the
greatest wedge-support peel.  It checks this as follows.

1. The stored table has one row for every missing `D`, records its complete
   `R_1` menu, and selects one `Q` in that menu.
2. The symbolic choices (6.1),(6.4) all belong to those menus and are
   pairwise distinct.
3. An independent implementation materializes all `458934` raw edges and
   `20973132` raw wedges, obtains the same fixed point of `454930` edges and
   `20772564` wedges, reconstructs rank `8736`, and replays every selected
   pair.

Therefore this is a formula-based perfect matching with literal support
certification, not evidence from a numerical rank alone.  The fixed graph
has at least three providers per row and no zero row.  A fully symbolic
construction of the supporting wedge at every endpoint of all `8164`
standard edges is not proved here; that membership is the only
non-symbolic ingredient in the SDR theorem.  The whole construction is
equivariant across the
adjacent-cut family: rotating the certificate for cuts `(0,1)` by `t`
gives a certificate for cuts `(t,t+1)`.  In particular the isomorphism of
Section 8 transports it to `s=16`.

This distinction matters.  The symbolic ballot theorem explains why the
adjacent bank has no internal-owner blockade, but all-eleven geometric
availability by itself does not prove wedge survival.  Formula (6.4) is the
exact symbolic repair of the sole failure of the naive twice-up rule.

## 7. Exact constructive target after marginal Hall

Retain the `3640` old edges as oriented two-vertex dominoes.  A final tail
path must use `9631` of the `12168` unused rank-seven vertices as singleton
blocks.  It therefore has

\[
                  3640+9631=13271                    \tag{7.1}
\]

blocks and exactly `13270` inter-block edges.  Equivalently, order the old
dominoes and join consecutive dominoes by `3639` ears of positive edge
lengths `\ell_i` satisfying

\[
 \sum_i(\ell_i-1)=9631,\qquad \sum_i\ell_i=13270.    \tag{7.2}
\]

If `b` ears are non-direct, their edge-type counts are

\[
 \#EE=3639-b,\qquad \#EU=2b,\qquad \#UU=9631-b.      \tag{7.3}
\]

The exact endpoint census has `3640` missing colours with no old endpoint
superset.  They must use `UU` edges.  But (7.3) gives, for every possible
ear-length distribution,

\[
             \#UU\ge9631-3639=5992>3640.             \tag{7.4}
\]

The no-`EE` provider projection has exactly the `572` zero rows
`\mathcal E` of (6.2).  Hence some direct bank is mandatory on that face.
The formula (6.4) does more than match its labels: it is a resource-disjoint
clean bank of `572` direct ears, with distinct rank-eight labels, distinct
boundary rank-nine labels, and `1144` distinct old endpoints.  Contracting
these edges leaves

\[
 572\text{ two-domino blocks}+2496\text{ untouched dominoes}
   =3068\text{ blocks}.                              \tag{7.5}
\]

The remaining path therefore needs exactly `3067` long ears.  There are
`7280-1144=6136` exposed base endpoints, while those ears require `6134`;
the two unused endpoints are exactly the final path ends.  Thus the base
endpoint equation is sharp, not merely slack.

One exact scalar realization is

\[
             (x_1,x_4,x_5)=(572,2637,430).            \tag{7.6}
\]

Indeed,

\[
 572+2637+430=3639,                                  \tag{7.7}
\]

\[
 3(2637)+4(430)=9631,                                \tag{7.8}
\]

and

\[
 572+4(2637)+5(430)=13270.                           \tag{7.9}
\]

After the direct bank, every remaining new edge has type `EU` or `UU`.  The
exact type ledger is

\[
             \#EU=6134,\qquad \#UU=6564.             \tag{7.10}
\]

For the independently frozen direct solution, filtering the already
peel-surviving relation by deleting the `572` rows, their used rank-eight
resources, their `1144` endpoints, all residual `EE` edges, and their `1144`
boundary turns gives

\[
 8164\text{ rows},\quad11906\text{ rank-eight resources},\quad
 242771\text{ incidences},                            \tag{7.11}
\]

with ordinary matching rank `8164`.  The symbolic ballot bank (6.4), which
differs from that frozen solution on 24 choices, analogously gives `11905`
resources and `242766=57003+185763` `EU+UU` incidences.  In both banks every
residual row retains the canonical provider `U^2(D)`, so injectivity of `U^2`
is already an explicit residual perfect matching.

These counts filter the original greatest fixed point; by themselves they
do not constitute a conditioned re-peel.  A separate bounded-path replay,
recorded in the artifacts below, certifies conditioned support of every
canonical residual edge.  From its two sides, the extra distances to free
old endpoints have exact histogram

```text
(1,0):2910  (1,1):2520  (2,0):1614  (2,1):880
(2,2): 208  (3,2):  30  (3,3):   2.
```

Thus radius three suffices after conditioning.  Each row has its own
post-fixed compatible path witness, so every canonical edge survives the
true conditioned greatest peel.  Even that stronger fact does not meet the
exact `6134` endpoint incidences or jointly pack the witness paths: different
rows may reuse owners, edges, turns, or components.

### 7.1 Residual type normal form and zero-excess selection

Write `BU` for a provider edge joining one exposed old-base endpoint to one
unused rank-seven vertex, and `UU` for a provider edge joining two unused
vertices.  (`BU` is called `EU` in the older endpoint/unused artifacts.)
After fixing the authenticated `572` direct ears of SHA `7abcbd84...`, the
`8164` residual rows have the exact type census

\[
 \begin{array}{c|ccc}
 \text{row type}&UU\text{-only}&BU\text{-only}&\text{mixed}\ (BU+UU)\\ \hline
 \text{count}&3640&1001&3523.
 \end{array}                                      \tag{7.11a}
\]

Let `b` be the number of selected `BU` providers.  The selected provider
types are then

\[
                         (BU,UU)=(b,8164-b).         \tag{7.11b}
\]

The complete long-ear ledger (7.10) forces the later repeated-colour edges
to have types

\[
              (BU_{\rm rep},UU_{\rm rep})
                =(6134-b,b-1600).                   \tag{7.11c}
\]

Nonnegativity gives `b>=1600`; the row census gives
`b<=1001+3523=4524`.  Thus the exact scalar interval is

\[
                         1600\le b\le4524.           \tag{7.11d}
\]

For the old-endpoint-anchored architecture, this corrects the tempting but
false requirement that the provider edges themselves use all `6134` base
endpoints.  Repeat edges may and generally must fill the remaining base
slots.

The residual capacity gate on this frozen direct-bank face is positive.
There is an authenticated literal selection with

\[
       (BU,UU)=(3065,5099),\qquad
       (BU_{\rm rep},UU_{\rm rep})=(3069,1465).      \tag{7.11e}
\]

It selects one supported provider for every residual lower row, uses `8164`
distinct rank-eight labels, has base load at most one and unused load at
most two, and has distinct boundary rank-nine labels.  Together with the
direct bank it therefore has `8736` distinct new rank-eight labels and
`4209=1144+3065` distinct forced boundary turns.  Its exact load histograms
are

\[
 \begin{array}{c|cc}
 \text{base load}&0&1\\ \hline
 \text{vertices}&3071&3065
 \end{array},
 \qquad
 \begin{array}{c|ccc}
 \text{unused load}&0&1&2\\ \hline
 \text{vertices}&4416&2241&5511.
 \end{array}                                      \tag{7.11f}
\]

The final owner set in the same no-terminal-ray architecture must add
`1879` of the currently zero-load unused vertices.  The repeat-edge unused
incidence demand is consequently

\[
             2241+2(1879)=5999
               =3069+2(1465),                       \tag{7.11g}
\]

so every required scalar endpoint and degree equation closes exactly.  The
`4534` repeat edges realizing it are not yet selected.  The earlier
single-worker `249477`-variable run ending `UNKNOWN` is superseded by this
literal certificate; it was not a negative result.

### 7.2 Exact alternating-switch normal form

Let `G` be the bipartite graph whose left shore is the `8164` residual
lower rows and whose right shore is the surviving rank-eight labels.  A
candidate edge `e` additionally carries its physical endpoint pair
`partial(e)={x_e,y_e}`, its type `BU` or `UU`, and, in the `BU` case, its
forced boundary rank-nine label.

Fix any left-perfect, right-simple selection `M`.  If `M'` is another such
selection, every left vertex has degree zero or two in the symmetric
difference `M triangle M'`, whereas every right vertex has degree zero, one,
or two.  Hence every nontrivial component is an alternating even cycle or
an alternating path whose two ends are right labels in
`Q(M) triangle Q(M')`.  Conversely, toggling any compatible collection of
such cycles and paths gives another left-perfect, right-simple selection.
Thus alternating cycles together with free-right alternating paths form an
exact move basis for the row/rank-eight matching fibre.

For an oriented alternating component `P`, its physical load and type
changes are

\[
 \Delta_P(v)=
  \sum_{e\in P\setminus M}{\bf1}_{v\in\partial e}
  -\sum_{e\in P\cap M}{\bf1}_{v\in\partial e},       \tag{7.12}
\]

\[
 \Delta_P b=
  |(P\setminus M)\cap BU|-|(P\cap M)\cap BU|.       \tag{7.13}
\]

A toggle preserves the residual capacity face exactly when the updated
base loads are at most one, unused loads are at most two, the updated `b`
lies in (7.11d), and its forced boundary-turn labels remain simple.  Formulae
(7.12)--(7.13) make this a finite signed circulation test; no scalar
`b=6134` constraint is legitimate.

The matching-fibre description is exact but the turn condition is
quadratic.  If an unused vertex `v` has selected load two, its two incident
provider edges force an ordered local wedge.  It is legal precisely when
the two other endpoints are distinct, their central union has rank nine,
any two old-base neighbours belong to different contracted blocks, and
the resulting local boundary/central turn labels are distinct.  Write
`tau_v` for its central rank-nine label.  Global provider-turn legality
additionally requires all `tau_v` to be distinct and disjoint from the
forced boundary-turn bank.

For the zero-excess selection (7.11e), exactly `17` of the `5511` load-two
unused vertices force illegal wedges.  Among the other `5494` wedges there
are `3991` distinct central labels, hence

\[
                     5494-3991=1503               \tag{7.14}
\]

central repetition units; `261` of those distinct central values also lie
in the boundary bank.  Therefore the exact forced central-turn overload is

\[
                         1503+261=1764.             \tag{7.15}
\]

An alternating toggle changes wedge states only at unused vertices incident
with a toggled provider edge.  Consequently the pair

\[
       \Phi(M)=\bigl(I(M),C(M)\bigr),                \tag{7.16}
\]

where `I` counts illegal forced wedges and `C` counts central repetition
plus central/boundary collision units, has a literal local signed update on
every alternating path or cycle.  For the frozen certificate,

\[
                         \Phi(M)=(17,1764).          \tag{7.17}
\]

This is the correct next switch objective.  It is not an ordinary min-cut:
`tau_v` is attached to an unordered *pair* of selected provider edges at
`v`.  A row/rank-eight Hall cut alone cannot certify or refute turn
feasibility.  A provider-stage turn solution is equivalent to a compatible
alternating path/cycle packet with zero endpoint excess and
`Phi=(0,0)`.  Even such a packet would still leave the `4534` repeat edges,
their new turns, and the one-path topology to be constructed.

The symbolic direct bank (6.4) differs from the frozen `7abcbd84...` bank
on 24 rows.  Its residual row-type census is the same, but the particular
zero-excess selection above has not been transported to that bank and is
not claimed for it.

Thus neither the scalar ledger nor endpoint-type capacity obstructs the
adjacent seed, and the entire mandatory direct face plus the residual
provider b-capacity face is solved explicitly.

The live correlated target is now precise: retain the `572` direct ears,
choose the `9631` singleton owners, orient and order the resulting `3068`
blocks, and choose the `12698` long-ear edges so that

* every one of the remaining `8164` missing lower colours occurs;
* exactly `4534` further edges carry repeated lower colours;
* all new rank-eight unions are globally fresh and distinct;
* the inter-block graph is one path; and
* every forced rank-nine turn, and every higher protected window required
  downstream, is globally compatible.

The exact next theorem is now a turn-aware alternating-circuit/repeat-edge
completion: first eliminate (7.17) inside the zero-excess provider fibre,
then choose the `4534` repeat edges so that all `9631` selected unused
vertices have degree two, every new turn is private, and the contracted
graph is one component path.

## 8. Why `s` and `17-s` agree

Rotate coordinates by

\[
                         R_s(i)=i-s\pmod {17}.         \tag{8.1}
\]

Pivot equivariance gives

\[
              R_s(p_a(C))=p_{a-s}(R_sC).              \tag{8.2}
\]

Thus `R_s` sends the two cut starts `(0,s)` to `(17-s,0)`.  Since (0.1)
is an undirected edge, swapping its two rails gives the construction with
starts `(0,17-s)`.  Coordinate rotation preserves intersections, unions,
ranks, component incidence, endpoint classes, wedges, support peeling, and
matching.  Hence the complete scalar row at `s` equals that at `17-s`, and
the explicit `s=1` matching transports to `s=16`.

## 9. Exact scope and artifacts

The positive verdict is precisely

> the adjacent cyclic cuts `s=1,16` have a literal residual provider
> transversal with zero base/unused endpoint excess, globally distinct
> rank-eight labels, and globally distinct forced boundary rank-nine labels.

It is not a solution of the full edge/wedge resource hypergraph.  The exact
remaining forced provider defects are the `17` illegal load-two wedges and
`1764` central-turn collision units in (7.17).  Repeat edges, central turns,
component topology, higher shadows, residence and compilation remain open.

Artifacts:

* shift-parametric generator:
  `scratch/h2_scan_k17_cyclic_supported_ear_hall_20260731.cpp`;
* sweep replay:
  `scratch/audit_k17_gk_cyclic_cut_supported_ear_sweep_20260731.py`;
* compact 16-shift payload:
  `scratch/k17_gk_cyclic_cut_supported_ear_sweep_20260731.audit.json`;
* explicit positive matching:
  `scratch/k17_gk_cyclic_cut_s1_supported_provider_matching_20260731.tsv`;
* independent materialized-wedge verifier:
  `scratch/h2_verify_k17_shift1_supported_hall_materialized_20260731.cpp`;
* independent materialized replay:
  `scratch/k17_gk_cyclic_cut_s1_materialized_wedge_replay_20260731.audit.json`;
* exact direct-bank solve and residual census:
  `scratch/independent_k17_gk_shift1_exceptional_bb_solver_20260731.audit.json`;
* conditioned radius-three support replay:
  `scratch/audit_k17_gk_shift1_conditioned_standard_support_radius3_20260731.py`
  and
  `scratch/k17_gk_shift1_conditioned_standard_support_radius3_20260731.audit.json`;
* residual type/capacity model audit:
  `scratch/threadD_k17_s1_stageB_residual_provider_capacity_20260731.model.audit.json`;
* exact residual capacity certificate and independent replay:
  `scratch/independent_k17_gk_shift1_residual_cap_20260731.tsv`,
  `scratch/independent_k17_gk_shift1_residual_cap_solver_20260731.audit.json`,
  and
  `scratch/independent_k17_gk_shift1_residual_cap_replay_20260731.audit.json`;
* combined direct-plus-residual certificate and independent audit:
  `scratch/k17_gk_adjacent_cut_bcap_certificate_20260731.tsv`,
  `scratch/k17_gk_adjacent_cut_bcap_combined_20260731.audit.json`, and
  `scratch/k17_gk_adjacent_cut_bcap_certificate_20260731.independent.audit.json`.

The symbolic formulas and their agreement with the frozen sweep are checked
separately by
`scratch/audit_k17_gk_cyclic_cut_symbolic_theorem_20260731.py` and
`scratch/k17_gk_cyclic_cut_symbolic_theorem_20260731.audit.json`.

The principal bindings are: provider relation SHA
`6b2d9802d028cca79064278a65020d8ec28e3cc1b04d59c518d29b66b1a68e97`,
direct solution SHA
`7abcbd84c926a4b6fb7154b2b2554d07282508eae10e7b411e2b9a2217231b8d`,
symbolic-audit payload
`7d54232911b66f2241a06b6803130184a3b5439edff6c5c436468c5a44650ca1`,
and conditioned-support payload
`23dd87dc551125260f1705546ab6e87a39106a420adb2a1556a3d24573d1573f`.

The audit JSON contains the full component histograms, protected-width
rows, catalogue counts, matching ranks, and raw per-shift replay hashes.
