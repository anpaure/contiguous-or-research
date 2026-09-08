# A multiscale ceiling for the direct label-lift/ABKV queue certificate

This note concerns only the following architecture.

* A selected object is a genuine queue atom with `H` middle starts.
* It certifies some (possibly rank-dependent) number of masks in each signed
  depth row.
* Different atom types, run lengths, maximum radii, and quota profiles may be
  mixed.
* The certified occurrences have total duplicate and missing defect `o(W)`.
* The atom words have total reset cost `o(W)`.
* The rounding proof uses the same Poisson sparsification, balanced label
  lift, and the displayed quantitative Alon--Bollobas--Kim--Vu matching
  estimate used in the proved growing-depth queue theorem.

The result below is a ceiling for that **direct ABKV certificate**, not a
nonexistence theorem for large matchings or for multiscale queue packings.
It shows that merely mixing values of `(h,H)`, or replacing full dummy rows by
rank-dependent slot quotas, does not enlarge the depth certified by this
particular one-shot black-box argument.  A structured matching theorem,
absorber, shared reset, or other information about the actual matching lies
outside the statement.

Throughout,

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 \rho_q=N_q/W,
\]

and

\[
 L=\log m,\qquad \ell=\log L.
\]

## 1. Abstract multiscale queue ledger

Index the atom types by `j`.  A type-`j` atom has

* `H_j` middle starts;
* maximum advertised radius `d_j`;
* `a_{j,q}` certified lower slots at depth `q`, where
  `0 <= a_{j,q} <= H_j` and `a_{j,q}=0` for `q>d_j`.

The upper slots can only increase the edge uniformity, so using just the lower
slots makes the forthcoming obstruction stronger.  Put

\[
 r_{j,q}=\frac{a_{j,q}}{H_j},\qquad
 s_j=\sum_{q=1}^{d}r_{j,q}.
\tag{1}
\]

Then `0 <= s_j <= d_j`.

Suppose `p_j` atoms of type `j` are selected and put

\[
 w_j=\frac{p_jH_j}{W}.
\tag{2}
\]

Allow certified duplicates.  Let `D_0,M_0` be the middle duplicate and
missing counts, and let `D_q,M_q` be the corresponding counts in the lower
depth-`q` row.  The exact certified-mask identity is

\[
 T_q=N_q+D_q-M_q.
\tag{3}
\]

Consequently,

\[
 \sum_j w_j=1+\frac{D_0-M_0}{W}
\tag{4}
\]

and

\[
 \sum_jw_jr_{j,q}
 =\rho_q+\frac{D_q-M_q}{W}.
\tag{5}
\]

Assume

\[
 D_0+M_0+\sum_{q=1}^{d}(D_q+M_q)=o(W).
\tag{6}
\]

Define

\[
 S_d=\sum_{q=1}^{d}\rho_q.
\tag{7}
\]

Summing (5) and using (6) gives the exact aggregate quota relation

\[
 \sum_jw_js_j=S_d+o(1),
 \qquad
 \sum_jw_j=1+o(1).
\tag{8}
\]

In the architecture considered here, each atom is emitted with its own queue
initialization.  Its extra initialization/reset charge is at least a fixed
positive constant times `d_j`; resets are not shared between atoms.  Thus a
necessary condition for total word length `W+o(W)` **inside this
architecture** is

\[
 \varepsilon_m:=\sum_jw_j\frac{d_j}{H_j}=o(1).
\tag{9}
\]

Let `K_j` be the uniformity after any dummy completion, padding, and
one-vertex label lift.  The `H_j` middle masks and the certified lower masks
are assumed to be distinct vertices of the augmented edge, as they are for
the queue intervals used in the proved construction.  Even if unused dummy
slots are completely removed, the edge therefore contains all its middle and
certified lower slots, so

\[
 K_j\ge H_j(1+s_j)\ge H_js_j.
\tag{10}
\]

Padding, upper slots, and the label vertex only increase `K_j`.

### Direct-certificate hypotheses

The capacity calculation below needs only the ledger above.  The later ABKV
ceiling additionally concerns the following explicitly restricted proof
architecture.

* **(A1) Independent resets.**  The reset charge is the one just described;
  a long path sharing its initialization between nominal atoms is outside the
  theorem.
* **(A2) Balanced ordinary hypergraphs.**  Each ABKV application is to an
  ordinary uniform hypergraph obtained by balanced padding and a label lift.
  With maximum-degree parameter `D`, every nonexceptional old middle vertex
  has degree `(1-o(1))D`, and the total exceptional old-vertex count is
  `o(W)`.  Every edge retains its same-start middle/facet pairs.  Any cleaning
  used to remove parallel lifted edges deletes `o(DW)` such incidences in the
  joint case, and `o(D_jw_jW)` uniformly over the components retained in the
  componentwise budget.
* **(A3) Direct ABKV error budget.**  If an application has uniformity `K`,
  maximum codegree `C`, and degree parameter `D`, put
  
  \[
   b(K,C,D)=K\left(\frac{C\log(1+C)}D\right)^{1/(K-1)}.
  \tag{10a}
  \]
  
  Every claimed application satisfies the theorem's formal codegree and
  degree hypotheses.  The proof charges the displayed Theorem 3.9 guarantee
  `O(b(K,C,D)|V|)+|B|` and uses no additional information about the actual
  matching.
* **(A4) Uniformity bookkeeping.**  Either all types are balanced and padded
  into one common-`K` ABKV input, its type-incidence shares `theta_j` satisfy
  `sum_j |theta_j-w_j/sum_i w_i|=o(1)`, and the direct certificate requires
  `b(K,C,D)=o(1)`; or types are assigned disjoint ownership components.  In
  the latter case component `j` owns
  `(1-o(1))w_jW` middle vertices, is a near-regular `K_j`-uniform ABKV input,
  and the proof requires
  
  \[
    \sum_j w_j b(K_j,C_j,D_j)=o(1).
  \tag{10b}
  \]
  
  The total exceptional-set charge is `o(W)`.  An unpadded mixed-uniformity
  union is not an input to the quoted ABKV theorem.

These assumptions are satisfied by the one-scale quantitative queue proof.
They are not automatic consequences of the abstract occurrence ledger.

## 2. Capacity--reset inequality

### Theorem 1 (multiscale capacity--reset bound)

Under (1)--(10), if `K_* = sup_j K_j`, then

\[
 \boxed{
 (S_d+o(1))^2\le (1+o(1))\,\varepsilon_m K_* .
 }
\tag{11}
\]

In particular, a `W+o(W)` queue packing, for which
`epsilon_m=o(1)`, necessarily has

\[
 \boxed{K_*=\omega(S_d^2).}
\tag{12}
\]

#### Proof

For every type with `s_j>0`,

\[
 s_j
 =\sqrt{\frac{d_j}{H_j}}
  \sqrt{\frac{H_js_j^2}{d_j}}.
\]

Since `s_j<=d_j`,

\[
 \frac{H_js_j^2}{d_j}\le H_js_j\le K_j\le K_*.
\]

Weighted Cauchy--Schwarz, (8), (9), and (4) now give

\[
\begin{aligned}
 (S_d+o(1))^2
 &=\left(\sum_jw_js_j\right)^2\\
 &\le
 \left(\sum_jw_j\frac{d_j}{H_j}\right)
 \left(\sum_jw_j\frac{H_js_j^2}{d_j}\right)\\
 &\le
 \varepsilon_m K_*\sum_jw_j\\
 &=(1+o(1))\varepsilon_mK_*.
\end{aligned}
\]

This proves (11) and (12).  Notice that no common value of `H_j`, no common
maximum radius, and no full-row dummy padding was used.  Rank-dependent
quotas are already included in `r_{j,q}`.  QED

## 3. The quantitative ABKV window

For a balanced component satisfying (A2), the normalized old--old codegree
cannot be made super-polynomially smaller by label lifting.  In particular,
whenever a component certifies a proportion `r_{j,1}` of its first lower row,
a same-start middle/facet double count gives

\[
 \frac{C_j}{D_j}\ge (1-o(1))\frac{r_{j,1}}{m}.
\tag{13}
\]

Indeed, an edge has `H_j` distinct middle slots and `a_{j,1}` distinct
same-start nested middle/facet pairs.  If the component owns `V_{j,0}` middle
vertices, there are at most `mV_{j,0}` relevant nested pairs.  Near-regularity
gives `(1-o(1))D_jV_{j,0}` total middle incidences, so the average pair
codegree is at least

\[
 (1-o(1))\frac{D_jV_{j,0}}{mV_{j,0}}
 \frac{a_{j,1}}{H_j}
 =(1-o(1))\frac{D_jr_{j,1}}m.
\]

The maximum codegree is at least this average.  A label lift does not alter
old--old pair incidences, and the cleaning allowance in (A2) changes the
estimate only by `o(1)`.  In the common-`K` joint case, the same argument is
applied after summing over types; the activity ratio is

\[
 \bar r_1=\frac{\sum_jw_jr_{j,1}}{\sum_jw_j}=1-o(1)
\tag{13a}
\]

by (4)--(6), and hence `C/D >= (1-o(1))/m`.

For `K>4`, the explicit factor in the ABKV unmatched-vertex upper bound is

\[
 b_j:=b(K_j,C_j,D_j)
 =K_j
 \left(\frac{C_j\log(1+C_j)}{D_j}\right)^{1/(K_j-1)}.
\tag{14}
\]

Equation (13), `r_{j,1}=m^{-o(1)}`, and `C_j>=1` give

\[
 \frac{C_j\log(1+C_j)}{D_j}\ge m^{-1-o(1)}.
\tag{15}
\]

Therefore the **displayed expression** `b_j` can tend to zero only if

\[
 \log K_j-\frac{(1+o(1))L}{K_j}\longrightarrow-\infty.
\tag{16}
\]

In particular,

\[
 \boxed{K_j\le(1+o(1))\frac{L}{\ell}.}
\tag{17}
\]

The first-depth quota is asymptotically one in any near-lossless central-band
ledger.  More precisely, (4)--(6) and `rho_1=1-O(1/m)` imply that the total
weight of types with `r_{j,1}<1/2` is `o(1)`; this is proved explicitly below.
Thus the mass relevant to (8) cannot evade (15) by deleting the first row.

Equation (17) is a ceiling for what the quoted ABKV *bound certifies*.  It is
not asserted that a particular larger-uniformity hypergraph has no large
matching.  When (16) fails, the theorem's displayed upper bound is simply not
an `o(|V|)` certificate; it is not a lower bound on the actual residual.
The separate ABKV hypothesis

\[
 e^{2K_j}C_j\log D_j=o(D_j)
\]

only forces `K_j=O(L)` here.  The sharper `L/ell` ceiling comes from demanding
that the theorem's quantitative uncovered-vertex bound actually be `o(1)`;
merely satisfying its formal codegree hypothesis is not enough for the queue
ledger.

## 4. Multiscale ABKV ceiling

### Theorem 2

Suppose `d->infinity` and `d=o(sqrt(m))`.  Consider a multiscale,
rank-dependent queue ledger satisfying (6), (9), and the direct-certificate
hypotheses (A1)--(A4).  If the displayed ABKV error budget is `o(W)`, then

\[
 \rho_q
 =\exp\!\left(-\frac{q^2}m
 +O\left(\frac qm+\frac{q^3}{m^2}\right)\right)
 =1-o(1)
\]

uniformly for `q<=d`, and therefore

\[
 S_d=(1-o(1))d.
\tag{18}
\]

and

\[
 \boxed{d=o\!\left(\sqrt{\frac{\log m}{\log\log m}}\right).}
\tag{19}
\]

#### Proof

The binomial-ratio estimate gives (18).  We first identify the types carrying
almost all of the middle-start mass.

Let

\[
 \delta_1=\sum_jw_j(1-r_{j,1}).
\]

Equations (4)--(6) and `rho_1=1-O(1/m)` give `delta_1=o(1)`.  Let

\[
 G=\{j:r_{j,1}\ge1/2\}.
\]

Then

\[
 \sum_{j\notin G}w_j\le2\delta_1=o(1).
\tag{20}
\]

Since `s_j<=d`, the types outside `G` contribute only `o(d)` to
`sum_j w_js_j`.  Hence, by (8) and (18),

\[
 \sum_{j\in G}w_js_j=(1-o(1))d.
\tag{21}
\]

The large uniformity is not confined to a negligible-weight outlier.  From
(8), (18), and `sum_j w_j=1+o(1)`,

\[
 \sum_jw_j(d-s_j)=o(d).
\tag{23}
\]

Hence types with `s_j<d/2` have total weight `o(1)`.  For `d>0`, (8) makes
`epsilon_m>0`; put `a_m=epsilon_m^{-1/2}`.  Among the remaining types, those
with

\[
 H_j<\frac{a_md}{2}
\]

have `d_j/H_j>1/a_m` and therefore total weight at most
`a_m epsilon_m=sqrt(epsilon_m)=o(1)`.  Combining this with (20), types of
total weight `1-o(1)` simultaneously satisfy

\[
 r_{j,1}\ge\frac12,\qquad
 s_j\ge\frac d2,\qquad
 H_j\ge\frac{d}{2\sqrt{\varepsilon_m}},
\]

and consequently

\[
 K_j\ge H_js_j
 \ge\frac{d^2}{4\sqrt{\varepsilon_m}}
 =\omega(d^2).
\tag{24}
\]

Call this intersection of three good sets `G_*`.

In the common-padding case, Theorem 1 gives directly

\[
 K=\omega(d^2).
\tag{24a}
\]

The joint same-start count (13a) gives
`C log(1+C)/D >= m^{-1-o(1)}`.  Assumption (A4) requires the displayed factor
`b(K,C,D)` to be `o(1)`, so (16)--(17) imply

\[
 \omega(d^2)\le K\le(1+o(1))\frac L\ell.
\]

This is (19).

In the componentwise case, suppose instead that (19) fails along a
subsequence.  Then `d >= c sqrt(L/ell)` there for some fixed `c>0`.
Uniformly for `j in G_*`, (24) gives

\[
 K_j\ge \frac{c^2L}{4\ell\sqrt{\varepsilon_m}}
       =\omega(L/\ell).
\tag{24b}
\]

Equations (13) and (15) consequently give

\[
 \log b_j
 \ge \log K_j-\frac{(1+o(1))L}{K_j}
 \longrightarrow+\infty
\tag{24c}
\]

uniformly on `G_*`.  Since `sum_{j in G_*}w_j=1-o(1)`, the direct component
budget satisfies

\[
 \sum_jw_jb_j\ge\sum_{j\in G_*}w_jb_j\not=o(1),
\]

contrary to (10b).  This proves (19) in the componentwise case as well.  The
contradiction is a failure of the displayed ABKV **certificate budget**; it
does not assert a lower bound on the actual unmatched set.  QED

The proved quantitative queue theorem already reaches every diverging depth

\[
 d=o\!\left(\sqrt{\frac{\log m}{\log\log m}}\right)
\]

by taking

\[
 \omega=\frac{\log m}{d^2\log\log m}\longrightarrow\infty.
\]

Therefore it is order-optimal inside the direct one-shot certificate defined
by (A1)--(A4).  Within that certificate, mixing run lengths or using
nonconstant row quotas can change constants and lower-order factors, but not
the depth scale.

## 5. What stronger input is actually needed

The obstruction is not full dummy padding.  Remove every dummy and count only
the average number of real depth rows per middle start; that number is `S_d`.
The capacity--reset inequality still forces effective edge size
`omega(S_d^2)`.

At the reduced inner-wreath threshold

\[
 d=(1+o(1))\sqrt{m\log\log m},
\]

the Gaussian binomial profile gives

\[
 S_d
 =\sum_{q\le d}\rho_q
 =\left(\frac{\sqrt\pi}{2}+o(1)\right)\sqrt m.
\tag{25}
\]

Consequently any near-zero-reset one-shot queue rounding satisfying the
capacity and independent-reset assumptions above must handle

\[
 K=\omega(m),
\tag{26}
\]

whereas the normalized same-start codegree is at least `Theta(1/m)` (and the
available upper bound is typically `O(H/m)`).  No generic application of the
present ABKV estimate can enter this regime: its `1/(K-1)` exponent and
`exp(2K)` hypothesis both become vacuous.

A sufficient replacement black box would be the following structured
statement.

> **Hierarchical queue-rounding theorem.**  For the dummy-free (or
> quota-completed) monotone queue-profile fractional matching, with
> `S_d=Theta(sqrt(m))` and reset ratio `epsilon_m=o(1)`, select integral
> atoms whose certified duplicate-plus-missing total is `o(W)`, even though
> the augmented real incidence size is `K=omega(m)` and the full augmented
> universe has size `Theta(sqrt(m) W)`.

Equivalently, the theorem must leave an `o(1/sqrt(m))` fraction of that
augmented universe uncovered.  It must exploit the nested row/queue geometry
or round successive depth blocks while preserving common middle ownership.
A theorem depending only on maximum degree, maximum pair-codegree, and
uniformity is not the same missing ingredient; at `K=omega(m)` and normalized
codegree at least `Theta(1/m)`, the present generic nibble parameters are in
the wrong regime.

Here is one fully quantitative parameter target for that black box.  Take

\[
 d=(1+o(1))\sqrt{m\log\log m},\qquad
 H=\sqrt m\,f(m),
\]

where

\[
 \sqrt{\log\log m}\ll f(m)\ll\sqrt m.
\]

Then the literal reset ratio is

\[
 \frac dH=(1+o(1))\frac{\sqrt{\log\log m}}{f(m)}=o(1),
\]

the dummy-free expected real incidence size is

\[
 K_{\rm real}
 =H\left(1+2\sum_{q\le d}\rho_q\right)
 =\left(\sqrt\pi+o(1)\right)m f(m),
\tag{27}
\]

and the known weighted codegree upper bound is

\[
 \alpha=O(H/m)=O(f(m)/\sqrt m)=o(1).
\tag{28}
\]

The required conclusion is at most `o(W)` uncovered real masks out of

\[
 V_{\rm real}
 =\left(1+2\sum_{q\le d}\rho_q\right)W
 =\left(\sqrt\pi+o(1)\right)\sqrt m\,W.
\tag{29}
\]

Thus the least useful quantitative replacement must achieve relative error
`o(m^{-1/2})` for this structured incidence system at
`K_real=Theta(mf(m))`; merely proving an unspecified `o(1)` matching error is
not enough.

## Verdict

There is no asymptotic gain **certified by the direct one-shot ABKV budget
(A1)--(A4)** from a multiscale mixture of the currently proved queue atoms.
The existing depth `d=o(sqrt(log m/log log m))` is the ceiling of that formal
certificate, not a nonexistence result for larger matchings.  The next useful
input may be a hierarchical/common-ownership rounding theorem, an explicit
absorber, a shared-reset construction, or another argument whose error is
additive `o(W)` rather than the displayed generic ABKV residual.
