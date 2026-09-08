# PBBS \(q\)-fan multiplicity is unbounded in a fixed Gaussian window

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or
external input is used.

## 0. Outcome

Let \(f\) be the canonical cyclic-parenthesis/PBBS permutation of
\(\binom{\mathbb Z_n}{m}\), where \(n=2m+1\), and put \(g=f^2\). For

\[
 S\in\binom{\mathbb Z_n}{m-q},
\]

write

\[
 \mu_q(S)
 =
 \#\left\{A\in\binom{\mathbb Z_n}{m}:
       \bigcap_{t=0}^{q}g^t(A)=S\right\}.          \tag{0.1}
\]

Thus \(\mu_q(S)\) is the correct lower \(q\)-fan multiplicity.

This note proves the following explicit theorem. For every \(q\ge1\), set

\[
 d=2q+1,\qquad n=d^2,\qquad
 m=\frac{d^2-1}{2}=2q(q+1),                       \tag{0.2}
\]

and, writing every \(x\in\mathbb Z_{d^2}\) uniquely as \(x=ad+b\) with
\(0\le a,b<d\), put

\[
 S_q=\{ad+b:0\le a<d,\ 0\le b<q\}.                \tag{0.3}
\]

Then

\[
 |S_q|=dq=m-q
\]

and

\[
 \boxed{\mu_q(S_q)\ge 2q+1=\sqrt{2m+1}.}          \tag{0.4}
\]

In fact \((2q+1)\mid\mu_q(S_q)\). The \(2q+1\) distinct rotations in the
target necklace of \(S_q\) all satisfy the same lower bound. Since

\[
 \frac q{\sqrt m}\longrightarrow\frac1{\sqrt2},  \tag{0.5}
\]

this is an unbounded pointwise multiplicity family inside one fixed
Gaussian window.

The mechanism is sharp for rotational stabilizers. For every target at
depth \(q\),

\[
 \boxed{|\operatorname {Stab}(S)|
 \mid\gcd(2m+1,2q+1),}
\qquad
 |\operatorname {Stab}(S)|\le2q+1.               \tag{0.6}
\]

Thus rotation alone can force at most linear multiplicity. A
superpolynomial lower bound, if true, must produce many distinct free
stabilizer orbits of PBBS occurrences by the unmatched-mark dynamics; it
cannot come from a larger cyclic stabilizer.

## 1. Rotation equivariance and freeness on the middle layer

Let \(\rho(x)=x+1\) on \(\mathbb Z_n\). In a cyclic binary word of weight
\(m\), forward parenthesis matching leaves a unique unmatched zero. Denote
it by \(r_+(A)\). The PBBS permutation is

\[
 f(A)=A^c\setminus\{r_+(A)\}.                     \tag{1.1}
\]

### Lemma 1.1 (PBBS is rotation equivariant)

For every \(j\in\mathbb Z\),

\[
 f(\rho^jA)=\rho^jf(A),\qquad
 g(\rho^jA)=\rho^jg(A).                           \tag{1.2}
\]

#### Proof

Cyclic parenthesis matching is defined without a distinguished origin.
Rotating a matched cyclic word rotates every matched pair and its unique
unmatched zero. Hence

\[
 r_+(\rho^jA)=\rho^jr_+(A).
\]

Complementation also commutes with rotation, so (1.1) gives the first
identity in (1.2). Squaring gives the second. \(\square\)

### Lemma 1.2 (the rotation action on middle sets is free)

No nonidentity rotation fixes a member of
\(\binom{\mathbb Z_n}{m}\).

#### Proof

Suppose a rotation \(\rho^j\) of order \(e\) fixes \(A\). Every orbit of
\(\langle\rho^j\rangle\) on \(\mathbb Z_n\) has size \(e\), so \(A\) is
a union of \(e\)-element orbits and \(e\mid m\). Also \(e\mid n\). But

\[
 \gcd(n,m)=\gcd(2m+1,m)=1.
\]

Therefore \(e=1\), and the rotation is the identity. \(\square\)

For a target \(S\), let

\[
 H_S=\operatorname {Stab}_{\langle\rho\rangle}(S),
\qquad h(S)=|H_S|.
\]

### Proposition 1.3 (stabilizer divisibility of a \(q\)-fan)

For every \(S\in\binom{\mathbb Z_n}{m-q}\),

\[
 \boxed{h(S)\mid\mu_q(S).}                        \tag{1.3}
\]

Consequently, if \(\mu_q(S)>0\), then

\[
 \mu_q(S)\ge h(S).                                \tag{1.4}
\]

#### Proof

Let

\[
 \mathcal O_q(S)
 =
 \left\{A\in\binom{\mathbb Z_n}{m}:
       \bigcap_{t=0}^{q}g^t(A)=S\right\}.
\]

For \(h\in H_S\), Lemma 1.1 gives

\[
 \bigcap_{t=0}^{q}g^t(hA)
 =
 h\left(\bigcap_{t=0}^{q}g^t(A)\right)
 =hS=S.
\]

Thus \(H_S\) acts on \(\mathcal O_q(S)\). Lemma 1.2 says that the action
is free: a nonidentity \(h\) cannot fix its initial middle set \(A\).
Every \(H_S\)-orbit in \(\mathcal O_q(S)\) therefore has exactly \(h(S)\)
elements. Their disjoint union has size \(\mu_q(S)\), proving (1.3) and
(1.4). \(\square\)

The audited all-depth PBBS corridor theorem states that

\[
 \mu_q(S)\ge1
 \quad
 (1\le q\le m,\ |S|=m-q).                         \tag{1.5}
\]

It is Theorem 5.1 of
MATH_ATTACK_AD15_DIRECT_PBBS_ALLQ_EROSION_AUDIT_20260725.md; the same
complete-support conclusion is retained in Section 8 of
MATH_NOTE_DIRECT_PBBS_TARGET_COUNT_AND_RIGGING_NOGO_20260726.md.
Combining (1.4) with (1.5) gives the unconditional bound

\[
 \boxed{\mu_q(S)\ge h(S)}                          \tag{1.6}
\]

for every correct-rank target.

## 2. The exact ceiling on the rotational mechanism

### Proposition 2.1 (rank forces the stabilizer order)

For every \(S\in\binom{\mathbb Z_n}{m-q}\),

\[
 h(S)\mid\gcd(n,m-q)
       =\gcd(n,2q+1).                              \tag{2.1}
\]

In particular \(h(S)\le2q+1\).

#### Proof

Every orbit of \(H_S\) on the regular cyclic ground set has \(h(S)\)
points. Since \(S\) is a union of such orbits,

\[
 h(S)\mid |S|=m-q.
\]

Also \(h(S)\mid n\). As \(n\) is odd,

\[
 \begin{aligned}
 \gcd(n,m-q)
 &=\gcd(n,2m-2q)\\
 &=\gcd(n,n-(2q+1))\\
 &=\gcd(n,2q+1).
 \end{aligned}
\]

This proves (2.1), and the final inequality is immediate. \(\square\)

Thus the largest stabilizer permitted by rank is \(2q+1\). The next
section realizes it exactly.

## 3. A two-parameter family attaining the stabilizer ceiling

Let \(d,L\ge3\) be odd, and put

\[
 q=\frac{d-1}{2},\qquad
 n=dL,\qquad
 m=\frac{dL-1}{2},\qquad
 r=\frac{L-1}{2}.                                 \tag{3.1}
\]

On \(\mathbb Z_{dL}\), define

\[
 S_{d,L}
 =
 \{aL+b:0\le a<d,\ 0\le b<r\}.                   \tag{3.2}
\]

Then

\[
 |S_{d,L}|=dr
 =\frac{d(L-1)}2
 =m-q.                                            \tag{3.3}
\]

### Lemma 3.1 (exact target stabilizer)

\[
 \boxed{
 \operatorname {Stab}(S_{d,L})
 =\langle\rho^L\rangle,
 \qquad
 |\operatorname {Stab}(S_{d,L})|=d.}             \tag{3.4}
\]

#### Proof

Every multiple of \(L\) preserves the residue \(b\bmod L\), so
\(\langle\rho^L\rangle\) fixes \(S_{d,L}\) and has order \(d\).

Conversely, if \(\rho^t\) fixes \(S_{d,L}\), reduction modulo \(L\) says
that translation by \(t\bmod L\) fixes the interval

\[
 I=\{0,1,\ldots,r-1\}\subset\mathbb Z_L.
\]

If that translation has order \(e\), then \(I\) is a union of
\(e\)-element orbits. Hence \(e\mid r\) and \(e\mid L\). But

\[
 \gcd(L,r)
 =\gcd\left(L,\frac{L-1}{2}\right)=1
\]

because \(L\) is odd. Thus \(e=1\), so \(t\equiv0\pmod L\). Therefore
the full stabilizer is exactly \(\langle\rho^L\rangle\). \(\square\)

### Theorem 3.2 (unbounded \(q\)-fan multiplicity)

For the parameters (3.1)--(3.2),

\[
 \boxed{
 d\mid\mu_q(S_{d,L}),
 \qquad
 d\le\mu_q(S_{d,L})
 \le\binom dq.}                                   \tag{3.5}
\]

The rotation necklace of \(S_{d,L}\) has exactly \(L\) targets, and every
one of them obeys (3.5).

#### Proof

Lemma 3.1 and Proposition 1.3 give the divisibility. The support theorem
(1.5) makes the multiplicity positive, proving the lower bound.

The upper bound is the exact cap in the all-depth corridor theorem:

\[
 \mu_q(S)\le\binom{2q+1}{q}=\binom dq.
\]

Orbit--stabilizer gives \(n/d=L\) distinct rotations of \(S_{d,L}\).
Lemma 1.1 bijects the occurrence fibres of two rotated targets, so all
their multiplicities are equal. \(\square\)

This family can be placed at any prescribed fixed Gaussian ratio. If
\(d\to\infty\) through odd values and \(L=L(d)\to\infty\) through odd
values with

\[
 \frac Ld\longrightarrow c\in(0,\infty),
\]

then

\[
 \frac q{\sqrt m}
 =
 \frac{(d-1)/2}{\sqrt{(dL-1)/2}}
 \longrightarrow\frac1{\sqrt{2c}},               \tag{3.6}
\]

while \(\mu_q(S_{d,L})\ge d=2q+1\to\infty\).

Taking \(L=d=2q+1\) gives exactly (0.2)--(0.4). In that square family the
target necklace itself has \(d=2q+1\) members.

## 4. Exact necklace-wide pair and floor-energy lower bounds

For any target histogram define its unordered collision count

\[
 P_q=\sum_{|T|=m-q}\binom{\mu_q(T)}2.              \tag{4.1}
\]

Theorem 3.2 gives, without any assumption on the remaining targets,

\[
 \boxed{
 P_q\ge L\binom d2.}                              \tag{4.2}
\]

Indeed the target necklace has \(L\) distinct members, each of load at
least \(d\).

For the square Gaussian family \(L=d=2q+1\), let

\[
 W=\binom{2m+1}{m},\qquad
 N_q=\binom{2m+1}{m-q}.
\]

Exact factorial cancellation and Taylor expansion give

\[
 \log\frac W{N_q}
 =
 \frac{q(q+1)}m+O\!\left(\frac{q^3}{m^2}\right)
 =
 \frac12+O\!\left(\frac1q\right).                 \tag{4.3}
\]

Hence \(1<W/N_q<2\) for all sufficiently large \(q\), so the relevant
ambient integer floor is one. Moreover complete support gives

\[
 1\le\frac1{N_q}\sum_{|T|=m-q}\mu_q(T)
 \le\frac W{N_q}<2,                               \tag{4.3a}
\]

because every target occurs and each of the \(W\) starts contributes to
at most one correct target. Thus the correct-window histogram itself also
has floor one. The floor-one quadratic is

\[
 \Phi_q
 =
 \frac12\sum_{|T|=m-q}
   (\mu_q(T)-1)(\mu_q(T)-2).                       \tag{4.4}
\]

Every summand is nonnegative for integral \(\mu_q(T)\). The \(d\) targets
in the distinguished necklace therefore give

\[
 \boxed{
 \Phi_q
 \ge
 \frac{d(d-1)(d-2)}2
 =
 (\sqrt2+o(1))m^{3/2}.}                           \tag{4.5}
\]

This is a genuine pointwise-spike lower bound, but it is
\(o(\operatorname {Cat}_m)\). It therefore refutes uniform bounded
multiplicity without by itself obstructing a Catalan-scale global energy
bound.

## 5. Exact proved boundary

Proved:

1. PBBS \(q\)-fan multiplicity is unbounded even when
   \(q/\sqrt m\to1/\sqrt2\).
2. More generally, unbounded multiplicity occurs at every fixed positive
   Gaussian ratio along an explicit arithmetic subsequence.
3. The lower bound is exact at the level of the forcing mechanism:
   \(h(S)\mid\mu_q(S)\), and the largest possible rotational stabilizer is
   \(2q+1\), attained by the displayed targets.
4. The whole distinguished target necklace, not merely one target, has
   load at least \(2q+1\).

Not proved:

1. an exact formula for \(\mu_q(S_{d,L})\);
2. a superpolynomial lower bound for one target;
3. a Catalan-scale lower bound for total PBBS floor energy.

After quotienting by the stabilizer, the residual integer is

\[
 a_q(S):=\frac{\mu_q(S)}{h(S)}.
\]

Rotation proves only \(a_q(S)\ge1\). Since (0.6) caps
\(h(S)\) linearly, any superpolynomial construction must prove that
\(a_q(S)\) itself is superpolynomial by exhibiting many genuinely
different unmatched-mark histories. This is the exact remaining dynamic
lane.
