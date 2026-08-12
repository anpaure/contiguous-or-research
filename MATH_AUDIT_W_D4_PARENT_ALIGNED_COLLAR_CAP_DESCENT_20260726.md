# The complete `D_4` parent-aligned profile: collar survival, complementary repayment, and the exact cap boundary

Date: 2026-07-26

Method: pure mathematics only.  No search, computation, solver, or web input
is used.  The two displayed `D_4` path factors certified in
`MATH_THEOREM_D4_PAIR23_PORT_FACTOR_20260726.md` are taken as exact input;
all deductions below are literal incidence identities.

## 0. Verdict

Let `F` be the canonical MSW `D_4`-port factor and let `G` be the complete
noncanonical `D_4`-port factor from the cited certificate.  On

\[
 E_0=\{1,8\},\qquad E_1=\{2,3\},\qquad
 E_2=\{4,5\},\qquad E_3=\{6,7\},                       \tag{0.1}
\]

their distinguished first-insertion totals are

\[
             (5,5,2,2)\longrightarrow(5,5,1,3).       \tag{0.2}
\]

This projected statistic is genuine, but it is not the decisive parent
profile.  The exact conclusions are as follows.

1. On the six cyclic starts belonging to the open parent sector, the full
   singleton profiles are

   \[
   \boxed{
   u_F=(9,9,12,12,12,12,9,9),\qquad
   u_G=(9,11,9,12,12,9,13,9).}                         \tag{0.3}
   \]

   Hence

   \[
          d:=u_G-u_F=2e_2-3e_3-3e_6+4e_7,             \tag{0.4}
   \]

   whose pair-class projection is

   \[
                 \Pi d=-e_{E_1}+e_{E_3}.               \tag{0.5}
   \]

   Thus the four crossing collars do **not** cancel (0.2).  Together with
   the second intrinsic boundary start they concatenate the transfer into
   the stronger bridge `E_1 -> E_3`.

2. The other three cyclic starts have the opposite signed profile.  Their
   old and new histograms are

   \[
   \boxed{
   \begin{aligned}
   v_F&=(5,5,2,2,2,2,5,5,14),\\
   v_G&=(5,3,5,2,2,5,1,5,14),
   \end{aligned}}                                      \tag{0.6}
   \]

   and

   \[
                         v_G-v_F=-d.                   \tag{0.7}
   \]

   Therefore a common carrier for all nine cyclic starts gives exact
   singleton cancellation.  At the literal first matched parent the
   targets are singletons, so there is no nonempty exterior carrier and
   this common-carrier condition is automatic.  The complete affected
   histogram, and hence its cap defect for every cap and background, is
   exactly unchanged.  This is complementary-sector repayment, not
   crossing-collar repayment.

3. The six-start sector is not by itself a complete first-parent
   replacement.  At the isolated cap `p=9`, even this restricted sector
   has zero cap descent for every residual background: all its loads are
   at least nine, so every hinge is linear.  For `p>=13`, the same sector
   has a legitimate residual-capacity vector giving exactly six units of
   descent, but using it requires a higher or mixed context that also
   accounts for the changed complementary sector.  The difference is
   carrier and capacity placement, not integrality.

4. After a further outer lift, uniform full-cycle collar cancellation is
   no longer universal.  If `Delta_ell` is the aggregate signed profile of
   all nine starts whose local target is a cyclic interval of length
   `ell`, then

   \[
       \Delta_1=\Delta_4=\Delta_5=\Delta_8=0,           \tag{0.8}
   \]

   but

   \[
       \Delta_2\ne0,\quad \Delta_3\ne0,\qquad
       \frac12\|\Delta_2\|_1=19,\quad
       \frac12\|\Delta_3\|_1=22.                      \tag{0.9}
   \]

   The complementary upper profiles at lengths seven and six are nonzero
   as well.  Thus there is no exact higher-context collar invariant killing
   the `D_4` primitive.

5. What remains unproved is the coefficient-one statement.  A physical
   parent atlas must separate or otherwise route the two singleton sectors,
   or expose one of the nonzero length-two/three profiles, **and** its actual
   unaffected load must supply the favourable residual capacities at all
   protected depths simultaneously.  The finite `D_4` factor proves that
   this is possible at the level of an individual exact atom; it does not
   prove that the canonical global background realizes the required sign.

## 1. Exact six-start and three-start ledgers

For a rooted row with port `P`, write its Johnson geodesic as

\[
 X_t=(P\setminus\{a_1,\ldots,a_t\})
          \cup\{b_1,\ldots,b_t\},\qquad 0\le t\le4.    \tag{1.1}
\]

The associated cyclic coordinate word is

\[
                q=(a_1,a_2,a_3,a_4,b_1,b_2,b_3,b_4,9). \tag{1.2}
\]

The six starts meeting the open parent sector have singleton targets

\[
                         a_2,a_3,a_4,b_1,b_2,b_3,       \tag{1.3}
\]

while the complementary three starts have targets

\[
                              a_1,b_4,9.                \tag{1.4}
\]

For a fourteen-row factor `H`, let

\[
 A_H(x)=\#\{P:a_1^H(P)=x\},\qquad
 B_H(x)=\#\{P:b_4^H(P)=x\}.                            \tag{1.5}
\]

### Lemma 1.1 (sector identity)

The two sector histograms satisfy

\[
 \boxed{
 u_H(x)=14-A_H(x)-B_H(x)\quad(x\in[8]),\qquad
 v_H=A_H+B_H+14e_9.}                                  \tag{1.6}
\]

In particular

\[
                         u_H+v_H=14\sum_{x=1}^9e_x.    \tag{1.7}
\]

#### Proof

In every row (1.2) is a permutation of `[9]`.  Among coordinates `[8]`,
the six positions (1.3) omit exactly `a_1` and `b_4`; the three positions
(1.4) contain exactly those two coordinates and `9`.  Summing the literal
row identity over the fourteen ports proves (1.6)--(1.7). \(\square\)

For the canonical factor, the first-deletion and last-insertion counts are

\[
 A_F=5e_1+5e_2+2e_4+2e_6,
 \qquad
 B_F=2e_3+2e_5+5e_7+5e_8.                             \tag{1.8}
\]

For the new factor, direct reading of the displayed fourteen paths gives

\[
 \begin{aligned}
 A_G&=5e_1+2e_2+5e_3+e_4+e_6,\\
 B_G&=e_2+e_4+2e_5+4e_6+e_7+5e_8.
 \end{aligned}                                        \tag{1.9}
\]

Substitution of (1.8)--(1.9) into (1.6) proves (0.3), (0.4),
(0.6), and (0.7).  The masses audit as

\[
          |u_F|=|u_G|=84,\qquad |v_F|=|v_G|=42.        \tag{1.10}
\]

### Corollary 1.2 (where the pair bridge goes)

Let `q^+` denote the distinguished first-insertion start `b_1`.  Its pair
projection changes by

\[
                 \Pi(q_G^+-q_F^+)=-e_{E_2}+e_{E_3}.    \tag{1.11}
\]

The other five open-parent starts therefore change by

\[
 \Pi\bigl((u_G-q_G^+)-(u_F-q_F^+)\bigr)
                         =-e_{E_1}+e_{E_2}.             \tag{1.12}
\]

Consequently (1.11) and (1.12) concatenate exactly to (0.5).

If the second intrinsic boundary start `a_4` is separated as `q^-`, then

\[
                 \Pi(q_G^--q_F^-)=2e_{E_2}-2e_{E_3},  \tag{1.13}
\]

and the four crossing starts alone have

\[
                 \boxed{\Pi\Delta_{\rm cross}
                      =-e_{E_1}-e_{E_2}+2e_{E_3}.}     \tag{1.14}
\]

Thus every meaning of “the crossing collars cancel the marked bridge” is
false for this factor.  Cancellation occurs only after adding (1.4).

## 2. Exact singleton cap calculation

Fix an unaffected background `beta` on the physical images of the six
open-parent starts and put

\[
                         c_x=(p-\beta_x)_+.             \tag{2.1}
\]

The residual overload change is

\[
\boxed{
\begin{aligned}
 E_c(G)-E_c(F)
={}&(11-c_2)_+-(9-c_2)_+\\
 &+(9-c_3)_+-(12-c_3)_+\\
 &+(9-c_6)_+-(12-c_6)_+\\
 &+(13-c_7)_+-(9-c_7)_+.
\end{aligned}}                                        \tag{2.2}
\]

### Proposition 2.0 (complete literal first-parent cancellation)

For the complete nine-start singleton profile,

\[
                         u_F+v_F=u_G+v_G.              \tag{2.3}
\]

Consequently a literal matched first-parent substitution has zero change
in cap defect, and zero change in every statistic depending only on the
complete target histogram, for every cap `p` and every unaffected
background.

#### Proof

Equation (2.3) is (1.7) applied to `F` and `G` in the segment-aligned
nine-start model.  More invariantly, every exact ambient factor has the
same singleton point margin.  In a literal first-parent replacement all
slots outside the complete affected family are fixed; subtracting their
common histogram shows that the complete affected singleton histograms
are equal.  Adding an arbitrary common background preserves equality.
\(\square\)

### Proposition 2.1 (isolated `p=9` cancellation)

For every admissible residual vector `0<=c<=9`, the right side of (2.2)
is zero.

#### Proof

Every old and new load appearing in (0.3) is at least nine.  Therefore
`(h-c)_+=h-c` for each of them.  Both profiles have total mass 84, so
their linear hinge sums agree. \(\square\)

### Proposition 2.2 (sharp formal descent)

For `p>=13`, the admissible residual capacity `c=u_G` gives

\[
                         E_c(G)=0,\qquad E_c(F)=6.      \tag{2.4}
\]

No residual vector can produce a larger absolute change.

#### Proof

The vector `u_G` has maximum coordinate 13.  With `c=u_G`, the new defect
is zero and the old defect is the positive mass of `u_F-u_G=-d`, namely

\[
           \frac12\|d\|_1=\frac{2+3+3+4}{2}=6.        \tag{2.5}
\]

For each coordinate, the signed hinge difference has the same sign as the
corresponding coordinate of `d` and magnitude at most its absolute value.
Its total positive contribution is therefore at most the positive mass of
`d`, and its total negative contribution has magnitude at most the
negative mass of `d`.  Both masses equal six.  Equality in (2.4) proves
sharpness. \(\square\)

Proposition 2.2 is an admissible residual-capacity witness, not a claim
about the background generated by the global construction.

## 3. The occurrence-resolved collar criterion

Aggregating occurrences by their local coordinate before attaching
collars can lose essential information.  The correct functor is therefore
defined on occurrences.

Let

\[
 \Omega_U=\mathcal D_4\times\{2,3,4,5,6,7\},\qquad
 \Omega_V=\mathcal D_4\times\{1,8,9\}.                \tag{3.1}
\]

For `H in {F,G}`, let `t_H(P,j)` be the coordinate in position `j` of
`q_H(P)`.  An aligned outer context assigns to each occurrence `(P,j)` an
exterior carrier `O_(P,j)` and the inherited injection `iota` of the local
coordinates.  Its physical target is

\[
              \Phi_C(P,j,x)=O_{P,j}\mathbin{\dot\cup}\iota(x).    \tag{3.2}
\]

Such a separated-carrier target has physical rank `|O_(P,j)|+1`; when the
carrier is nonempty it is a higher or mixed context, not the literal
singleton rank of Proposition 2.0.

### Theorem 3.1 (exact parent-aligned singleton action)

The complete physical signed profile is

\[
\boxed{
 \Delta_C=
 \sum_{(P,j)\in\Omega_U\cup\Omega_V}
 \left(e_{\Phi_C(P,j,t_G(P,j))}
       -e_{\Phi_C(P,j,t_F(P,j))}\right).}              \tag{3.3}
\]

It cancels if and only if the signed measure in (3.3) is zero.

If all starts have one common exterior carrier, then (3.3) is the common
injection of `d-d=0`.  If the `U` starts have one common carrier, the `V`
starts have another common carrier, and the two physical target images are
disjoint, then

\[
          \Delta_C=\iota_U(d)-\iota_V(d),\qquad
          \frac12\|\Delta_C\|_1=12.                    \tag{3.4}
\]

In the situation of (3.4), for `p>=13` there is an admissible residual
vector giving six units of descent: use `c=u_G` on the `U` image and use
`c=0` on the `V` image.

#### Proof

Equation (3.3) is the literal target census, occurrence by occurrence.
When the carrier is common, summation over the slots can be performed
before the injection; Lemma 1.1 then gives `d` and `-d`.  Common-carrier
coincidence proves cancellation.  Under the stated two-carrier hypothesis,
the two injective images are disjoint, so their positive masses add and
(2.5) gives (3.4).  Proposition 2.2 gives six units on the `U` image.  The
zero residual capacity makes every hinge linear on the `V` image; its old
and new total masses are both 42, so its net change is zero. \(\square\)

The common-carrier hypotheses in the two specializations are essential.
For slot-dependent collars, neither `d` nor `-d` alone determines the
push-forward: one must retain (3.3).  In particular a map applied only to
the aggregated vector `d` is not a valid general substitute for the
occurrence tensor.

## 4. Full higher-context tensor

For `1<=ell<=8`, `j in Z_9`, and a row word `q`, put

\[
 I_{\ell,j}(q)=\{q_j,q_{j+1},\ldots,q_{j+\ell-1}\},     \tag{4.1}
\]

with cyclic indices, and define

\[
 \Delta_{\ell,j}
 =\sum_{P\in\mathcal D_4}
    \left(e_{I_{\ell,j}(q_G(P))}
          -e_{I_{\ell,j}(q_F(P))}\right),
 \qquad
 \Delta_\ell=\sum_{j\in\mathbb Z_9}\Delta_{\ell,j}.  \tag{4.2}
\]

For a uniform exterior carrier, (4.2) is exactly the complete all-start
profile at local target length `ell`.  With nonuniform carriers the
row-start-resolved version of (3.3), with `I_(ell,j)` in place of `t_H`,
is authoritative.

The exact ledgers of the two factors imply

\[
                 \Delta_1=\Delta_4=\Delta_5=\Delta_8=0.\tag{4.3}
\]

The first surviving lower profiles are

\[
\begin{aligned}
\Delta_2={}&
 2e_{14}+e_{25}+e_{26}+3e_{27}+e_{36}+e_{37}
 +2e_{47}+e_{48}+e_{58}+3e_{39}+3e_{69}\\
&-e_{12}-e_{13}-e_{23}-e_{24}-2e_{34}-e_{35}
 -2e_{46}-e_{56}-e_{67}-e_{68}-e_{78}-2e_{29}-4e_{79},
                                                               \tag{4.4}\\
\Delta_3={}&
 e_{127}+2e_{147}+e_{236}+e_{247}+e_{257}+e_{267}+e_{367}
 +e_{148}+e_{258}+e_{348}+e_{389}+e_{489}\\
&+2e_{259}+2e_{369}+e_{379}+e_{479}+e_{159}+e_{569}+e_{169}\\
&-e_{124}-e_{125}-e_{136}-e_{235}-e_{246}-e_{346}-e_{357}
 -e_{567}-e_{178}-e_{368}-e_{478}\\
&-e_{289}-e_{589}-e_{179}-e_{239}-2e_{279}-e_{349}
 -e_{149}-e_{459}-2e_{679}.                            \tag{4.5}
\end{aligned}
\]

Here, for example, `e_14` means the basis vector of target `{1,4}`.
The coefficient sums give

\[
 \sum_S(\Delta_2(S))_+=19,
 \qquad
 \sum_S(\Delta_3(S))_+=22,                             \tag{4.6}
\]

and the negative masses are the same.  Complementation gives the upper
profiles at lengths seven and six.

### Theorem 4.1 (exact cancellation classification for a uniform carrier)

For the certified pair `F,G`, the complete uniform-carrier all-start
profile cancels at lengths `1,4,5,8` and survives at lengths `2,3,6,7`.
At the first two surviving lengths its total variations are exactly 19 and
22 as in (4.6).

#### Proof

At length one, Lemma 1.1 gives `d-d=0`.  Length eight is its complement.
At lengths four and five, the cyclic intervals encode respectively the
complete `X`- and `Y`-ownership ledgers (up to complementation); both exact
factors enumerate the same shores, so their aggregate differences vanish.
Equations (4.4)--(4.5) are obtained by literal substitution of the two
displayed row-word tables into (4.2).  Their positive and negative
coefficient sums are respectively `19` and `22`, proving nonvanishing and
the asserted variations.  Complementing local targets proves the claims
at lengths seven and six. \(\square\)

### Corollary 4.2 (formal higher-context cap descent)

Let `u_F^(ell),u_G^(ell)` be the uniform-carrier full-cycle histograms at
length `ell=2` or `3`.  For `p>=126`, the residual capacity

\[
                         c=u_G^{(\ell)}                 \tag{4.7}
\]

is admissible and gives exact descent

\[
 \begin{array}{c|cc}
 \ell&E_c(G)&E_c(F)\\ \hline
 2&0&19\\
 3&0&22.
 \end{array}                                           \tag{4.8}
\]

#### Proof

Each histogram counts `14*9=126` occurrences, so every coordinate is at
most 126 and (4.7) is admissible.  The old defect at capacity `u_G` is the
positive mass of `u_F-u_G`, equal to the negative mass of `Delta_ell`.
Equation (4.6) gives (4.8). \(\square\)

Again, (4.8) proves cap-productivity of the exact local primitive for an
admissible capacity vector.  It does not manufacture that vector as the
unaffected load of the global exact factor.

## 5. Consequence for the early-scale hierarchy

The strict-interior erasure theorem remains untouched: a window swallowing
both fixed ports `P` and `J\P` has empty local intersection and cannot see
this or any other internal `D_s`-port substitution.  The `D_4` factor is
useful only when installed parent-aligned, so that the serviced windows
cut a flag or attach different carriers to the cyclic sectors.

For that surviving variant the present audit proves the following exact
boundary.

* The new factor is a legal integral exact-factor atom with fixed ports.
* Its distinguished pair transfer survives every crossing start belonging
  to the open parent sector and becomes (0.5).
* Every literal matched first parent cancels after the three complementary
  starts are included; this full-profile cancellation holds for every cap
  and background.
* A genuinely higher or mixed context with certified carrier separation
  exposes a six-unit singleton descent for a suitable admissible residual
  vector.
* A further lift exposing local target lengths two or three has a nonzero
  full-cycle profile even without carrier separation, and has the formal
  descents (4.8).

What is still missing is a theorem that the actual calibrated parent
catalogue supplies, on a product-compatible collection of integral atoms,
the carrier separation and residual capacities required by (3.3) and the
hinge inequality simultaneously over all protected depths.  Until that is
proved, (0.2) is a genuine orbit-crossing primitive and a refutation of
universal collar cancellation, but not an unconditional PCap descent and
not a proof of coefficient one.
