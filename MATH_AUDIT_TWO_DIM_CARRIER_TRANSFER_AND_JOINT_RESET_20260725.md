# Audit of the record-maximum carrier transfer and the exact two-phase reset boundary

Date: 2026-07-25  
Method: pure mathematics only; no computation or search

## 0. Verdict

The record-maximum transfer in
`PBBS_TWO_DIM_CARRIER_TRANSFER_COUNTEROBSTRUCTION_20260725.md` is correct
after the two local wording corrections already made in that file:

* the uniform bound for the extension mass is
  \(2/3\le\Xi_{\ell,J}\le3/2\), not (4/3);
* the reverse of a downward first-passage word need not first attain its
  minimum at its endpoint.  It is a **record-reset word**: every prefix
  stays above the terminal minimum and the endpoint is a minimum.  This is
  exactly what the reset proof uses.

The exact one-pair matrix is

\[
 \mathsf R_{p,p}=zC_A C_p,
 \qquad
 \mathsf R_{p,q}=zC_A(C_q-C_{q-1})y^{q-p}quad(q>p),\tag{0.1}
\]

and zero below the diagonal.  Its powers and resolvent are

\[
 (\mathsf R^k)_{p,q}
 =\begin{cases}
 (zC_A C_p)^k,&q=p,\\
 (zC_A C_q)^k-(zC_A C_{q-1})^k,&q>p,
 \end{cases}                                      \tag{0.2}
\]

with the factor (y^{q-p}) in the second line, and

\[
 [(I-\mathsf R)^{-1}]_{p,q}
 =\begin{cases}
 (1-zC_A C_p)^{-1},&q=p,\\
 \bigl((1-zC_A C_q)^{-1}
 -(1-zC_A C_{q-1})^{-1}\bigr)y^{q-p},&q>p.
 \end{cases}                                      \tag{0.3}
\]

At (z=1/4), every prescribed positive displacement has Green mass at
most one, while the saturated zero-displacement state has mass

\[
 {1\over1-\rho_{s,u}(1/4)}
 ={(u+1)(s-u+2)\over s+2}=\Theta(s)                \tag{0.4}
\]

for a central seam.

The physical source/sink telescope is also exact.  In reverse corridor
order, the first outer word resets the incoming record to zero, and the
last outer word resets every possible terminal record.  Hence

\[
 \boxed{
 e_0^{\!*}(I-\widehat{\mathsf R}(z;1))^{-1}{\bf1}
 ={1\over1-zC_b(z)C_A(z)}
 ={1\over1-\rho_{s,u}(z)}.}                        \tag{0.5}
\]

There is an exact marked refinement.  The middle renewal segment ending
at record (q) contributes (y^q).  The final reset of depth (A+1)
contributes the remaining displacement (A+1-q).  Therefore

\[
 \boxed{
 e_0^{\!*}(I-\widehat{\mathsf R}(z;y))^{-1}
 \bigl(y^{A+1-q}\bigr)_{q=0}^{A+1}
 ={y^{A+1}\over1-\rho_{s,u}(z)}.}                 \tag{0.6}
\]

Thus the complete physical corridor has deterministic total reset
displacement and no Fourier decay at all.  The triangular eigenvalues are
independent of (y), and the physical boundary vectors restore the full
scalar Green mode rather than suppressing it.  Formula (0.6) starts after
the initial reset.  If the incoming record before that reset is (p), its
additional displacement is (b-p), so the complete corridor carries the
fixed marker (y^{b-p+A+1}).

For two or more transported phases, intersecting the complete reset sink
projectors gives no gain.  This statement does not require a common
renewal atomization: every joint record state which is actually realized
is accepted coordinatewise.  Interlacing can help only by reducing the
language of words satisfying the transported equation

\[
 \mathcal A_{t,u}R_t=R_u\mathcal C_{t,u},           \tag{0.7}
\]

not through an intersection of record-state sinks.  With a common
atomization, the product-record Möbius telescope proves that even this
joint accepted mass is exactly the scalar Green series.  For genuinely
interlaced atomizations, the exact unresolved object is the compatible
word language of (0.7), not another product of reset projectors.

This is a theorem-level no-go for the local record/Fourier shortcut, not
for coefficient one.

## 1. Fixed-prefix and extension calculations

Consider blocks (D_i) of caps (L+i), with critical Boltzmann weights.
For a legal prefix (w), let (a) be its number of record-minimum
delimiters, let (y=\operatorname{net}(w)), and put (p=a+y).  The
completion of the current block is

\[
 R_{L+a,p}(x)
 ={x^pQ_{L-y}(x^2)\over Q_{L+a+1}(x^2)}.           \tag{1.1}
\]

The fixed nonseparator bits contribute (x^{|w|-a}), while the first
(a) block partition functions telescope to

\[
 \prod_{i=1}^{a}C_{L+i}(z)
 ={Q_{L+1}(z)\over Q_{L+a+1}(z)}.                  \tag{1.2}
\]

Division and evaluation at (x=1/2) give

\[
 \Pr(\mathscr D_L\text{ begins with }w)
 =2^{1-|w|}{L-y+1\over L+2}.                       \tag{1.3}
\]

This confirms that separator depth itself contributes no first-hit loss.
For a balanced boundary (B) of length (2\ell) and the appended word
(\operatorname{rev}(S)0), the ratio of (1.3) for the two prefixes is

\[
 2^{-|S|-1}{\ell+2\over\ell+1}.                   \tag{1.4}
\]

Summing over (S) of height at most (J) gives

\[
 \Xi_{\ell,J}
 ={(\ell+2)(J+1)\over(\ell+1)(J+2)}.              \tag{1.5}
\]

Both factors in (1.5) are monotone in their own variable, so

\[
 {2\over3}\le\Xi_{\ell,J}\le{3\over2}.            \tag{1.6}
\]

The upper endpoint is approached with \(\ell=1,J\to\infty\); hence
(3/2) is sharp under only \(\ell,J\ge1\).

## 2. The running-maximum matrix

One lower/upper seam pair has word

\[
 L\,1\,U\,0.
\]

If the complemented lower loop has exact depth (h), an incoming record
(p) becomes

\[
 p'=\max(p,h).                                     \tag{2.1}
\]

The exact-height lower-loop series is

\[
 C_h-C_{h-1},\qquad C_{-1}=0.                     \tag{2.2}
\]

Summing (2.2) over (h\le p) gives (C_p), proving (0.1).  After (k)
pairs the record is the maximum of the incoming value and the (k)
depths.  The series for final record at most (q) is therefore

\[
 (zC_A C_q)^k.                                    \tag{2.3}
\]

Subtracting the corresponding expression at (q-1) proves (0.2), and
summing in (k) proves (0.3).

At the critical point,

\[
 \lambda_q:=zC_A C_q
 ={(A+1)(q+1)\over(A+2)(q+2)}.                    \tag{2.4}
\]

Consequently

\[
 {1\over1-\lambda_p}
 ={(A+2)(p+2)\over A+p+3}\le p+2,                \tag{2.5}
\]

and for (q>p),

\[
 {1\over1-\lambda_q}-{1\over1-\lambda_{q-1}}
 ={(A+2)(A+1)\over(A+q+3)(A+q+2)}\le1.           \tag{2.6}
\]

These are exact; no asymptotic estimate is used.

## 3. Physical reset and the marked telescope

Let a word (F_d) start at its top wall, stay between heights (-d) and
zero, and end at (-d), with no earlier assumption needed here.  Every
prefix of (\operatorname{rev}F_d) is a suffix of (F_d), and therefore
has net height at least (-d); its endpoint has height (-d).  If the
incoming record height is (p\le d), appending
(\operatorname{rev}F_d) lowers the global minimum by (d-p) and leaves
the final record height zero.  This proves the reset property without the
false claim that the terminal minimum is first attained at the endpoint.

For a seam with (A=s-u) and (b=u-1), the reversed corridor is

\[
 \operatorname{rev}F_b\,
 \prod_i(0\operatorname{rev}U_i1\operatorname{rev}L_i)\,
 0\operatorname{rev}F_A.                           \tag{3.1}
\]

The first factor resets every incoming record (p\le b) to zero.  A
middle pair has depth in ({1,\ldots,A+1}), and the final factor resets
every resulting record (q\le A+1).  The reverse one-pair eigenvalues are

\[
 \widehat\lambda_q=zC_bC_{q-1},
 \qquad1\le q\le A+1,
 \qquad\widehat\lambda_0=0.                       \tag{3.2}
\]

Starting from zero, the exact-state Green entries telescope:

\[
 \widehat G_{0,0}=1,
 \qquad
 \widehat G_{0,q}
 ={1\over1-\widehat\lambda_q}
 -{1\over1-\widehat\lambda_{q-1}}.               \tag{3.3}
\]

Summing all states gives

\[
 \sum_{q=0}^{A+1}\widehat G_{0,q}
 ={1\over1-zC_bC_A},                               \tag{3.4}
\]

which is (0.5).

For the marked identity, the middle transition from record zero to (q)
has marker (y^q).  The final reset has displacement (A+1-q), so its
marker is (y^{A+1-q}).  Multiplication makes every summand in (3.4)
carry the same marker (y^{A+1}), proving (0.6).  Thus the physically
completed displacement distribution is a point mass, not a diffusive
law.

## 4. Two transported phases

For phases (t<u), the exact transported tail equation is

\[
 \mathcal A_{t,u}R_t=R_u\mathcal C_{t,u},          \tag{4.1}
\]

where

\[
 \mathcal A_{t,u}
  =(\overline T_{u-1}0)\cdots(\overline T_t0),
 \qquad
 \mathcal C_{t,u}
  =(0S_u)\cdots(0S_{t+1}).                        \tag{4.2}
\]

Give every compatible common word its deterministic pair of record states
((q_1,q_2)).  The external first-passage reset for phase (i) accepts
every (q_i) up to its physical strip depth (B_i).  If
(Q_{\rm real}) is the set of pairs actually realized by compatible
words, then

\[
 Q_{\rm real}\subseteq
 \{(q_1,q_2):0\le q_i\le B_i\}.                   \tag{4.3}
\]

The intersection of the two physical sink conditions accepts every state
in (Q_{\rm real}).  It is not asserted that the whole Cartesian
rectangle is realized.

This gives the following general identity.  Let \(\mathscr L_{t,u}\) be
the language of renewal words satisfying (4.1), and partition it by its
joint terminal record state:

\[
 \mathscr L_{t,u}=\bigsqcup_q\mathscr L_{t,u}(q).
\]

Then, with (w(\omega)) denoting the literal word weight,

\[
 \boxed{
 \sum_q\sum_{\omega\in\mathscr L_{t,u}(q)}w(\omega)
 =\sum_{\omega\in\mathscr L_{t,u}}w(\omega).}     \tag{4.4}
\]

Equation (4.4) is tautological but decisive: intersecting complete reset
projectors cannot reduce mass.  It remains true when the two renewal scans
interlace and no common atomization exists.

If the two scans do have a common atomization, assign each atom its vector
of record depths (h(\omega)), and put

\[
 K(q)=\sum_{\omega:h(\omega)\le q}w(\omega).       \tag{4.5}
\]

Coordinatewise maxima and product-poset Möbius inversion give the exact
state Green function

\[
 G(q)=\sum_{r\le q}{\mu(r,q)\over1-K(r)}.          \tag{4.6}
\]

Summing the full reset rectangle cancels every term except its top:

\[
 \boxed{
 \sum_qG(q)={1\over1-K(B)}.}                       \tag{4.7}
\]

When the common atoms exhaust the scalar one-pair language,
(K(B)=\rho_{s,u}), so (4.7) is again the scalar
(1/(1-\rho_{s,u})=\Theta(s)) Green mass.

For genuinely interlaced scans, (4.4) shows that the reset projectors
still give no gain.  The sole possible gain is now precisely

\[
 \sum_{\omega\in\mathscr L_{t,u}}w(\omega)
 =o\!\left({1\over1-\rho_{s,u}}\right),            \tag{4.8}
\]

an estimate on solutions of the transported word equation itself.  It
cannot be obtained by multiplying or intersecting the two all-state reset
vectors.

### 4.1 The exact nonoverlap solution of the transported equation

There is a large sector in which even the word equation leaves the scalar
mode unchanged.  Put

\[
 d=u-t,
 \qquad
 A=\mathcal A_{t,u},
 \qquad C=\mathcal C_{t,u}.
\]

Every block in either collar has net (-1), so

\[
 \operatorname{net}(A)=\operatorname{net}(C)=-d.  \tag{4.9}
\]

Assume the nonoverlap inequalities

\[
 |R_u|\ge|A|,
 \qquad |R_t|\ge|C|.                              \tag{4.10}
\]

The two differences in (4.10) are equal by the length of (4.1).  Prefix
and suffix cancellation in the free monoid gives a unique common middle
word (Z):

\[
 \boxed{R_u=AZ,
 \qquad R_t=ZC.}                                   \tag{4.11}
\]

Indeed the first (|A|) letters on the two sides of (AR_t=R_uC)
force (R_u=AZ), and left cancellation then gives (R_t=ZC).

Both (R_t) and (R_u) are terminal middle words which, in their native
phase, run from height (s) to height one and stay in ([1,s]).  In the
(R_t)-reading, (Z) starts at height (s).  In the (R_u)-reading it
starts after the net-(-d) word (A), hence at height (s-d).  Therefore
every prefix net height (H_Z) satisfies

\[
 1-s\le H_Z\le0,
 \qquad
 1-(s-d)\le H_Z\le d.
\]

Their intersection is

\[
 -(s-d-1)\le H_Z\le0.                              \tag{4.12}
\]

Since (R_t=ZC) and (C) has net (-d),

\[
 \operatorname{net}(Z)=d+1-s=-(s-d-1).            \tag{4.13}
\]

Consequently, after a vertical shift, (Z) is exactly a corridor from
height

\[
 S:=s-d-1                                             \tag{4.14}
\]

to zero, confined to ([0,S]).  Its generating function is

\[
 \boxed{G_S(x)={x^S\over F_{S+1}(x^2)}.}           \tag{4.15}
\]

Conversely, suppose explicitly that (A), when started at height (s),
is legal down to height (s-d), and that (C), when started at height
(d+1), is legal down to height one.  For such fixed legal collars, every
such (Z) makes both concatenations in (4.11) legal terminal corridors.
Thus (4.15) is the exact common-middle language of this nonoverlap sector,
not merely an upper bound.  Scalar cap conditions on (A,C) alone would
not imply these based legality conditions.

At the critical point,

\[
 G_S(1/2)={2\over S+2},
 \qquad
 {G_S(1/2)\over G_s(1/2)}={s+2\over s-d+1}.        \tag{4.16}
\]

If (d\le(1-\varepsilon)s), this ratio is bounded above and below by
positive constants.  Marking any seam whose two distances from the walls
are proportional to (S), its scalar renewal Green mass is

\[
 { (v+1)(S-v+2)\over S+2}=\Theta_\varepsilon(s).  \tag{4.17}
\]

Hence two transported phases with fixed or proportional separation do not
remove the diagonal mode on the complete nonoverlap sector.  Any two-phase
gain must be charged to genuinely overlapping/interlaced solutions of
(4.1), or to additional PBBS chronology which makes the legal common
middle (Z) sparse.

### 4.2 Complete free-monoid dichotomy and the overlap bridge

The complementary word-equation sector also has an exact canonical form.
Define

\[
 \Delta:=|R_u|-|A|=|R_t|-|C|.                     \tag{4.18}
\]

The equality of the two expressions follows from (AR_t=R_uC).

* If \(\Delta\ge0\), Section 4.1 gives the unique common middle (Z) of
  length \(\Delta\).
* If \(\Delta=-r<0\), there is a unique overlap word (H) of length (r)
  such that

  \[
   \boxed{A=R_uH,
   \qquad C=HR_t.}                                 \tag{4.19}
  \]

Indeed (R_u) is then the prefix of (A) of length (|A|-r); write
(A=R_uH), substitute in (AR_t=R_uC), and cancel (R_u).

The overlap bridge has a forced large net height.  Since

\[
 \operatorname{net}(A)=\operatorname{net}(C)=-d,
 \qquad
 \operatorname{net}(R_t)=\operatorname{net}(R_u)=1-s,
\]

equation (4.19) gives

\[
 \boxed{
 \operatorname{net}(H)=s-d-1=S.}                 \tag{4.20}
\]

Consequently

\[
 r\ge S,
 \qquad r\equiv S\pmod2.                         \tag{4.21}
\]

Thus the genuinely overlapping two-phase sector is not an unspecified
interlacing error: it is exactly the sector in which a suffix of the dual
collar (A) and a prefix of the forward collar (C) share one
positive-net bridge of height (S=s-(u-t)-1).  The remaining two-phase
statement can be written precisely as a coefficientwise bound for these
bridges, with the common word counted once.  The nonoverlap theorem shows
that no gain is available outside this bridge sector.

## 5. Exact scope

The loop decomposition, running-maximum update, marked triangular matrix,
and source/sink reset are exact for the unrestricted literal seam corridor.
In the increasing-cap chamber they form a coefficientwise upper language
for actual PBBS carriers.  They do not impose the complete inter-time
canonical (\tau\)-chronology, quotient-edge-disjoint packing, or every
transported equation simultaneously.

Accordingly:

* the one-phase record/Fourier shortcut is rigorously closed;
* finitely many common-atom record phases are also closed by (4.7);
* for genuinely interlaced phases, the remaining theorem is the weighted
  word-equation estimate (4.8), with all outer bits counted once.

No constant-one conclusion is made.
