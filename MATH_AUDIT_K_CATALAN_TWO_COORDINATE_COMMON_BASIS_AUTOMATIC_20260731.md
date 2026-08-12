# Independent audit of the automatic two-coordinate common basis

Date: 2026-07-31  
Lane: K, recursive residual/collar interface  
Status: **GO** for the requested load-bearing theorem; only the physical
side-forest row remains

## 1. Provenance

The requested source was

```text
MATH_THEOREM_CATALAN_TWO_COORDINATE_COMMON_BASIS_AUTOMATIC_20260731.md
SHA-256 f43a8ea28db892370a509bf5fcaae65f24e33d0ecfa209f6a5a01716f0d3d53c
```

Those bytes were present and read at the beginning of this audit.  During
the audit the shared file advanced to

```text
SHA-256 4e5be1a9ba646edd713a3cffe3453cbcfe22e3f4bc61f680bd1b8f1bc055d0f2
```

by adding the balanced common-basis distribution corollary.  It then
advanced once more to

```text
SHA-256 b0979c3c3cbaceda8159c3857f2dc396c0a9b3935bb4d8141e8b333ba2cdda3a
```

by explicitly dispatching the empty Hall subfamily before introducing its
real-binomial parameter.  Lemma 3.1,
Theorem 4.1, and Theorem 5.1—the requested load-bearing statements—remain
the same as in the captured initial read.  The clean-room finite artifact is
deliberately fail-closed and records the delegated/current hash mismatch.
The added distribution corollary is audited separately in Section 6 below.

## 2. Real-binomial domain and the endpoint chord

Put

\[
 B_j(x)=\binom{x}{j},\qquad
 t=x-n+1,qquad
 A(t)=\sum_{j=2}^{n-1}\frac1{t+j}.
\]

For a nonempty \(n\)-uniform family, the Lovasz parameter satisfying
\(|\mathcal A|=B_n(x)\) has \(x\ge n\); thus every later use has \(t>0\).
The empty family is dispatched separately in Hall and rank inequalities.
There is no generalized-binomial sign issue.

Let \(x_0\) satisfy \(B_n(x_0)=z=\operatorname{Cat}_n\).  The exact ratio

\[
 \frac{z}{\binom{2n-2}{n}}
 =\frac{2(2n-1)}{(n+1)(n-1)}
\]

is at most one exactly when \(n^2-4n+1\ge0\), hence for every integer
\(n\ge4\).  Therefore \(x_0\le2n-2\).  The two-step Lovasz shadow bound is
legitimate: iterate the one-step theorem, using monotonicity of the real
binomial parameter, to obtain

\[
                         |\partial_2\mathcal A|\ge B_{n-2}(x).
\]

At \(x=x_0\),

\[
 \frac{B_{n-2}(x_0)}{B_n(x_0)}
 =\frac{n(n-1)}{(x_0-n+1)(x_0-n+2)}\ge1.
\]

Also \(R=N-C=P-z\).  Hence the affine chord in Lemma 3.1 equals \(z\) at
the left endpoint and \(P\) at the right endpoint \(a=M\).  Both endpoint
inequalities are exact.

## 3. Derivative-ratio audit of Lemma 3.1

The logarithmic derivatives are

\[
 \frac{B'_{n-2}(x)}{B_{n-2}(x)}=A(t),
 \qquad
 \frac{B'_n(x)}{B_n(x)}
 =A(t)+\frac1t+\frac1{t+1}.
\]

Together with

\[
 \frac{B_{n-2}(x)}{B_n(x)}=\frac{n(n-1)}{t(t+1)},
\]

this gives exactly

\[
 \frac{B'_{n-2}(x)}{B'_n(x)}
 =\frac{n(n-1)}{t(t+1)+(2t+1)/A(t)}.
\]

The denominator \(D(t)\) has derivative

\[
 D'(t)=2t+1+\frac2{A(t)}
       -\frac{(2t+1)A'(t)}{A(t)^2}>0,
\]

because \(A(t)>0\) and \(A'(t)<0\).  Thus the derivative ratio is strictly
decreasing.  Since \(B'_n(x)>0\), the chord error derivative changes sign
at most once and only from positive to negative.  The error has no interior
minimum, so its two nonnegative endpoint values prove Lemma 3.1.  This is a
maximum-shaped, not a convexity, argument; its direction is correct.

## 4. Dual-rank inequality

For either two-step transversal matroid \(T\), the exact rank formula is

\[
 r_T(Y)=\min_{Z\subseteq Y}
        \bigl(|Y|-|Z|+|\partial_2Z|\bigr).
\]

Equivalently, with

\[
 \delta(Y)=\max_{Z\subseteq Y}
            \bigl(|Z|-|\partial_2Z|\bigr),
\]

one has \(r_T(Y)=|Y|-\delta(Y)\).  Take \(Y=X-A\), \(|A|=a\le N\).

For \(|Z|\le z\), the endpoint-bank lemma makes the deficit nonpositive.
For \(|Z|\ge z\), Lemma 3.1 gives

\[
 |Z|-|\partial_2Z|
 \le\frac CN(|Z|-z)
 \le\frac CN(M-a-z)
 =\frac CN(N-a).
\]

Since \(r_T(X)=P\), duality now yields

\[
 r_{T^*}(A)
 =a-P+r_T(X-A)
 =C-\delta(X-A)
 \ge\frac CN a.
\]

Every domain restriction used here is necessary and satisfied.  The upper
case follows by complementation.  The integer rank is consequently at least
\(\lceil Ca/N\rceil\).

## 5. Pullback and Edmonds common basis

Let \(|E|=N\), and let \(\tau,\eta:E\to X\) be injections.  Pullback along
an injection is the restriction of \(T^*\) to its image, relabelled onto
\(E\); no contraction or surjectivity assumption is hidden here.  Applying
the dual-rank bound to the \(N\)-element image shows that each pullback has
rank at least \(C\), and the ambient dual rank is exactly \(C\), so both
pullback ranks equal \(C\).

For every \(S\subseteq E\),

\[
 r_\tau(S)+r_\eta(E-S)
 \ge\frac CN|S|+\frac CN(N-|S|)=C.
\]

Edmonds' matroid-intersection min--max theorem therefore gives a common
independent set of order \(C\), necessarily a basis of both pullbacks.  No
disjointness or compatibility between \(\tau(E)\) and \(\eta(E)\) is
required.

For a child Catalan linear forest, orient every physical path consistently.
Then its tail and head maps are injections.  A common dual basis \(Q\) has
complements \(X-\tau(Q)\) and \(X-\eta(Q)\) which are bases of the two
primal transversal matroids, exactly the two saturating diagonal matchings
in Theorem 6.1.  An arbitrary edge-by-edge orientation of an undirected
path would not suffice; consistent directed-path orientation is the exact
application hypothesis and is always available.

## 6. Balanced common-basis distribution in the current source

The strengthened current source adds a valid corollary.  The constant vector

\[
                         x_e=C/N\qquad(e\in E)
\]

has total mass \(C\), and the dual-rank theorem gives
\(x(S)\le r_i(S)\) for both pullback matroids and every \(S\subseteq E\).
Thus it lies in both base polytopes.  The two-matroid intersection polytope
is integral; its order-\(C\) face is the convex hull of common bases.
Consequently there is a distribution on common bases with exact marginal
\(C/N\) on every child edge, and every nonnegative additive cost has a
common basis no more expensive than its uniform-density average.

This proves no negative dependence or concentration and does not select
forest-compatible representatives.

## 7. Clean-room numerical audit, \(n=4,\ldots,12\)

An independently written checker exhausts the exact Kruskal--Katona
two-shadow cardinality profile for every family size
\(0,\ldots,\binom{2n}{n}\), inserts it into the transversal-rank formula,
and checks every \(a=0,\ldots,N\).  Across \(n=4,\ldots,12\), it checked

\[
                         3,660,521
\]

family sizes.  Every instance of the endpoint-bank inequality, chord
inequality, dual-rank density and Edmonds rank sum passed.  The exact
dual rank at \(a=N\) was \(C\) in every case.

It also checked the derivative identity on 648 exact rational points and
found the ratio strictly decreasing at every consecutive point.  The
endpoint roots were independently evaluated at 80-digit precision.  These
finite checks corroborate, but do not replace, the proof above.

Artifacts:

```text
scratch/audit_k_catalan_two_coordinate_common_basis_cleanroom_20260731.py
SHA-256 1ad47336a479a97ca36297e1bec8952138b5354da2550ad1e1bbef44e82fb10e

scratch/k_catalan_two_coordinate_common_basis_cleanroom_20260731.audit.json
SHA-256 66a9c085b622a4f94addef91e439e4f0cf507b136b1df342066115f421fd5d0c
```

The JSON status is deliberately
`PASS_CURRENT_BYTES_DELEGATED_HASH_MISMATCH`; it binds the current source
SHA and cannot be mistaken for a byte-level replay of the unavailable old
file after the concurrent update.

## 8. Exact residual-synthesis consequence

**Synchronized incidence is closed for every \(n\ge4\).**  The generic
logarithmic-residual obstruction and absorber-pressure theorems are
unchanged, but in the deterministic two-coordinate recursive route the
following are no longer hypotheses:

* separate one-sided endpoint Hall;
* a synchronized common deletion basis; and
* additive-risk balancing of the common basis.

The sole remaining central collar row is physical realization of a
guaranteed common basis: choose its two diagonal representatives so that
both punctured side graphs have maximum degree at most two, seam anchors
have side degree at most one, and the contracted seam-attachment multigraph
is a forest.  No integral side-forest construction, residence/deep-shadow
compiler, or \(\nu=B\) theorem follows from incidence alone.

## 9. Verdict

**GO.**  No hidden Lovasz--Kruskal--Katona domain error, rank-formula error,
pullback defect, or Edmonds quantifier failure was found.  The requested
common basis theorem is valid, and the current balanced-distribution
extension is valid.  The exact remaining theorem is the physical punctured-
side forest realization.
