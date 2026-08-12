# Global affine master cycles for critical promotion rings: exact loads and a deterministic run obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, random sampling, solver,
or external theorem is used.

## 0. Outcome

Put

\[
 n=2m,\qquad H=\left\lfloor\sqrt{m\log m}\right\rfloor,
 \qquad M=m+H,\qquad W=\binom{2m}{m},
 \tag{0.1}
\]

and identify the coordinate set with the cyclic group \(\mathbb Z_n\).
For every unit \(a\in\mathbb Z_n^*\), let

\[
 \Gamma_a=(0,a,2a,\ldots,(n-1)a)
 \tag{0.2}
\]

be the corresponding directed Cayley cycle.  A root is a set

\[
 A\in\binom{\mathbb Z_n}{m-H},\qquad U_A=\mathbb Z_n\setminus A.
 \tag{0.3}
\]

The **global affine-restriction family** permits an arbitrary, globally
coupled slope assignment

\[
 \alpha:\binom{\mathbb Z_n}{m-H}\longrightarrow\mathbb Z_n^*.
 \tag{0.4}
\]

The promotion frame at \(A\) is the cyclic order induced on \(U_A\) by
\(\Gamma_{\alpha(A)}\).  The value \(\alpha(A)\) may depend on the whole
root system; no independence, locality, product structure, or bounded
root block is assumed.

This note proves a deterministic no-go for the entire family.

1.  For a fixed master cycle \(\Gamma\), a target \(S\) and a root
    \(A\subset S\), put \(J=S\setminus A\).  Then \(J\) is a window of
    the frame \(\Gamma|_{A^c}\) if and only if \(J\) is contained in one
    cyclic \(S\)-run of \(\Gamma\).  This gives exact formulae for every
    middle, lower, and upper target load.

2.  If \(|S|=s\), the fraction of \(s\)-sets having a run of length at
    least \(k\) in at least one affine Cayley cycle is at most

    \[
      n\varphi(n)\frac{(s)_k}{(n)_k}
      \le n^2\left(\frac{s}{n}\right)^k.
      \tag{0.5}
    \]

    This bound is independent of the assignment \(\alpha\).

3.  At the middle layer, \(s=m\) and \(k=H\).  Hence the number
    \(C_0(\alpha)\) of middle owners hit by the full ring system satisfies

    \[
      \boxed{
      C_0(\alpha)\le
      W n^2 2^{-H}
      =W\exp\bigl(-(\log2+o(1))H\bigr)=o(W).}
      \tag{0.6}
    \]

    Nevertheless the exact middle incidence mass is

    \[
                         MN_H=(1+o(1))W,
      \qquad N_H=\binom{2m}{m-H}.
      \tag{0.7}
    \]

    Thus almost all incidence mass is forced into repetitions:

    \[
      \sum_X(\ell_0(X)-1)_+
        =MN_H-C_0(\alpha)=(1-o(1))W,
      \tag{0.8}
    \]

    while \((1-o(1))W\) middle owners are holes.  Deleting one phase or
    truncating rings cannot improve the support.

4.  Let \(q_0=\lceil m^{1/4}\rceil\).  At the entrance depth, both the
    lower and upper potential supports have relative size

    \[
       \exp\bigl(-(\log2+o(1))H\bigr).
       \tag{0.9}
    \]

    Therefore even after arbitrary globally coordinated phase cuts and
    nested tags, each sign has \((1-o(1))N_{q_0}=(1-o(1))W\) entrance
    holes.  More generally, for every fixed \(0<\rho<1\), the same
    exponential support failure holds simultaneously for both signs at
    every \(0\le q\le\rho H\).

The obstruction is not the previously proved polynomial block-product
hole floor.  Here the slope choices may correlate the entire
\(\binom mH\)-root star of every middle target and may be chosen by an
arbitrary global rule.  The failure is a support-entropy obstruction:
the affine group supplies only \(\varphi(n)\le n\) master cycles, and a
typical target has no \(H\)-run in any of them.

In fact, any restriction construction using a library of \(L\) master
cycles can cover a positive fraction of the middle layer only if

\[
                         \boxed{L\ge(1-o(1))\frac{2^H}{n}.}
 \tag{0.10}
\]

Thus cyclic, affine finite-field, and any other polynomial-orbit
master-frame construction are ruled out, even with unrestricted
root-dependent and globally coupled selection.  A surviving algebraic
construction must use at least \(\exp(\Omega(H))\) genuinely different
global orders, or must cease to be a restriction of global orders.

## 1. Promotion windows in restriction form

Let \(\Gamma\) be any directed cyclic order of \(\mathbb Z_n\).  If
\(U\subseteq\mathbb Z_n\), write \(\Gamma|_U\) for the cyclic order
obtained by deleting all labels outside \(U\).

For \(S\subsetneq\mathbb Z_n\), a **cyclic \(S\)-run in \(\Gamma\)** is
a maximal nonempty interval of consecutive labels of \(\Gamma\) all
belonging to \(S\).  The runs are understood cyclically, so the pieces
at a displayed cut are joined when appropriate.

### Lemma 1.1 (exact run criterion)

Let \(A\subset S\subsetneq\mathbb Z_n\), put

\[
                         J=S\setminus A,
 \tag{1.1}
\]

and assume \(J\ne\varnothing\).  Then \(J\) is a cyclic interval of
\(\Gamma|_{A^c}\) if and only if \(J\) is contained in one cyclic
\(S\)-run of \(\Gamma\).

#### Proof

We have

\[
                         A^c=(\mathbb Z_n\setminus S)\sqcup J.
 \tag{1.2}
\]

If \(J\) is contained in one \(S\)-run, all labels of that run outside
\(J\) lie in \(A\) and disappear upon restriction.  No label of
\(\mathbb Z_n\setminus S\) lies between the surviving labels of \(J\),
so they form one interval in \(\Gamma|_{A^c}\).

Conversely, distinct cyclic \(S\)-runs are separated in both directions
by labels of \(\mathbb Z_n\setminus S\).  Those labels all survive in
\(A^c\).  Hence a set \(J\) meeting two different runs cannot be one
cyclic interval of the restricted order. \(\square\)

This criterion is the exact place at which restriction of a global
order loses the root star.  Deleting the \(A\)-labels can close gaps
inside one \(S\)-run, but it cannot cross a label outside \(S\).

## 2. Exact middle and signed loads

Fix an arbitrary slope assignment \(\alpha\) as in (0.4).  For a cycle
\(\Gamma\), let \(\mathcal R_\Gamma(S)\) be the set of cyclic \(S\)-runs
in \(\Gamma\).

For a middle owner \(X\in\binom{\mathbb Z_n}m\), its exact full-ring
load is

\[
 \boxed{
 \ell_0^\alpha(X)=
 \sum_{J\in\binom XH}
 \mathbf1\!\left\{
   J\subseteq R\text{ for some }
   R\in\mathcal R_{\Gamma_{\alpha(X\setminus J)}}(X)
 \right\}.}
 \tag{2.1}
\]

Indeed the corresponding root is forced to be \(A=X\setminus J\), and
Lemma 1.1 is precisely the condition that \(J\) be one of its
\(H\)-windows.  A proper nonempty cyclic interval has a unique starting
phase, so (2.1) has no phase multiplicity.

For \(0\le q<H\) and a lower target
\(S\in\binom{\mathbb Z_n}{m-q}\), the exact untagged load is

\[
 \boxed{
 \ell_q^{-,\alpha}(S)=
 \sum_{J\in\binom S{H-q}}
 \mathbf1\!\left\{
   J\subseteq R\text{ for some }
   R\in\mathcal R_{\Gamma_{\alpha(S\setminus J)}}(S)
 \right\}.}
 \tag{2.2}
\]

For \(0\le q\le H\) and an upper target
\(T\in\binom{\mathbb Z_n}{m+q}\), it is

\[
 \boxed{
 \ell_q^{+,\alpha}(T)=
 \sum_{J\in\binom T{H+q}}
 \mathbf1\!\left\{
   J\subseteq R\text{ for some }
   R\in\mathcal R_{\Gamma_{\alpha(T\setminus J)}}(T)
 \right\}.}
 \tag{2.3}
\]

These are literal physical target identities, not marginal counts.
They also retain the common nested chronology: for a fixed root, the
sets in (2.2) and (2.3) are the shorter and longer intervals around the
same phase.

### Proposition 2.1 (exact aggregate loads)

For every slope assignment \(\alpha\),

\[
 \sum_{X\in\binom{\mathbb Z_n}m}\ell_0^\alpha(X)=MN_H,
 \tag{2.4}
\]

and, at every proper lower depth and every upper depth,

\[
 \sum_{|S|=m-q}\ell_q^{-,\alpha}(S)=MN_H,
 \qquad
 \sum_{|T|=m+q}\ell_q^{+,\alpha}(T)=MN_H.
 \tag{2.5}
\]

#### Proof

Every root frame has exactly \(M\) cyclic intervals of each fixed
length between \(1\) and \(M-1\).  Count root--phase incidences.  The
target of such an incidence is unique, and (2.1)--(2.3) count the same
incidences by target. \(\square\)

At the lower endpoint \(q=H\), the interval is empty.  The physical
tagged construction uses the unique root \(A=S\) and activates one
anchor phase; the untagged phase-incidence count has the harmless
\(M\)-fold degeneracy already audited in the promotion-ring notes.

Now permit arbitrary phase deletions and nested threshold tags.  If
\(y_{A,i,q}\in\{0,1\}\) records whether phase \(i\) of root \(A\) is
active at threshold \(q\), then the tagged versions of (2.2)--(2.3) are
obtained by multiplying each surviving summand by the \(y\)-value of
its unique physical phase.  In particular,

\[
 b_q^-(S)\le\ell_q^{-,\alpha}(S),\qquad
 b_q^+(T)\le\ell_q^{+,\alpha}(T).
 \tag{2.6}
\]

Thus tags can balance loads only inside the potential supports of
(2.2)--(2.3); they cannot create a missing target.

## 3. The master-cycle support bound

For a cyclic order \(\Gamma\), let

\[
 \mathcal B_{s,k}(\Gamma)
 =\left\{S\in\binom{\mathbb Z_n}s:
          S\text{ has a cyclic run of length at least }k
   \text{ in }\Gamma\right\}.
 \tag{3.1}
\]

### Lemma 3.1 (one-cycle run bound)

For \(1\le k\le s<n\),

\[
 |\mathcal B_{s,k}(\Gamma)|
 \le n\binom{n-k}{s-k},
 \tag{3.2}
\]

and hence

\[
 \frac{|\mathcal B_{s,k}(\Gamma)|}{\binom ns}
 \le n\frac{(s)_k}{(n)_k}
 \le n\left(\frac{s}{n}\right)^k.
 \tag{3.3}
\]

#### Proof

Choose the starting position of a length-\(k\) interval in \(n\) ways,
force those \(k\) labels into \(S\), and choose the other \(s-k\)
labels arbitrarily.  This overcounts sets having several long runs and
therefore proves (3.2).  Division by \(\binom ns\) gives the falling
factorial ratio.  Finally, for \(0\le j<k\),

\[
                         \frac{s-j}{n-j}\le\frac sn,
\]

which proves (3.3). \(\square\)

### Theorem 3.2 (arbitrary root-dependent affine slopes)

Let \(C_q^-(\alpha)\) and \(C_q^+(\alpha)\) be the numbers of lower and
upper targets having positive load in (2.2)--(2.3).  Then

\[
 \frac{C_q^-(\alpha)}{\binom n{m-q}}
 \le n\varphi(n)
 \frac{(m-q)_{H-q}}{(n)_{H-q}}
 \le n^2\left(\frac{m-q}{n}\right)^{H-q},
 \tag{3.4}
\]

for \(0\le q<H\), and

\[
 \frac{C_q^+(\alpha)}{\binom n{m+q}}
 \le n\varphi(n)
 \frac{(m+q)_{H+q}}{(n)_{H+q}}
 \le n^2\left(\frac{m+q}{n}\right)^{H+q}.
 \tag{3.5}
\]

#### Proof

If a target has positive load, one summand of (2.2) or (2.3) survives.
By Lemma 1.1, the target has a run of the required length in
\(\Gamma_a\) for at least one \(a\in\mathbb Z_n^*\).  Therefore its
support lies in

\[
                         \bigcup_{a\in\mathbb Z_n^*}
                         \mathcal B_{s,k}(\Gamma_a).
 \tag{3.6}
\]

Apply Lemma 3.1 and the union bound over \(\varphi(n)\) cycles.  Notice
that this argument does not inspect how \(\alpha\) was chosen. \(\square\)

The translation term in an affine parametrization \(b+ia\) produces
only a rotation of \(\Gamma_a\), so it supplies no additional cyclic
order.  Reversal is already present through \(-a\).

## 4. Critical middle and entrance failure

At \(q=0\), Theorem 3.2 gives

\[
 \frac{C_0(\alpha)}W\le n^2 2^{-H}.
 \tag{4.1}
\]

Since \(H/\log m\to\infty\),

\[
 n^2 2^{-H}
 =\exp\bigl(2\log n-(\log2)H\bigr)
 =\exp\bigl(-(\log2+o(1))H\bigr).
 \tag{4.2}
\]

Equations (2.4) and (4.1) prove (0.6)--(0.8).  This is a deterministic
concentration catastrophe: the correct scalar mean in (0.7) coexists
with vanishing support.

Now take \(q_0=\lceil m^{1/4}\rceil\).  Since \(q_0=o(H)\), (3.4) gives

\[
 \frac{C_{q_0}^-(\alpha)}{N_{q_0}}
 \le n^2 2^{-(H-q_0)}
 =\exp\bigl(-(\log2+o(1))H\bigr).
 \tag{4.3}
\]

For the upper sign,

\[
 \log\left(\frac{m+q_0}{2m}\right)
 =-\log2+O(q_0/m),
 \tag{4.4}
\]

and \((H+q_0)q_0/m=o(1)\).  Hence (3.5) yields

\[
 \frac{C_{q_0}^+(\alpha)}{N_{q_0}}
 \le\exp\bigl(-(\log2+o(1))H\bigr).
 \tag{4.5}
\]

An exact entrance census has \(N_{q_0}\) active phase incidences of each
sign.  By (2.6), at most the targets counted in (4.3)--(4.5) can receive
one.  Therefore the lower and upper entrance hole counts satisfy

\[
 \boxed{
 M_{q_0}^-,M_{q_0}^+
 \ge\left(1-e^{-(\log2+o(1))H}\right)N_{q_0}
 =(1-o(1))W.}
 \tag{4.6}
\]

Because the total active mass equals the target-layer size, the
duplicate excess on either sign is the same quantity:

\[
 \sum_S(b_{q_0}^-(S)-1)_+=N_{q_0}-|\operatorname{supp}b_{q_0}^-|,
 \tag{4.7}
\]

and similarly above.  Thus neither a phase permutation nor a nested tag
flow can repair the entrance failure.

### Corollary 4.1 (uniform nested-window failure)

Fix \(0<\rho<1\).  Uniformly for \(0\le q\le\rho H\),

\[
 \frac{C_q^-(\alpha)}{N_q}
 \le\exp\left(-(1-\rho)\log2\,H+o(H)\right),
 \tag{4.8}
\]

and

\[
 \frac{C_q^+(\alpha)}{N_q}
 \le\exp\left(-\log2\,H+o(H)\right).
 \tag{4.9}
\]

#### Proof

The lower bound has \(H-q\ge(1-\rho)H\).  For the upper bound,

\[
 (H+q)\log\left(\frac{m+q}{2m}\right)
 \le-(\log2)(H+q)+O(Hq/m+q^2/m).
 \tag{4.10}
\]

Here \(Hq/m+q^2/m=O(H^2/m)=O(\log m)=o(H)\), while the polynomial
prefactor contributes only \(O(\log m)=o(H)\). \(\square\)

This is simultaneous in depth because every possible selected window,
under every possible root-dependent affine slope, is already contained
in the deterministic envelopes (3.6).  No independence between depths
has been used.

## 5. The general orbit-size threshold

The proof did not use the arithmetic form of \(\Gamma_a\) except to
bound the number of available master cycles.

### Theorem 5.1 (master-library entropy obstruction)

Let \(\mathfrak L\) be any library of \(L\) directed cyclic orders on
\([n]\).  For each root, choose an arbitrary member of \(\mathfrak L\),
with unrestricted global dependence, and restrict it to the root top.
Then the number of middle owners covered is at most

\[
                         Ln2^{-H}W.
 \tag{5.1}
\]

Consequently a family covering \((1-o(1))W\) middle owners must satisfy

\[
                         L\ge(1-o(1))\frac{2^H}{n}.
 \tag{5.2}
\]

#### Proof

Repeat (3.6) with \(\mathfrak L\) in place of the affine cycles and use
Lemma 3.1 with \(s=m,k=H\). \(\square\)

If a finite group \(G\le S_n\) acts on one master cycle, its orbit has
size at most \(|G|\).  Hence every group-orbit construction with

\[
                         \log|G|=o(H)
 \tag{5.3}
\]

covers \(o(W)\) middle owners.  This includes the cyclic and affine
groups, every fixed-dimensional linear or projective group over a field
of polynomial size, and every fixed-depth recursive group whose total
orbit size is \(\exp(o(H))\).

The conclusion is strictly about **restriction frames**.  A difference
family that builds the order of \(U_A\) intrinsically from \(A\), rather
than by restricting one of a small number of ambient cycles, is not
covered unless its possible ambient extensions form such a small
library.

## 6. Audited boundary

Proved here:

1. the exact run criterion for all promotion windows obtained by
   restricting ambient cyclic orders;
2. exact physical middle, lower, and upper target load formulae for an
   arbitrary globally coupled affine slope assignment;
3. the correct total middle and signed incidence masses;
4. a deterministic \((1-o(1))W\) middle hole and duplicate excess for
   the full affine family;
5. a two-sided \((1-o(1))W\) entrance hole, unaffected by phase cuts or
   nested tags;
6. uniform failure throughout every fixed inner fraction of the
   Gaussian window; and
7. the necessary \(\exp(\Omega(H))\) ambient-order entropy threshold.

Not proved:

1. a no-go for intrinsic root-dependent difference orders with
   \(\exp(\Omega(H))\) or larger order entropy;
2. a construction coordinating the full \(\binom mH\)-root star;
3. an owner near-factor or two-sided entrance transversal; or
4. the constant-one theorem.

The exact lesson is that global dependence alone is insufficient.  A
small algebraic orbit can correlate every root decision and still miss
almost every physical target, because its nested windows live inside a
vanishing union of long-run events.  The next viable algebraic family
must be root-intrinsic and high-entropy, not an affine conjugate or
restriction of a bounded master catalogue.
