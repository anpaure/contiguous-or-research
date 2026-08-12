# The full moving-bank carousel spectrum and its exact upper-fusion gate

**Date:** 2026-08-07  
**Input:** `MATH_THEOREM_MOVING_BANK_SINGLE_BULGE_CAROUSEL_20260807.md`  
**Status:** theorem.  The complete cyclic interval-OR spectrum is computed.
After symmetric averaging at owner mass one, the carousel is exact at the
middle and (for \(d\ge3\)) immediate-upper ranks and has surplus at every internally
reachable higher rank.  Its internal support stops at rank
\(Q=s-1+Rd\).  Thus averaging individual carousels is globally
upper-complete if and only if \(Q=n\); at maximal aperture the only absent
ranks have codimension below the Euclidean remainder
\(c=n-s+1-Rd<d\).  Those top targets have a two-support seam
representation.  The load-bearing global obstruction is therefore an exact
pointwise immediate-upper-current condition on the cycle fusions.

## 1. Notation

Use

\[
 n=2m+1,
 \qquad D=d+1,
 \qquad s=m-2d,
 \qquad L=Rd,
\]

and the source word of the moving-bank theorem.  Put

\[
 \theta:=4\sum_{a\ge1}e^{-4\pi a^2}
          \approx1.395\times10^{-5},
\]

the asymptotic reset-bank density used below.  Also put

\[
 Z_j=\{z_{j,1},\ldots,z_{j,d-1}\},
 \qquad
 K_j=H_j\cup\{g_j\}
     =\{b_j,b_{j+1},\ldots,b_{j+d}\}.                \tag{1.1}
\]

The complete coordinate support of one carousel is

\[
 \Sigma=P\mathbin{\dot\cup}B\mathbin{\dot\cup}Z,
 \qquad
 Q:=|\Sigma|=s-1+Rd.                                 \tag{1.2}
\]

For \(1\le h\le R\), the union of \(h\) consecutive high banks is

\[
 K_{j,h}:=\bigcup_{u=0}^{h-1}K_{j+u},
 \qquad
 |K_{j,h}|=\min(R,d+h).                              \tag{1.3}
\]

All indices are cyclic.  A **proper cyclic arc** uses between one and
\(L-1\) consecutive source positions.

## 2. Complete literal spectrum

There are exactly three kinds of proper cyclic arc.

### Type 0: no high position

Such an arc lies in one low run.  For

\[
 1\le \ell\le d-1,
 \qquad 1\le a\le d-\ell,
\]

its target is

\[
 P\cup\{z_{j,a},z_{j,a+1},\ldots,z_{j,a+\ell-1}\},   \tag{2.1}
\]

of rank \(s-1+\ell\).

### Type I: between one and \(R-1\) highs

Let \(j\) be the first high and let \(h\) be the number of highs.  Let
\(\alpha\) be the number of low letters retained immediately before the
first high, and \(\beta\) the number retained immediately after the last:

\[
 0\le\alpha,\beta\le d-1.
\]

Define the suffix and prefix

\[
 Z^-_{j,\alpha}
   =\{z_{j-1,d-\alpha},\ldots,z_{j-1,d-1}\},
 \qquad
 Z^+_{j,\beta}
   =\{z_{j,1},\ldots,z_{j,\beta}\},                 \tag{2.2}
\]

with the empty-set convention at zero.  The target is exactly

\[
 \boxed{
 T(j,h,\alpha,\beta)=
 P\cup K_{j,h}\cup Z^-_{j,\alpha}
  \cup\bigcup_{u=0}^{h-2}Z_{j+u}
  \cup Z^+_{j+h-1,\beta}.}                           \tag{2.3}
\]

Its rank is

\[
 \rho_h+\alpha+\beta,
 \qquad
 \rho_h=s-1+(h-1)(d-1)+\min(R,d+h).                 \tag{2.4}
\]

### Type II: all \(R\) highs

The complementary gap contains no high, hence is a nonempty interval of
one low run.  If its length is \(g\), then

\[
 1\le g\le d-1,
\]

and the target is

\[
                         \Sigma-G,                  \tag{2.5}
\]

where \(G\) is that low interval.  Its rank is \(Q-g\).

The full cyclic word itself has target \(\Sigma\), of rank \(Q\).

### Theorem 2.1 (completeness)

Equations (2.1), (2.3), and (2.5) list every proper cyclic interval-OR
occurrence exactly once as an interval.  Different listed intervals may
have the same target after the bank union in (1.3) saturates; no quotient by
such target coincidences is being taken.

#### Proof

An arc containing no high lies uniquely in a low run, giving (2.1).  If it
contains \(1\le h<R\) highs, those highs are consecutive and have a unique
first member.  Between them lie \(h-1\) complete low runs; only a suffix
before and a prefix after may be partial.  This is exactly (2.3).  Finally,
an arc containing all highs has a proper complement with no high, hence a
low-run interval, giving (2.5).  These cases are disjoint and exhaustive.
\(\square\)

## 3. Exact occurrence enumerator

Put

\[
 c_t=\#\{(\alpha,\beta)\in\{0,\ldots,d-1\}^2:
                         \alpha+\beta=t\}
 =\begin{cases}
 t+1,&0\le t\le d-1,\\
 2d-1-t,&d\le t\le2d-2,\\
 0,&\text{otherwise}.
 \end{cases}                                         \tag{3.1}
\]

Let \(N_q\) be the number of proper cyclic interval occurrences whose OR
has rank \(q\).  The complete rank enumerator is

\[
 \boxed{
 \begin{aligned}
 \sum_qN_qx^q
  ={}&R\sum_{\ell=1}^{d-1}(d-\ell)x^{s-1+\ell}\\
    &+R\sum_{h=1}^{R-1}x^{\rho_h}
                     (1+x+\cdots+x^{d-1})^2\\
    &+R\sum_{g=1}^{d-1}(d-g)x^{Q-g}.
 \end{aligned}}                                      \tag{3.2}
\]

Indeed the coefficients in the three lines count respectively the low
segments, the choices of \((j,\alpha,\beta)\), and the complementary low
gaps.  Evaluating at \(x=1\) gives

\[
 R{d(d-1)\over2}+R(R-1)d^2+R{d(d-1)\over2}
 =L(L-1),                                            \tag{3.3}
\]

the exact number of proper oriented cyclic arcs.

## 4. The entire internally reachable upper band

Recall \(m=s+2d\).  From (2.4),

\[
                         \rho_1=m-d,
 \qquad                 \rho_2=m.                   \tag{4.1}
\]

Before the bank saturates, consecutive \(\rho_h\)'s differ by \(d\);
after saturation they differ by \(d-1\).  Each Type-I band has width
\(2d-2\).  The last one ends at

\[
                         \rho_{R-1}+2d-2=Q.          \tag{4.2}
\]

Hence the bands overlap and give every rank

\[
                         m,m+1,\ldots,Q.             \tag{4.3}
\]

No interval has rank above \(Q\), because every letter is contained in
\(\Sigma\).

### Theorem 4.1 (exact middle and q1 counts)

For every \(R\ge d+2\),

\[
                         N_m=L.                       \tag{4.4}
\]

For \(d\ge3\), one also has

\[
                         N_{m+1}=L.                  \tag{4.5}
\]

These \(L\) rank-\((m+1)\) targets are pairwise distinct and are exactly
the unions of consecutive owners.  When \(d=2\) and \(R\ge5\), the same
count gives \(N_{m+1}=L=2R\).  Only in the minimal exceptional case
\((d,R)=(2,4)\) does the saturated \(h=3\) band contribute another \(R\)
longer intervals, giving \(N_{m+1}=3R>L\).  The immediate-owner edge row
itself still has exactly \(L\) occurrences in every case.

#### Proof

At rank \(m\), the \(h=1\) band uses
\(\alpha+\beta=d\), which has \(d-1\) solutions, and the \(h=2\) band
uses \(\alpha=\beta=0\), which has one.  Thus

\[
                         N_m=R((d-1)+1)=Rd=L.
\]

At rank \(m+1\), the \(h=1\) band has \(d-2\) solutions and the \(h=2\)
band has two, so again

\[
                         N_{m+1}=R((d-2)+2)=L.
\]

For \(d\ge3\), every later band starts above \(m+1\).  A rank-\((m+1)\)
arc has source length \(D+1\), so it is the union of one consecutive owner
edge.  In the one-high case its proper cyclic \(B\)-block recovers \(j\),
and its two boundary \(Z\)-pieces recover \((\alpha,\beta)\).  In the
two-high case either its proper \(B\)-block recovers \(j\), or, when
\(R=d+2\), its complete internal \(Z_j\)-block and unique side label do.
Thus all \(L\) edge colours are distinct.

For \(d=2\), one has \(\rho_3=m+1\) exactly when \(R=4\); then its
coefficient at zero is one, adding \(R\) longer occurrences.  If
\(d=2\) and \(R\ge5\), then \(\rho_3=m+2\), so there is no additional
rank-\((m+1)\) occurrence. \(\square\)

### Theorem 4.2 (upper occurrence surplus)

For

\[
                         m\le q<Q,
\]

one has

\[
                         N_q\ge L.                   \tag{4.6}
\]

At rank \(Q\), at least \(R\) proper arcs have full support.

#### Proof

The coefficient sequence \(c_t\) is the triangle

\[
                         1,2,\ldots,d,\ldots,2,1.
\]

When consecutive Type-I bands are shifted by \(d\), the two overlapping
coefficients sum to exactly \(d\).  When the shift drops to \(d-1\), their
sum is at least \(d\).  The initial \(h=1\) band supplies the missing half
of the first \(h=2\) band, as in Theorem 4.1.  At the top, if
\(q=Q-y\) with \(1\le y\le d-1\), the last Type-I band contributes
\(y+1\), while the all-high complementary-gap family contributes
\(d-y\).  Thus the normalized coefficient is at least \(d\) at every rank
below \(Q\), proving \(N_q\ge Rd\).

For \(q=Q\), take \(h=R-1\) and
\(\alpha=\beta=d-1\).  The interval contains every low label and its high
banks already cover \(B\), so it has union \(\Sigma\).  There is one such
arc for each omitted high, giving \(R\) arcs. \(\square\)

## 5. Symmetric target loads

Average the template over all coordinate permutations.  Every fixed
rank-\(q\) interval occurrence is then uniformly distributed over
\(\binom{[n]}q\).  Let

\[
                         W={n\choose m}.
\]

Give the symmetric carousel orbit total mass \(W/L\), so that its middle
owner load is one.  Its rank-\(q\) occurrence load at each named target is

\[
 \boxed{
                         \lambda_q
   ={W\over L}\,{N_q\over {n\choose q}}.}            \tag{5.1}
\]

Because \(n=2m+1\),

\[
                         {n\choose m+1}=W.
\]

For \(d\ge3\), Theorems 4.1--4.2 therefore give

\[
                         \lambda_m=\lambda_{m+1}=1,  \tag{5.2}
\]

and

\[
                         \lambda_q>1
 \qquad(m+2\le q<Q).                                 \tag{5.3}
\]

At \(q=Q\),

\[
                         \lambda_Q
      \ge {W\over d{n\choose Q}}.                    \tag{5.4}
\]

Here

\[
                         Q-m=(R-2)d-1\ge d^2-1.
\]

At the triangular scale \(d^2=\Theta(m)\), the binomial ratio
\({n\choose Q}/W\) is exponentially small.  For example, with
\(t=Q-m\),

\[
 { {n\choose m+t}\over {n\choose m}}
 =\prod_{i=1}^t{m+2-i\over m+i}
 \le \exp\!\left(-{t(t-1)\over m+t}\right).          \tag{5.5}
\]

Thus \(\lambda_Q>1\) for all sufficiently large triangular parameters.

### Corollary 5.1 (exact boundary of symmetric upper completeness)

The symmetric average of individual carousels covers every named target of
every rank

\[
                         m\le q\le Q
\]

with load at least one for all sufficiently large parameters.  It has zero
load at every rank \(q>Q\).  Consequently it is upper-complete through rank
\(n\) if and only if

\[
                         Rd=n-s+1.                   \tag{5.6}
\]

This is an exact support obstruction, not a concentration issue: averaging
more coordinate relabellings cannot create a target larger than the support
of one template.

## 6. The maximal-aperture remainder and seam representation

Choose the largest admissible number of banks,

\[
                         R_*=\left\lfloor{n-s+1\over d}\right\rfloor,
\]

and put

\[
 c=n-Q=n-s+1-R_*d,
 \qquad                 0\le c<d.                   \tag{6.1}
\]

Then the only internally absent upper targets have ranks

\[
                         n-c+1,\ldots,n,             \tag{6.2}
\]

or equivalently complements of sizes \(0,1,\ldots,c-1\).

### Theorem 6.1 (two-support top-cap representation)

Let \(X\subset[n]\) with \(|X|=t<c\).  If \(n+t\ge2c\), there are
\(c\)-sets \(C_0,C_1\) such that

\[
                         C_0\cap C_1=X.              \tag{6.3}
\]

Consequently the two admissible carousel supports

\[
                         \Sigma_i=[n]-C_i
\]

satisfy

\[
                         \Sigma_0\cup\Sigma_1=[n]-X. \tag{6.4}
\]

Thus every internally missing top target is the OR of two complete
carousel supports and can, at the support level, be delivered by an
interval spanning one seam between two suitably chosen full components.

#### Proof

Choose disjoint sets \(A_0,A_1\subset[n]-X\), each of size \(c-t\), and
put \(C_i=X\cup A_i\).  The disjoint choices exist exactly under the
displayed inequality.  Taking complements gives (6.4).  Every \(Q\)-set
can be partitioned into the required \(P,B,Z\) banks, so both supports are
literal carousel supports. \(\square\)

At the triangular scale, \(c<d=O(\sqrt n)\), so the number of absent top
targets is

\[
                         \sum_{t=0}^{c-1}{n\choose t}
                         =\exp(o(n)),                \tag{6.5}
\]

whereas \(W/L=\exp(\Theta(n))\) owner components are available.  Hence
there is no scalar shortage of possible top-cap seams.  Equation (6.4) is
only a support representation: it does not prove owner-disjoint selection
or a legal literal splice.

## 7. Exact immediate-upper fusion current

For \(d\ge3\), the equality \(\lambda_{m+1}=1\) has a sharp consequence.
There is no
immediate-upper slack in the symmetric factor.

Let an integral collection of carousel owner cycles use every rank-\(m\)
owner once and every rank-\((m+1)\) edge colour once.  For a Johnson edge
\(e=XY\), write

\[
                         U(e)=X\cup Y.
\]

Suppose a fusion deletes an edge set \(E_-\) and inserts an edge set
\(E_+\).  Define its immediate-upper current by

\[
 \boxed{
                         \partial_U
   =\sum_{e\in E_+}[U(e)]-\sum_{e\in E_-}[U(e)].}     \tag{7.1}
\]

### Theorem 7.1 (zero-current edge-row fusion criterion)

The fusion preserves the exact immediate-upper **edge row** if and only if

\[
                         \partial_U=0                \tag{7.2}
\]

pointwise on \(\binom{[n]}{m+1}\).  In particular, a two-edge splice

\[
 (A,A'),(B,B')
 \longmapsto
 (A,B'),(B,A')                                       \tag{7.3}
\]

is admissible only if the cross pairs are Johnson edges and

\[
 \{A\cup A',B\cup B'\}
   =\{A\cup B',B\cup A'\}                            \tag{7.4}
\]

as multisets, unless it is embedded in a larger family whose total current
cancels pointwise.

#### Proof

Every deleted edge removes one occurrence of its named upper colour and
every inserted edge adds one.  The signed change at each colour is exactly
its coefficient in (7.1), so exact preservation is equivalent to (7.2).
Equation (7.4) is the specialization to (7.3). \(\square\)

The same fusion must also be literal-state compatible and must control
the arbitrary-width intervals meeting its cuts.  Those deeper ranks have
strict symmetric surplus internally, while rank \(m+1\) has none.  Thus
(7.2) is the first exact upper gate for a fusion which does not export a
separate seam q1 bank.

There is one important proof-safe qualification.  A fused word may create
new rank-\((m+1)\) intervals of width larger than one owner edge.  Let
\(\sigma_U(T)\) be the number of such newly certified seam intervals with
target \(T\).  Because the unfused carousel bank has exactly one q1
occurrence per target, the exact setwise condition is

\[
 \boxed{
                         \partial_U(T)+\sigma_U(T)\ge0
       \quad\text{for every }T\in{[n]\choose m+1}.}   \tag{7.5}
\]

Thus zero current is sufficient, and is necessary when
\(\sigma_U=0\).  A nonzero-current fusion is not ruled out, but every unit
of its negative current must be paid by a named literal seam interval.  It
is not enough to cite the deeper-rank symmetric surplus, because that
surplus lives at different target ranks.

## 8. Proof-safe conclusion

The moving-bank carousel has a stronger upper profile than was previously
known:

* every internal rank from \(m\) through \(Q\) occurs;
* for \(d\ge3\), symmetric owner and immediate-upper loads are exactly one;
* every other internally reachable upper rank has symmetric surplus;
* maximal aperture leaves fewer than \(d\) top ranks, and every missing
  target is the union of two legal supports.

It still does not prove an all-dimensional word.  The remaining upper-side
theorem is now exact:

> Select an owner-once, q1-once integral bank of carousels and fuse its
> cycles with either total current (7.1) zero or a literal q1 seam bank
> satisfying (7.5), while using seam intervals to realize the
> codimension-\(<c\) top cap and preserving the literal depth-\(d\)
> state.

This is a correlated coloured-cycle-fusion theorem.  Uniform averaging
solves every marginal below the top remainder but cannot, by itself, solve
that integral fusion.

## 9. Capacity-balanced aperture: bottom packing and top seams coexist

Maximal aperture is unnecessary.  Let

\[
                         v=n-s+1
\]

and fix a constant

\[
 0<\delta<1-\frac\pi4.
\tag{9.1}
\]

Choose

\[
 R=\left\lfloor{(1-\delta)v\over d}\right\rfloor,
 \qquad L=Rd,
 \qquad c=v-L=n-Q.
\tag{9.2}
\]

Then

\[
 {L\over v}\longrightarrow1-\delta,
 \qquad {c\over v}\longrightarrow\delta.
\tag{9.3}
\]

The aperture condition holds, and \(R/d\to(1-\delta)4/\pi>1\), so
\(R\ge d+3\) and the carousel is bi-resident for all sufficiently large
parameters.

### Theorem 9.1 (simultaneous scalar feasibility)

The integral base-star packing of the moving-bank theorem supplies at
least

\[
                  \bigl(\delta e^{-\pi}-o(1)\bigr)W
\tag{9.4}
\]

carousel endpoints.

Consequently, whenever

\[
                         \boxed{\delta e^{-\pi}>\theta,}
\tag{9.5}
\]

it contains the full \((\theta+o(1))W\) reset bank.  At the same time the
number of upper targets beyond the internal support is exponentially
smaller than the number of available carousel components:

\[
 \sum_{t=0}^{c-1}{n\choose t}
   =2^{(H_2(\delta/2)+o(1))n},
 \qquad
 {\theta W\over L}=2^{(1-o(1))n},                       
\tag{9.6}
\]

where \(H_2\) is binary entropy and \(H_2(\delta/2)<1\).  Every target
counted on the left is the union of two legal \(Q\)-supports.

#### Proof

Theorem 6.1 of the moving-bank construction gives

\[
 {U\over {n\choose s}}
 \ge {Ls(v-L+1)\over v(Ls+v-L+1)}.
\tag{9.7}
\]

Here \(Ls/v\to\infty\), while \((v-L+1)/v\to\delta\).
Also \({n\choose s}/W\to e^{-\pi}\).  This proves (9.4)--(9.5).

Since \(v/n\to1/2\), equation (9.3) gives \(c/n\to\delta/2<1/2\).
The standard binomial entropy estimate proves the first part of (9.6).
The central binomial estimate gives \(W=2^{(1-o(1))n}\), and division by
the polynomial \(L=\Theta(n)\) preserves that exponent.  Finally Theorem
6.1 applies to every complement \(X\) with \(|X|<c\), because
\(n+|X|\ge2c\) for all sufficiently large parameters. \(\square\)

A convenient numerical choice is any

\[
                         \delta>\theta e^{\pi};
\tag{9.8}
\]

this is about \(3.3\times10^{-4}\), far below
\(1-\pi/4\).  Thus the same aperture choice has both a positive bottom
packing margin and exponentially excessive top-seam count.

Theorem 9.1 is only a scalar compatibility theorem.  It does not choose
owner-disjoint carousels, assign the seam representations injectively, or
prove the literal q1-current condition (7.5).  Its point is that the
bottom-capacity and top-support requirements do not force contradictory
choices of \(R\).
