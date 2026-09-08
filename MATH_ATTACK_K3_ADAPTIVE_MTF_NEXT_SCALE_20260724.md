# Third-wave K: adaptive-MTF rounding at the next scale

## Executive verdict

Put

\[
W=\binom{2m}{m},
\qquad
N_q=\binom{2m}{m-q}=\binom{2m}{m+q},
\qquad
r_q=\frac{N_q}{W}.
\]

Write \(\mathrm{AD}(H)\) for the adaptive-MTF forest conclusion: one
oriented spanning Johnson linear forest, with \(e\) certified edges whose
lower colours are mutually distinct and whose upper colours are separately
mutually distinct, such that

\[
N_1-e=o(W)
\]

and, for one common compatible choice of boundary data,

\[
H(c+\rho_H)+
\sum_{q=2}^H(\widetilde M_q^-+\widetilde M_q^+)=o(W).
\]

Here \(c\) is the forest component count, \(\rho_H\) is the number of
internal positive coordinate runs of length at most \(H\), and
\(\widetilde M_q^\pm\) are the missing canonical signed depth-\(q\) supports
for that common boundary choice.  Write
\(\mathrm{AD}_A=\mathrm{AD}(\lceil A\sqrt m\rceil)\).

The audited theorem

\[
H=o\!\left(\sqrt{\frac{\log m}{\log\log m}}\right)
\]

is not unconditionally extended here.  The third-wave attack instead proves
the requested rigorous ceilings and replaces the huge decorated matching by
an exact correlated/pathwise max-flow formulation.

The main conclusions are as follows.

1.  The old strip codegree bound loses a factor \(\ell\).  The correct bound
    is

    \[
    \frac{\Gamma}{D}\le\frac{2}{m-H},
    \]

    and this is asymptotically sharp.  This improves the dependency
    calculation but does not improve the scale delivered by the displayed
    ABKV residual estimate.

2.  That quantitative ABKV certificate is intrinsically limited to

    \[
    H=o\!\left(\sqrt{\frac{\log m}{\log\log m}}\right).
    \]

    This is a proof-method ceiling, not a matching impossibility.

3.  A full equal-row strip matching has two genuine counting floors.

    - Requiring total band leave \(o(W/H)\) forces \(H=o(m^{1/4})\).
    - In the literal matched-cycles-plus-singleton-leftovers construction,
      the component term alone forces \(H=o(m^{1/3})\).

    The second is the true ceiling for that literal architecture.  Boundary
    flags of singleton components can improve deep support, so the stronger
    \(m^{1/4}\) statement must not be misreported as an architecture-wide AD
    obstruction.

4.  Below the true ceiling, the correct next strip theorem is smallest-rank
    saturation, not tiny total leave.  A full-strip matching with

    \[
    N_H-2\ell p=o(W/H),
    \qquad H=o(m^{1/3}),
    \qquad \ell/H\to\infty,
    \]

    would prove the adaptive-MTF conclusion.  It has an exact fractional
    solution.

5.  For complementary geodesic atoms, slot decoration can be eliminated
    exactly.  After choosing the middle paths and enforcing depth-one
    rainbowness, every deeper signed rank is an ordinary capacitated Hall
    problem.  Its Hall deficiency is exactly an all-subfamily cyclomatic
    excess.  A sufficient Gaussian path-dispersion target is

    \[
    HL+\sum_{q=2}^H(\delta_q^-+\delta_q^+)=o(W),
    \]

    where \(L\) is the middle leave and the \(\delta_q^\pm\) are explicit
    Hall/cycle-rank deficiencies.

6.  Rounding confined to a fixed exact complementary-path factor is rigid.
    For \(H=o(\sqrt m)\), all choices of orientations, terminal dummies,
    initial queues, and their correlations can change the aggregate deep
    defect by only \(o(W)\).  A macroscopic first-shadow defect requires
    positive-density path rebundling.  A single global coordinate permutation
    merely relabels the same defects.

7.  In the internal certified-slot model, at residual density \(1/H\),
    independent product reservoirs die whenever
    \(H\log H\gg\log m\), in particular at Gaussian depth.  Moreover,
    regularity, partiteness, fractional saturation, and numerical
    degree/codegree data alone cannot imply rounding: a
    truncated-projective-plane family matches those numerical scales but has
    integral matching number one.

Thus the next live construction is neither a better independent nibble nor a
within-factor pathwise randomization.  It is a genuinely correlated choice of
almost all complementary paths satisfying the cyclomatic Hall inequalities
at every signed depth.

No web search, finite search, or computational experiment is used below.

---

## 1. Gaussian expansions used throughout

The exact ratio is

\[
r_q
=\prod_{j=0}^{q-1}\frac{m-j}{m+j+1}.
\tag{1.1}
\]

Uniformly for \(1\le q\le H=o(\sqrt m)\), Taylor expansion of the logarithm
gives

\[
\log r_q
=-\frac{q^2}{m}
+O\!\left(\frac{q^2}{m^2}+\frac{q^4}{m^3}\right),
\tag{1.2}
\]

and hence

\[
\boxed{
r_q
=1-\frac{q^2}{m}
+O\!\left(\frac{q^4+q^2}{m^2}\right).
}
\tag{1.3}
\]

In particular,

\[
W-N_H
=\left(\frac{H^2}{m}
+O\!\left(\frac{H^4+H^2}{m^2}\right)\right)W.
\tag{1.4}
\]

These estimates are uniform on every range used below.

For completeness, the elementary bound

\[
r_q
\le\exp\!\left(-\frac{q^2}{m+q}\right)
\tag{1.5}
\]

follows termwise from (1.1).  Consequently any asymptotic requirement
\(H(1-r_H)=o(1)\) already forces \(H=o(\sqrt m)\).  Thus the expansion range
used in the strip ceilings below loses no potentially successful sequence.

---

## 2. Exact floors and ceilings for full equal-row strips

Let a full cyclic strip contain

\[
s=2\ell
\]

labels in every middle or signed shadow row.  Suppose a matching contains
\(p\) strips.  Since the depth-\(H\) rows are the smallest,

\[
sp\le N_H.
\tag{2.1}
\]

Put

\[
d=N_H-sp\ge0.
\tag{2.2}
\]

The uncovered class sizes are exactly

\[
u_0=W-sp=(W-N_H)+d,
\tag{2.3}
\]

and

\[
u_q^-=u_q^+=N_q-sp=(N_q-N_H)+d.
\tag{2.4}
\]

### 2.1 Total-band-leave floor

The total leave in the full strip hypergraph is

\[
U=u_0+\sum_{q=1}^H(u_q^-+u_q^+)
=U_{\mathrm{floor}}+(2H+1)d,
\tag{2.5}
\]

where

\[
U_{\mathrm{floor}}
=(W-N_H)+2\sum_{q=1}^H(N_q-N_H).
\tag{2.6}
\]

Using (1.3) and

\[
\sum_{q=1}^H(H^2-q^2)
=\frac{4H^3-3H^2-H}{6},
\]

one obtains

\[
\boxed{
U_{\mathrm{floor}}
=\left(
\frac{4H^3-H}{3m}
+O\!\left(\frac{H^5}{m^2}\right)
\right)W.
}
\tag{2.7}
\]

Thus, if \(H\to\infty\) and \(H=o(\sqrt m)\),

\[
U_{\mathrm{floor}}
=\left(\frac43+o(1)\right)\frac{WH^3}{m}.
\tag{2.8}
\]

Here \(U_{\mathrm{floor}}\) is the fractional/deepest-saturation floor.
Divisibility may force \(d\ge N_H\bmod s\), so the minimum integral leave
can be larger.

Consequently the strong requirement

\[
U=o(W/H)
\tag{2.9}
\]

forces

\[
\boxed{H=o(m^{1/4}).}
\tag{2.10}
\]

At \(H\sim c m^{1/4}\), the normalized floor satisfies

\[
\frac{U}{W/H}\ge\frac43c^4+o(1).
\tag{2.11}
\]

This is a genuine counting ceiling for the criterion that insists on tiny
total band leave.  It is not yet a lower bound on the actual AD deep defect:
unmatched middle masks, when made into singleton MTF components, can expose
additional deep labels.

### 2.2 The literal component ceiling

In the audited strip construction, every uncovered middle mask becomes a
separate component.  Therefore

\[
c=p+u_0\ge u_0\ge W-N_H.
\tag{2.12}
\]

Equations (1.4) and (2.12) imply

\[
\boxed{
Hc
\ge
\left(1+o(1)\right)\frac{WH^3}{m}.
}
\tag{2.13}
\]

Hence the literal architecture consisting of disjoint full strip cycles,
one cut per selected cycle, and singleton middle leftovers necessarily has

\[
\boxed{H=o(m^{1/3})}
\tag{2.14}
\]

if it is to satisfy AD.  This conclusion is independent of the quality of
the matching algorithm.

The scope is important.  It does not exclude connecting the leftover middles
by a new geometry, allowing deep overlap, using unequal certified quotas, or
abandoning strips altogether.

### 2.3 Correct correlated strip target

The right leave variable is the deepest-rank defect \(d\) in (2.2), not
the total leave \(U\).

The degree of a fixed target in either signed depth-\(q\) part is

\[
D_q=\frac{(m+q)!(m-q)!}{2(m-\ell)!^2}.
\]

Weight every full strip by \(1/D_H\), where \(D_H\) is its degree at either
signed depth-\(H\) vertex.  Then both depth-\(H\) parts have fractional load
one, while every shallower part has load

\[
\frac{D_q}{D_H}=\frac{N_H}{N_q}\le1.
\tag{2.15}
\]

The total fractional mass is exactly

\[
\frac{N_H}{2\ell}.
\tag{2.16}
\]

Thus deepest-rank saturation has an exact fractional solution and no marginal
obstruction.  Integral divisibility can still force
\(d\ge N_H\bmod 2\ell\), but this residue is less than \(2\ell\) and hence is
\(o(W/H)\) throughout the stated asymptotic strip range.

Suppose an integral full-strip matching satisfies

\[
d=N_H-2\ell p=o(W/H).
\tag{2.17}
\]

Cut the selected cycles using virtual cyclic closure and add uncovered middle
masks as singletons.  The selected rows give the valid upper bound

\[
\begin{aligned}
&H(c+\rho_H)
+\sum_{q=2}^H(\widetilde M_q^-+\widetilde M_q^+)\\
&\quad\le
\frac{HN_H}{2\ell}
+H(W-N_H)
+2\sum_{q=2}^H(N_q-N_H)
+\left(3H-2-\frac{H}{2\ell}\right)d.
\end{aligned}
\tag{2.18}
\]

The intrinsic baseline on the second line is

\[
\boxed{
\begin{aligned}
H(W-N_H)&+2\sum_{q=2}^H(N_q-N_H)\\
&=\left(
\frac{7H^3}{3m}
-\frac{3H^2}{m}
-\frac{H}{3m}
+\frac2m
+O\!\left(\frac{H^5}{m^2}\right)
\right)W.
\end{aligned}
}
\tag{2.19}
\]

Also, because \(e=p(2\ell-1)\),

\[
N_1-e=(N_1-N_H)+d+p.
\tag{2.20}
\]

It follows rigorously that

\[
\boxed{
H=o(m^{1/3}),\qquad
\ell/H\to\infty,\qquad
H<\ell<m,\qquad
d=o(W/H)
\quad\Longrightarrow\quad
\mathrm{AD}(H).
}
\tag{2.21}
\]

This is the strongest live theorem for the equal-row strip architecture:

> **Smallest-rank strip matching lemma — unproved.**  Find a full-strip
> matching saturating each signed depth-\(H\) class up to \(o(W/H)\), with
> \(H=o(m^{1/3})\) and \(H\ll\ell=o(m)\).

It would give a polynomial extension of the audited theorem, all the way to
the true component ceiling.  No such integral rounding is proved here.

---

## 3. The sharp strip codegree

The previous orbit estimate

\[
\Gamma/D\le 2\ell/(m-H)
\]

is not sharp.

Write \(D=D_H=D_{-H}\) for the maximum strip degree.

### Theorem 3.1 (sharp codegree scale)

Assume

\[
\ell-H\ge2,
\qquad
m-\ell\ge1,
\qquad
H<m/4.
\tag{3.1}
\]

For the full strip hypergraph,

\[
\boxed{
\frac{\Gamma}{D}\le\frac{2}{m-H}.
}
\tag{3.2}
\]

Moreover,

\[
\boxed{
\Gamma\ge\frac{2D_0}{m}
=\left(2+o(1)\right)\frac Dm
}
\tag{3.3}
\]

whenever \(H=o(\sqrt m)\).  Thus the normalized codegree is
\(\Theta(1/m)\).

### Proof

Fix a row-\(d\) mask \(X\), a row-\(e\) mask \(Y\), and the stabilizer orbit
\(\mathcal O\) of \(Y\) relative to \(X\).  The orbit is determined by the
rank of \(Y\) and \(|X\cap Y|\).  If

\[
a=|X\setminus Y|,
\qquad
b=|Y\setminus X|,
\]

then

\[
|\mathcal O|
=\binom{m+d}{a}\binom{m-d}{b}.
\tag{3.4}
\]

Inside a strip through \(X\), let \(n_{\mathcal O}\) be the number of
row-\(e\) cyclic intervals belonging to this orbit.  Strip geometry depends
only on \(d,e\) and relative cyclic displacement, so double counting gives

\[
\frac{\deg(X,Y)}{D_d}
=\frac{n_{\mathcal O}}{|\mathcal O|}.
\tag{3.5}
\]

For two cyclic intervals, a fixed intersection size occurs at no more than
two starts, except on the following plateaux.

1.  If one interval is contained in the other by \(j\) coordinates, there
    are \(j+1\) starts and the nontrivial orbit factor is
    \(\binom{m\mp d}{j}\).  For \(j\ge1\),

    \[
    \frac{j+1}{\binom{m\mp d}{j}}
    \le\frac{2}{m-H}.
    \tag{3.6}
    \]

    Here \(j\le2H<m-H-1\) in the stated range, so the displayed binomial
    bound applies.  The case \(j=0\) is \(Y=X\) and is excluded from pair
    codegrees.

2.  On the disjoint or full-union plateau there are at most \(2H+1\)
    starts.  Both nontrivial binomial orbit factors are at least \(m-H\), so

    \[
    \frac{n_{\mathcal O}}{|\mathcal O|}
    \le\frac{2H+1}{(m-H)^2}
    \le\frac2{m-H}.
    \tag{3.7}
    \]

Every generic nontrivial orbit has size at least \(m-H\) and multiplicity at
most two.  The only remaining orbit-one candidate is \(Y=X^c\); it cannot
co-occur with \(X\), since every strip member contains the same nonempty core.
Equations (3.5)--(3.7), together with \(D_d\le D\), prove (3.2).

For the lower bound, fix a middle mask \(X\).  Every strip through \(X\)
contains exactly two immediate rank-\((m+1)\) supersets of \(X\).  Its
stabilizer is transitive on the \(m\) such supersets.  Hence each has
codegree \(2D_0/m\), proving (3.3).  \(\square\)

The improved upper bound permits the ABKV parameters

\[
C_*=\left\lceil\frac{2D}{m-H}\right\rceil,
\qquad
\eta=\frac{C_*\log(1+C_*)}{D},
\]

and hence

\[
\eta=O\!\left(\frac{\ell\log m}{m}\right),
\tag{3.8}
\]

instead of \(O(\ell^2\log m/m)\).  Its logarithm still has leading term
\(-\log m\) in the ABKV-admissible regime.  More explicitly,
\(\log\eta=-\log m+\log\ell+\log\log m+O(1)\) at the scale relevant here,
so the exponential-in-rank bottleneck remains.

---

## 4. Ceiling of the existing ABKV certificate

The strip hypergraph rank is

\[
R=2\ell(2H+1)\sim4\ell H.
\tag{4.1}
\]

The component term requires

\[
\ell/H\to\infty.
\tag{4.2}
\]

The lower codegree (3.3) implies that the residual parameter in the displayed
ABKV estimate satisfies

\[
\eta\ge m^{-1+o(1)}.
\tag{4.3}
\]

On the only potentially successful strip range \(H=o(\sqrt m)\), the estimate
used in the audited proof is

\[
U
=O\!\left(
R\eta^{1/(R-1)}|V|
\right),
\qquad
|V|=(2H+1+o(H))W.
\tag{4.4}
\]

For this displayed right-hand side to certify \(U=o(W/H)\), it is necessary
that

\[
RH^2\eta^{1/(R-1)}=o(1).
\tag{4.5}
\]

Equations (4.3)--(4.5) force

\[
\frac{\log m}{R}-\log(RH^2)\longrightarrow\infty.
\tag{4.6}
\]

Write \(\ell/H=\omega(m)\to\infty\).  Since
\(R\sim4\omega H^2\), (4.6) implies

\[
H^2\log H=o(\log m),
\tag{4.7}
\]

and therefore

\[
\boxed{
H=o\!\left(\sqrt{\frac{\log m}{\log\log m}}\right).
}
\tag{4.8}
\]

Thus the first-wave scale is optimal for that numerical residual
certificate, even after the sharp codegree correction.

For the new deepest-saturation target one can weaken the requested total
leave.  Since (2.5) gives

\[
d\le\frac{U}{2H+1},
\tag{4.9}
\]

the condition \(U=o(W)\) already implies \(d=o(W/H)\).  Applied to (4.4),
this asks only

\[
RH\eta^{1/(R-1)}=o(1),
\tag{4.10}
\]

or

\[
\frac{\log m}{R}-\log(RH)\longrightarrow\infty.
\tag{4.11}
\]

With \(R\sim4\omega H^2\) and \(\omega\to\infty\), this still forces
\(H^2\log H=o(\log m)\).  Thus using the correct deepest leave changes the
polynomial prefactor in the certificate but not its asymptotic depth ceiling.

This statement is deliberately scoped.  It says neither that ABKV forbids a
better matching nor that strips cannot be correlated more efficiently.  It
says that substituting the exact parameters into the displayed residual
bound cannot certify a larger scale.

The weaker ABKV applicability condition

\[
e^{2R}\Gamma\log D=o(D)
\tag{4.12}
\]

only gives \(R\lesssim\tfrac12\log m\), and, with (4.2),

\[
H=o(\sqrt{\log m}).
\tag{4.13}
\]

Applicability without a sufficiently small leave does not prove AD.

---

## 5. Exact pathwise Hall rounding for complementary geodesics

The Gaussian certified-slot hypergraph has rank \(\Theta_A(m^{3/2})\).
That large rank can be removed from the formulation.

Put

\[
K=m+1,
\qquad
t_q=K-q,
\qquad
s_q=\left\lfloor K\frac{N_q}{W}\right\rfloor,
\qquad
d_q=t_q-s_q.
\tag{5.1}
\]

Here a complementary geodesic is a Johnson path
\(T_0,T_1,\ldots,T_m=T_0^c\); each coordinate of \(T_0\) departs exactly
once and each coordinate of its complement enters exactly once.

Let \(\mathcal P\) be a middle-disjoint family of oriented complementary
geodesics.  Assume their actual depth-one lower colours are globally distinct
and their actual depth-one upper colours are separately globally distinct.
Write

\[
L=W-K|\mathcal P|.
\tag{5.2}
\]

At signed depth \(q\ge2\), each path has \(t_q\) genuine internal canonical
flags.  Let \(G_q^\sigma\) be the bipartite incidence graph between paths and
their signed internal \(q\)-flags.  Give every path demand \(s_q\) and every
flag capacity one.  Define the Hall deficiency

\[
\boxed{
\delta_q^\sigma
=\max_{\mathcal X\subseteq\mathcal P}
\left(s_q|\mathcal X|
-|N_{G_q^\sigma}(\mathcal X)|\right)_+.
}
\tag{5.3}
\]

### Theorem 5.1 (exact pathwise rounding)

The maximum number of pairwise distinct signed depth-\(q\) flags obtainable
subject to at most \(s_q\) choices per path is

\[
\boxed{
|\mathcal P|s_q-\delta_q^\sigma.
}
\tag{5.4}
\]

In particular, an exact \(s_q\)-per-path decoration exists if and only if
\(\delta_q^\sigma=0\).

### Proof

Replace each path by \(s_q\) left clones with the same flag neighbourhood.
A matching saturating all clones is precisely a valid decoration.  The
capacitated Hall theorem gives the zero-deficiency statement.  More
generally, the standard max-flow min-cut formula says that the number of
unsaturated clones in a maximum matching is the largest clone-set Hall
deficit.  Because all clones of one path have the same neighbourhood, a
maximizing clone set contains either all \(s_q\) clones of each represented
path or none.  Thus that clone-set maximum is exactly (5.3), proving (5.4).
\(\square\)

Different depths and signs are separate rank parts.  Their choices can be
made independently after the common path family has been fixed.

The support obtained from (5.4) gives

\[
\begin{aligned}
\widetilde M_q^\sigma
&\le N_q-|\mathcal P|s_q+\delta_q^\sigma\\
&<\frac W{m+1}+L+\delta_q^\sigma.
\end{aligned}
\tag{5.5}
\]

Use the paths as components and add the \(L\) uncovered middle masks as
singletons.  Then

\[
c\le\frac W{m+1}+L,
\qquad
\rho_H=0,
\qquad
N_1-e=\frac{mL}{m+1}.
\tag{5.6}
\]

Consequently, uniformly for \(H=O(\sqrt m)\),

\[
\boxed{
HL+
\sum_{q=2}^H(\delta_q^-+\delta_q^+)=o(W)
\quad\Longrightarrow\quad
\mathrm{AD}(H).
}
\tag{5.7}
\]

This is an exact max-flow relaxation of the high-precision atom-matching
theorem and a sufficient correlated/pathwise target for AD.  Requiring
\(\delta_q^\sigma=0\) at every signed rank recovers exact decorated-atom
matching; allowing their total to be \(o(W)\) is a strictly weaker
sufficient condition.  The formulation separates the hard choice of paths
from the ordinary flow problems that decorate them.

### 5.1 Cyclomatic form of Hall

For \(\mathcal X\subseteq\mathcal P\), form the multigraph
\(\Gamma_q^\sigma(\mathcal X)\) whose vertices are the distinct signed
\(q\)-flags and in which every source path joins consecutive flags along its
internal \(q\)-row.  Retain parallel edges.  Let

\[
g_q^\sigma(\mathcal X)
=\#\{\text{connected components of the image multigraph}\},
\tag{5.8}
\]

and let \(\beta_q^\sigma(\mathcal X)\) be its cyclomatic number.  Every
source row contributes \(t_q\) vertices and \(t_q-1\) edge occurrences, so

\[
\beta_q^\sigma(\mathcal X)
=(t_q-1)|\mathcal X|
-|V(\Gamma_q^\sigma(\mathcal X))|
+g_q^\sigma(\mathcal X).
\tag{5.9}
\]

Therefore the collision excess is exactly

\[
\begin{aligned}
t_q|\mathcal X|
-|N_{G_q^\sigma}(\mathcal X)|
&=\beta_q^\sigma(\mathcal X)
+|\mathcal X|-g_q^\sigma(\mathcal X).
\end{aligned}
\tag{5.10}
\]

Substitution into (5.3) gives

\[
\boxed{
\delta_q^\sigma
=\max_{\mathcal X\subseteq\mathcal P}
\left(
\beta_q^\sigma(\mathcal X)
-(d_q-1)|\mathcal X|
-g_q^\sigma(\mathcal X)
\right)_+.
}
\tag{5.11}
\]

In particular, a full decoration exists exactly when, for every path
subfamily,

\[
\boxed{
\beta_q^\sigma(\mathcal X)
\le(d_q-1)|\mathcal X|+g_q^\sigma(\mathcal X).
}
\tag{5.12}
\]

This is the promised component-dispersion criterion: the remaining obstruction
is not aggregate support alone, but excess projected cycle rank in every
subfamily.

At depth one,

\[
s_1=t_1=m,
\qquad
d_1=0.
\tag{5.13}
\]

Thus (5.12) forces

\[
\beta_1^\sigma(\mathcal X)=0,
\qquad
g_1^\sigma(\mathcal X)=|\mathcal X|.
\tag{5.14}
\]

Indeed \(\beta\ge0\) and a union of \(|\mathcal X|\) connected source rows
has \(g\le|\mathcal X|\).  Slot selection gives no flexibility at depth one:
the path rows must already be mutually disjoint.

At depth two, for \(m\ge5\),

\[
K\frac{N_2}{W}
=m-3+\frac6{m+2},
\]

so

\[
s_2=m-3,
\qquad
t_2=m-1,
\qquad
d_2=2.
\tag{5.15}
\]

The exact depth-two condition is therefore

\[
\boxed{
\beta_2^\sigma(\mathcal X)
\le|\mathcal X|+g_2^\sigma(\mathcal X)
\quad\text{for every }\mathcal X.
}
\tag{5.16}
\]

More generally, with \(\{x\}\) denoting fractional part,

\[
d_q
=K(1-r_q)-q+\{Kr_q\}
=q(q-1)+O\!\left(\frac{q^4}{m}+1\right)
\tag{5.17}
\]

uniformly for \(q=o(\sqrt m)\).

### 5.2 Multiplicity-two collision orientation

Suppose at one signed depth every flag occurs on at most two selected paths.
Form the collision multigraph on \(\mathcal P\), with one edge for each flag
shared by two paths.  Then (5.12) reduces exactly to

\[
|E(\mathcal X)|\le d_q|\mathcal X|
\quad\text{for every }\mathcal X\subseteq\mathcal P.
\tag{5.18}
\]

Equivalently, the collision multigraph admits an orientation of maximum
indegree at most \(d_q\).  Indeed, assign each collision edge to one of its
endpoints with endpoint capacity \(d_q\); capacitated Hall is exactly
(5.18).  Orient a collision toward a path which discards that shared flag;
fill any unused discard allowance by discarding arbitrary additional flags.
This is a concrete correlated rounding rule, but no construction of the
required low-pseudoarboricity collision graphs is presently known.

### Exact next missing theorem — unproved

A sufficient Gaussian path-dispersion problem is now:

> Find \(B-o(B/H)\), \(B=W/(m+1)\), middle-disjoint complementary geodesics
> whose two depth-one rows are disjoint and for which
> \[
> \sum_{q=2}^H(\delta_q^-+\delta_q^+)=o(W).
> \]

This statement is strictly more informative than asking for a generic
near-perfect matching in a \(\Theta(mH)\)-rank hypergraph.

---

## 6. Rigidity of rounding inside a fixed path factor

Let \(\mathcal F\) be one complementary-geodesic factor of the middle
layer.  It has

\[
B=\frac{W}{m+1}
\tag{6.1}
\]

unoriented paths and partitions the middle layer.  For the depth-one
statements in Section 6.1, we additionally assume that its actual upper edge
colours partition rank \(m+1\), as happens when \(\mathcal F\) is obtained by
cutting an exact odd wreath factor.  The boundary-cap theorem itself does not
use that extra hypothesis.

For one path \(P=(T_0,\ldots,T_m)\), define the boundary-independent internal
supports

\[
\mathcal I_q^-(P)
=\left\{
\bigcap_{j=0}^qT_{i+j}:0\le i\le m-q
\right\},
\tag{6.2}
\]

\[
\mathcal I_q^+(P)
=\left\{
\bigcup_{j=0}^qT_{i+j}:0\le i\le m-q
\right\}.
\tag{6.3}
\]

Let \(\mathcal I_q^\pm\) be their unions over all paths and put

\[
D_{q,\mathrm{int}}^\pm=N_q-|\mathcal I_q^\pm|.
\tag{6.4}
\]

### Theorem 6.1 (boundary-cap rigidity)

For every collection of path orientations and every jointly correlated legal
choice of terminal dummies and initial queues,

\[
\boxed{
0\le
D_{q,\mathrm{int}}^\pm-\widetilde M_q^\pm
\le qB.
}
\tag{6.5}
\]

Consequently, writing

\[
D_H^{\mathrm{int}}
=\sum_{q=2}^H
(D_{q,\mathrm{int}}^-+D_{q,\mathrm{int}}^+),
\tag{6.6}
\]

one has

\[
\boxed{
0\le
D_H^{\mathrm{int}}
-\sum_{q=2}^H(\widetilde M_q^-+\widetilde M_q^+)
\le B(H(H+1)-2).
}
\tag{6.7}
\]

### Proof

On a complementary geodesic, no departed coordinate returns and no inserted
coordinate later departs.  Hence the first \(K-q\) lower flags are exactly
the forward consecutive intersections (6.2); only the final \(q\) lower
flags can depend on terminal dummies.  Dually, the final \(K-q\) upper flags
are the backward consecutive unions (6.3); only the initial \(q\) can depend
on the initial queue.  There are \(qB\) boundary occurrences per sign.
Adding them can reduce missing support by at most \(qB\), proving (6.5).
Summing over two signs and \(q=2,\ldots,H\) proves (6.7).  \(\square\)

Reversing a path preserves its internal support sets, although the optimized
boundary gain need not be orientation-invariant.

For one common jointly compatible choice \(\xi\) of all path orientations
and boundary data, let
\(g_{\mathcal F}(\xi)\) be the total number, over signed depths
\(2,\ldots,H\), of distinct boundary labels added outside the corresponding
global internal supports.  Define

\[
G_{\partial,H}(\mathcal F)=\max_\xi g_{\mathcal F}(\xi).
\tag{6.8}
\]

Then identically

\[
\boxed{
\min_\xi
\sum_{q=2}^H(\widetilde M_q^-+\widetilde M_q^+)
=D_H^{\mathrm{int}}-G_{\partial,H}(\mathcal F),
}
\tag{6.9}
\]

with

\[
0\le G_{\partial,H}(\mathcal F)
\le\min\{D_H^{\mathrm{int}},B(H(H+1)-2)\}.
\tag{6.10}
\]

Such legal choices exist throughout the present ranges: for example, when
\(H\le m/2\), use the natural future inserted coordinates as terminal
dummies and the last \(H\) not-yet-entered coordinates as the initial queue.

If

\[
H=o(\sqrt m),
\tag{6.11}
\]

the right side of (6.10) is \(o(W)\).  Therefore

\[
\boxed{
D_H^{\mathrm{int}}=o(W)
\iff
\min_\xi\sum_{q=2}^H
(\widetilde M_q^-+\widetilde M_q^+)=o(W).
}
\tag{6.12}
\]

Thus every sub-Gaussian scale strictly above the audited polylogarithmic
window still requires a genuinely good internal path factor.  Orientations,
queues, dummies, and arbitrary negative dependence among their choices are
asymptotically incapable of repairing a bad one.

At Gaussian depth \(H=\lceil A\sqrt m\rceil\), the total boundary capacity is

\[
(A^2+o(1))W.
\tag{6.13}
\]

Internal and optimized canonical defects are no longer equivalent in
aggregate.  At any single depth, however, both signs together can add at
most

\[
2qB=O_A(W/\sqrt m)=o(W).
\tag{6.14}
\]

So a positive-density internal defect at one Gaussian rank is fatal to every
pathwise boundary choice.

### 6.1 Depth-one rigidity and transport

Actual edge intersections and unions are invariants of the unoriented path
blocks.  Under the upper-partition hypothesis imposed above, all upper
colours are distinct, so selecting one edge for each distinct lower colour
is optimal and gives

\[
e
=\left|
\{T_i\cap T_{i+1}:P\in\mathcal F,\ 0\le i<m\}
\right|.
\tag{6.15}
\]

Hence \(N_1-e\) is unchanged by orientations, queues, dummies, slot choices,
or any correlations among them.

For \(\sigma\in\{-,+\}\), define the physical first-shadow defects by

\[
M_1^-(\mathcal F)
=N_1-\left|\{T_i\cap T_{i+1}:P\in\mathcal F,\ 0\le i<m\}\right|,
\]

\[
M_1^+(\mathcal F)
=N_1-\left|\{T_i\cup T_{i+1}:P\in\mathcal F,\ 0\le i<m\}\right|.
\]

Under the upper-partition hypothesis, \(M_1^+(\mathcal F)=0\) and
\(N_1-e=M_1^-(\mathcal F)\).

Suppose two complementary-geodesic middle factors
\(\mathcal F,\mathcal F'\) share \(B-r\) unoriented path blocks.  Removing
the common supports shows, for either sign,

\[
\boxed{
|M_1^\sigma(\mathcal F)-M_1^\sigma(\mathcal F')|
\le mr,
}
\tag{6.16}
\]

and, for every \(q\ge2\),

\[
\boxed{
|D_{q,\mathrm{int}}^\sigma(\mathcal F)
-D_{q,\mathrm{int}}^\sigma(\mathcal F')|
\le(K-q)r.
}
\tag{6.17}
\]

These are per-sign internal-support bounds.  Independently optimized boundary
defects require the additional boundary-gain term from (6.10).

If, for one fixed sign \(\sigma\), one factor has
\(M_1^\sigma\ge\varepsilon W\) and another has \(M_1^\sigma=o(W)\), then
(6.16) forces

\[
\boxed{
r\ge
\frac{\varepsilon W-o(W)}m
=(\varepsilon+o(1))B.
}
\tag{6.18}
\]

Thus positive-density path rebundling is deterministically necessary already
at depth one.  This is conditional on a macroscopic starting defect; the
repository's frozen MSW premise supplies such a starting situation, but the
inequality itself makes no assertion that every exact factor is defective.

Applying one global coordinate permutation to the whole factor only relabels
all supports, Hall graphs, component counts, and cycle ranks.  It cannot
change their cardinalities.  Independent per-path permutations, on the other
hand, do not in general preserve or guarantee the common middle partition;
the exceptional choices that do preserve it already constitute a legal
rebundling.  A useful permutation scheme must therefore rebundle paths across
genuinely different factor states.

---

## 7. Independent residual reservoirs become pathless

The desired internal pathwise augmentation cannot be supported by an
independently thinned reservoir.

In the internal certified-slot model of Section 5, retain every target in
every signed depth independently with probability \(\varepsilon\).  Fix
\(A\) and suppose \(H\le A\sqrt m\).  Uniformly in \(q\le H\),

\[
s_q\ge c_A m
\tag{7.1}
\]

for a constant \(c_A>0\).  A fixed complementary geodesic has at most \(m+1\)
available flags at one signed depth.  A binomial tail bound gives

\[
\Pr(\text{at least \(s_q\) retained flags at one signed depth})
\le(C_A\varepsilon)^{c_A m}
\tag{7.2}
\]

for another constant \(C_A\).  The reservoirs in distinct signed rank parts
are independent, so

\[
\Pr(\text{one fixed path is feasible at every signed depth})
\le(C_A\varepsilon)^{c_A mH}.
\tag{7.3}
\]

There are at most

\[
W(m!)^2=\exp(O(m\log m))
\tag{7.4}
\]

directed complementary geodesics.  The union bound proves:

### Theorem 7.1 (product-reservoir extinction)

If \(C_A\varepsilon<1\) and

\[
H\log\frac1{C_A\varepsilon}\gg\log m,
\tag{7.5}
\]

then with probability tending to one the retained product reservoir contains
no internally feasible complementary pathwise atom of Section 5.

At the desired residual density \(\varepsilon\asymp1/H\), this applies when

\[
H\log H\gg\log m.
\tag{7.6}
\]

This is not an obstruction to a correlated absorber.  It proves that a
successful leftover must retain coherent path towers and excludes precisely
those permutation or coupon-style schemes whose induced signed-rank
reservoirs are independent targetwise thinnings.

---

## 8. Numerical matching data cannot force rounding

The actual decorated atom hypergraph has large rank and unavoidable
\(1/m\)-scale codegrees.  Under the decorated-description multihypergraph
convention, fix a middle mask \(T\) and an incident mandatory depth-one lower
flag \(S\subset T\).  Conditioned on an atom containing \(T\), the mask is
uniformly distributed among its \(K=m+1\) path positions.  It is incident
with one lower flag at an endpoint and two internally.  Averaging and then
dividing among the \(m\) lower neighbours gives

\[
\boxed{
\frac{\deg(T,S)}{\deg(T)}=\frac2{m+1}.
}
\tag{8.1}
\]

The same holds on the upper side.  At Gaussian depth,

\[
R_{\mathrm{atom}}
=K+2\sum_{q=1}^H s_q
\]

is the certified-slot atom rank, and

\[
\frac{R_{\mathrm{atom}}}{m^{3/2}}
\longrightarrow
2\int_0^A e^{-t^2}\,dt.
\tag{8.2}
\]

Indeed, uniformly for \(q\le A\sqrt m\), the exact product (1.1) gives
\(r_q=\exp(-q^2/m+O_A(m^{-1/2}))\); (8.2) is then the corresponding Riemann
sum, with the floors in \(s_q\) contributing only \(O(H)\).

Thus neither the ABKV exponential-rank condition nor a hypothetical condition
\(R_{\mathrm{atom}}\Gamma/D=o(1)\) is available.

More importantly, no theorem based only on the numerical triple
\((R,D,\Gamma)\), regularity, multipartiteness, and fractional saturation can
prove the needed rounding.

### Theorem 8.1 (projective-plane meta-obstruction)

Let \(Q\) be a prime power and fix a point \(x\) in the projective plane of
order \(Q\).  The \(Q+1\) lines through \(x\), with \(x\) deleted, partition
the other points into \(Q+1\) parts of size \(Q\).  Every line not through
\(x\) is a transversal of those parts.

Add \(h\) auxiliary \(Q\)-point parts.  For every base line \(\ell\) not
through \(x\) and every vector \(z\in[Q]^h\), form the edge

\[
\ell\cup\{(j,z_j):1\le j\le h\}.
\tag{8.3}
\]

The resulting hypergraph is simple and \(R\)-partite, with

\[
R=Q+1+h,
\qquad
D=Q^{h+1},
\qquad
\Gamma=Q^h=\frac DQ.
\tag{8.4}
\]

Uniform edge weight \(1/D\) is an exact fractional perfect matching of mass
\(Q\).  Nevertheless every two edges intersect in their base projective
lines, so

\[
\boxed{\nu=1.}
\tag{8.5}
\]

### Proof

A base point lies on \(Q\) allowed projective lines and each has \(Q^h\)
auxiliary extensions.  An auxiliary point lies in \(Q^2\) base lines and
\(Q^{h-1}\) extensions, giving degree \(Q^{h+1}\) in both cases.  Two
compatible vertices determine at most \(Q^h\) edges.  All vertex loads under
weight \(1/D\) equal one.  Finally, any two projective lines meet, and two
allowed lines cannot meet at \(x\).  Hence every two hyperedges intersect.
\(\square\)

Taking \(Q\) on the scale of \(m\) and \(h\) on the scale of \(m(H-1)\)
reproduces

\[
R\asymp mH,
\qquad
\Gamma/D\asymp1/m,
\]

with enormous degree and total integral failure.  This example does not
model the special geometry of complementary paths.  Its exact implication is
that those geometric and absorptive properties are indispensable; numerical
degree/codegree improvements alone cannot solve the problem.

---

## 9. Exhausted routes and the surviving theorem

### What is now proved

1. The full-row strip matching has exact total-leave floor (2.7).
2. Tiny total band leave has a true \(m^{1/4}\) counting ceiling.
3. Matched strips plus singleton middles have a true \(m^{1/3}\) component
   ceiling.
4. Deepest-rank saturation (2.17) would suffice throughout
   \(H=o(m^{1/3})\), and its fractional solution is exact.
5. The sharp strip codegree is \(\Theta(1/m)\), not \(O(\ell/m)\).
6. The existing quantitative ABKV residual certificate cannot exceed the
   already audited \(o(\sqrt{\log m/\log\log m})\) scale.
7. Certified-slot rounding is exactly the Hall/cyclomatic problem
   (5.3)--(5.12), with the exact depth-two criterion (5.16).
8. Within a fixed exact path factor, boundary/orientation choices are
   asymptotically inert for every \(H=o(\sqrt m)\).
9. Among exact complementary-path factors, repairing a macroscopic
   first-shadow defect requires positive-density path rebundling.
10. Internal certified-slot product reservoirs at density \(1/H\) are excluded when
    \(H\log H\gg\log m\), and no black-box theorem using only the numerical
    regularity/partiteness/fractional-saturation data can provide the missing
    absorber.

### What is not proved

No unconditional adaptive-MTF theorem is obtained at a depth larger than the
first-wave logarithmic scale.  In particular, this report does not prove the
smallest-rank strip matching lemma, the cyclomatic-dispersion theorem for an
almost-exact complementary path family, or \(\mathrm{AD}_A\).

The two clean live targets are now:

1. **Polynomial strip target.**  For some
   \(H\to\infty\), \(H=o(m^{1/3})\), and \(H\ll\ell=o(m)\), round the
   deepest-rank fractional strip matching to
   \[
   N_H-2\ell p=o(W/H).
   \]

2. **Gaussian path-dispersion target.**  Find
   \(B-o(B/H)\) complementary geodesics with disjoint middle and depth-one
   rows and
   \[
   \sum_{q=2}^H\sum_{\sigma\in\{-,+\}}
   \max_{\mathcal X}
   \left(
   \beta_q^\sigma(\mathcal X)
   -(d_q-1)|\mathcal X|
   -g_q^\sigma(\mathcal X)
   \right)_+
   =o(W).
   \]

The second is the exact max-flow relaxation and sufficient missing
correlated/pathwise target requested by this attack.  It has no known
counting ceiling at Gaussian depth.  It also makes clear why the next advance
must be global: depth one already forbids repair by slot selection,
fixed-factor boundaries contribute only a small cap below Gaussian scale,
and independently thinned residuals contain no coherent path towers in the
extinction regime of Theorem 7.1.

---

## 10. Audit record and caveats

The strip ceiling package, the Hall/cyclomatic theorem, and the fixed-factor
boundary theorem were independently cross-audited.

- The constants \(4/3\), \(7/3\), the \(m^{1/4}\) raw-leave ceiling, and the
  \(m^{1/3}\) component ceiling were rederived independently.
- The sharp codegree proof was checked orbit by orbit, including containment,
  disjoint/full-union plateaux, and the nonco-occurring complement orbit.
- The clone-Hall identity, the cycle-rank conversion, the values
  \(s_2=m-3,d_2=2\), and the expansion of \(d_q\) were independently
  verified.
- The boundary cap was checked per sign and per path; its aggregate value is
  exactly \(B(H(H+1)-2)\).
- The projective-plane degrees, codegrees, fractional mass, and matching
  number were independently recounted.

The following scope restrictions are essential.

- The \(m^{1/4}\) ceiling is for tiny total full-band leave, not for every AD
  implementation.
- The \(m^{1/3}\) ceiling assumes unmatched middles remain singleton
  components.
- Formula (2.18) is an upper certificate from selected strip rows; singleton
  boundary flags may improve it.
- The ABKV ceiling concerns the displayed quantitative guarantee, not the
  existence of better correlated matchings.
- The exact codegree (8.1) uses the decorated-description multihypergraph
  convention; aggregating parallel decorated edge sets requires a separate
  multiplicity audit.
- The projective-plane example blocks black-box numerical matching theorems,
  not arguments using complementary-geodesic geometry.
- Reservoir extinction concerns the internal certified-slot model, assumes
  independent targetwise retention in every signed rank, and, at density
  \(1/H\), is proved only when \(H\log H\gg\log m\).  A separately enlarged
  family of boundary decorations would require its own count.
- Internal supports are orientation-invariant; optimized boundary gain need
  not be.
- The transport inequalities are per sign and concern internal supports.
  An aggregate defect spread over \(H\) ranks need not force
  positive-density rebundling.
- One global coordinate permutation preserves all defects; independent
  per-path permutations do not in general preserve the common middle
  partition, and preserving choices already constitute a rebundling.

Within these scopes, every statement labelled as proved and every displayed
identity or constant above is unconditional; the two existence targets are
explicitly labelled unproved.
