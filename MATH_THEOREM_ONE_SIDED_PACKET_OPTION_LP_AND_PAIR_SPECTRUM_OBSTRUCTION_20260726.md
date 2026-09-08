# One-sided packet options: exact fractional dual, exact product criterion, and a pair-spectrum obstruction

Date: 2026-07-26

## 0. Verdict

Let \({\cal P}\) be the retained packets.  Packet \(P\) must choose one
whole legal compiler option \(\omega\in\Omega_P\), and that one option is
used for both signs and every protected depth.  Write

\[
 a_{P\omega t}={\bf1}_{\{t\in I_P^\omega\}},
 \qquad
 {\cal T}=\bigsqcup_{q\le H,\epsilon=\pm}{\cal T}_{q}^{\epsilon}.
\]

The exact one-sided problem is a partition-constrained maximum-coverage
problem.  It has two useful formulations.

1.  Its natural linear relaxation has the exact dual

    \[
    h_{\rm frac}
     =\max_{0\le y_t\le1}
       \left\{\sum_ty_t-
       \sum_{P}\max_{\omega\in\Omega_P}
                    \sum_{t\in I_P^\omega}y_t\right\}.
    \tag{0.1}
    \]

    Normalized conjugacy averaging makes this relaxation have value zero
    whenever every typed target has fractional load at least one.  Thus
    the weighted one-point Hall gate is genuinely closed in the convex
    hull.

2.  If \(x_P\in\Delta(\Omega_P)\) and

    \[
       p_{Pt}=\sum_\omega x_{P\omega}a_{P\omega t},
    \]

    then

    \[
       \Psi(x)=\sum_{t\in{\cal T}}\prod_{P\in{\cal P}}(1-p_{Pt})
    \tag{0.2}
    \]

    is the expected number of holes under independent whole-packet
    choices.  More strongly,

    \[
       \boxed{\min_{\omega_P}H((\omega_P)_P)
       =\min_{x\in\prod_P\Delta(\Omega_P)}\Psi(x).}
    \tag{0.3}
    \]

    Hence coefficient one follows from, and in this packet model is
    equivalent to, finding one common all-depth product point with
    \(\Psi(x)=o(W)\).  Conditional expectation rounds it without loss.

The normalized conjugacy point does not meet (0.2).  When its hits are
diffuse and the fractional load of a shallow target is
\(1+o(1)\), its hole probability is \(e^{-1}+o(1)\).  Pair codegrees of
individual compiler images do not repair this.  There are arbitrarily
large packet systems with:

* total mass \(G=(1+o(1))N\);
* fractional target load at least one;
* one-target and every admissible two-target probability asymptotic to
  the independent values \(1/k\) and \(1/k^2\); but
* every integral whole-packet assignment leaves a fixed positive fraction
  of the targets uncovered.

Therefore no near-cover theorem based only on normalized conjugacy
marginals and compiler-image pair codegrees can prove constant one.  A
positive theorem must use higher-order whole-option structure, such as a
near-resolution into realizable home bundles, or prove (0.2) directly by
a strongly nonuniform correlated design.

## 1. Exact fractional LP and dual

The standard relaxation is

\[
\begin{aligned}
 h_{\rm frac}=\min\quad &\sum_th_t\\
 \text{subject to}\quad
 &h_t+\sum_{P,\omega}a_{P\omega t}x_{P\omega}\ge1
       &&(t\in{\cal T}),\\
 &\sum_{\omega\in\Omega_P}x_{P\omega}=1
       &&(P\in{\cal P}),\\
 &h_t,x_{P\omega}\ge0.
\end{aligned}
\tag{1.1}
\]

### Theorem 1.1 (exact dual)

Equation (0.1) is the dual value of (1.1).

#### Proof

Give the first constraints multipliers \(y_t\ge0\) and the packet
equalities free multipliers \(\beta_P\).  Finiteness of the infimum over
\(h_t\ge0\) gives \(y_t\le1\).  Finiteness over
\(x_{P\omega}\ge0\) gives

\[
 \beta_P\ge\sum_ta_{P\omega t}y_t
 \quad(\omega\in\Omega_P).
\]

Minimizing \(\beta_P\) gives
\(\beta_P=\max_\omega\sum_{t\in I_P^\omega}y_t\), and the dual
objective is \(\sum_ty_t-\sum_P\beta_P\).  Strong finite-dimensional
LP duality proves (0.1). \(\square\)

Suppose distributions \(x_P\) satisfy

\[
                         \sum_Pp_{Pt}\ge1
                         \qquad(t\in{\cal T}).       \tag{1.2}
\]

Then \(h=0\) is feasible in (1.1).  Equivalently, for every
\(0\le y\le1\),

\[
\begin{aligned}
 \sum_ty_t
 &\le\sum_{P,\omega}x_{P\omega}
                    \sum_{t\in I_P^\omega}y_t\\
 &\le\sum_P\max_\omega\sum_{t\in I_P^\omega}y_t.
\end{aligned}
\tag{1.3}
\]

Uniform normalized conjugacy is one common distribution on whole legal
states, not a separate copy of source capacity for each target.  If its
annealed load is at least one at every retained typed target, (1.2)
applies simultaneously to the disjoint union of all depths and signs.
This is the precise positive content of conjugacy flattening.

## 2. Exact integral product criterion

For a deterministic assignment \(\boldsymbol\omega=(\omega_P)_P\),

\[
 H(\boldsymbol\omega)
 =\sum_t\prod_P(1-a_{P\omega_Pt}).                  \tag{2.1}
\]

If the packet options are sampled independently from \(x_P\), taking
expectations in (2.1) gives (0.2).

### Theorem 2.1 (whole-packet conditional expectation)

Equation (0.3) holds.  In particular, every product point \(x\) can be
rounded to one deterministic common all-depth option assignment with at
most \(\Psi(x)\) holes.

#### Proof

The function \(\Psi\) is affine in each packet simplex separately.
Fix all other packet distributions and replace \(x_P\) by a vertex of
its simplex having no larger value.  Iterating over the packets produces
a deterministic assignment and does not increase \(\Psi\).  Conversely,
every deterministic assignment is already a product point, proving
equality of the two minima. \(\square\)

The elementary estimate

\[
 \Psi(x)\le\sum_t\exp\left(-\sum_Pp_{Pt}\right)     \tag{2.2}
\]

is useful only when the fractional loads diverge or become polarized.
At shallow depths their average is \(G/N_q=1+o(1)\).  If additionally
\(\max_Pp_{Pt}=o(1)\) and \(\sum_Pp_{Pt}=1+o(1)\), then

\[
 \prod_P(1-p_{Pt})=e^{-1+o(1)}.                    \tag{2.3}
\]

Thus uniform diffuse conjugacy gives a linear product-hole ledger.  Its
two-target spectrum does not enter (2.3).

## 3. Exact binary obstruction

The failure of pair information is already exact at load one.  Let
\(V=\mathbb F_2^r\setminus\{0\}\), \(L=|V|=2^r-1\), and take targets

\[
                         {\cal T}=V\times\mathbb F_2.
\]

There are two packets.  Both have the option set
\(\Omega=\mathbb F_2^r\), and option \(a\) has image

\[
                         I^a=\{(v,a\cdot v):v\in V\}.             \tag{3.1}
\]

Every option is injective and has mass \(L\), so the total occurrence
mass is \(2L=|{\cal T}|\).

Under the uniform option distribution,

\[
 \Pr((v,b)\in I^a)=\frac12,                         \tag{3.2}
\]

and, for distinct \(v,w\),

\[
 \Pr((v,b),(w,c)\in I^a)=\frac14.                  \tag{3.3}
\]

Indeed distinct nonzero vectors over \(\mathbb F_2\) are linearly
independent.  Thus every target has total fractional load exactly one and
every admissible pair has the independent codegree.

If the two chosen options are equal, exactly \(L\) targets are missed.
If they are distinct, put \(d=a-a'\ne0\).  They agree at precisely

\[
             |\{v\ne0:d\cdot v=0\}|=2^{r-1}-1       \tag{3.4}
\]

coordinates.  At each such coordinate one of its two targets is missed.
Therefore every assignment has

\[
 H\ge2^{r-1}-1=\left(\frac14-o(1)\right)|{\cal T}|. \tag{3.5}
\]

The fractional LP has zero holes, the one- and two-target data are exact,
and the integral gap is linear.

## 4. Diffuse small-marginal obstruction

The preceding example has packet marginal \(1/2\).  The same phenomenon
persists when every packet marginal tends to zero, as in a large compiler
cylinder.

### Theorem 4.1 (pair-generic packet systems with linear unavoidable holes)

There are sequences \(k\to\infty\) and packet systems with

\[
 p_{Pt}=(1+o(1))/k,qquad
 \Pr_\omega(t,t'\in I_P^\omega)=(1+o(1))/k^2          \tag{4.1}
\]

for every pair of compatible targets in two distinct local coordinates,
such that:

1. every target has total fractional load at least one;
2. total occurrence mass is \((1+o(1))N\); and
3. every integral assignment leaves at least \(N/8\) holes.

#### Proof

Put \(L=k^{12}\), \(M=k^6\), \(\varepsilon=k^{-1/2}\), and choose
\(M\) independent uniform words in \([k]^L\).  Let \({\cal C}\) be
the resulting option multiset.  Chernoff bounds and a union bound show
simultaneously that, for every coordinate \(j\), symbol \(a\), and
distinct coordinates \(j,j'\), symbols \(a,b\),

\[
 \frac1M|\{c\in{\cal C}:c_j=a\}|
   ={1\pm\varepsilon\over k},                       \tag{4.2}
\]

\[
 \frac1M|\{c\in{\cal C}:c_j=a,c_{j'}=b\}|
   ={1\pm\varepsilon\over k^2}.                    \tag{4.3}
\]

Indeed the smallest expectation in (4.3) is \(M/k^2=k^4\), while the
relative-error exponent is \(\varepsilon^2k^4=k^3\), much larger than
the logarithm of the \(O(L^2k^2)\) events.

Take

\[
                         P=\lceil(1+3\varepsilon)k\rceil
\]

packets, each with option set \({\cal C}\), and targets
\({\cal T}=[L]\times[k]\).  A word covers
\(I^c=\{(j,c_j):j\in[L]\}\), so every option has mass \(L\).
Equations (4.2)--(4.3) give (4.1), and

\[
 P\frac{1-\varepsilon}{k}>1                         \tag{4.4}
\]

for large \(k\).  Thus the uniform fractional point has zero LP holes.
Also \(G=PL=(1+o(1))kL=(1+o(1))N\).

It remains to choose \({\cal C}\) so that no integral assignment works.
Fix an ordered \(P\)-tuple of option indices, repetitions allowed.  At
one coordinate the expected number of uncovered symbols is at least

\[
 k(1-1/k)^P>(1/4)k                                  \tag{4.5}
\]

for large \(k\); repetitions only increase it.  The coordinate hole
counts are independent, lie in \([0,k]\), and Hoeffding gives

\[
 \Pr\{\text{total holes}<kL/8\}\le e^{-L/32}.       \tag{4.6}
\]

There are at most \(M^P\) ordered assignments, and
\(P\log M=o(L)\).  A union bound makes (4.6) fail for none of them with
probability tending to one.  Intersect this event with (4.2)--(4.3),
whose probability also tends to one.  The resulting deterministic option
family proves the theorem. \(\square\)

For targets in the same local coordinate, different symbols are mutually
exclusive in one option.  This is the unavoidable face-compatibility
relation, not a codegree defect.  Away from that relation, the construction
is pair-generic.

## 5. Consequence for the compiler program

Theorems 3.1 and 4.1 are abstract packet systems, not counterexamples to
the particular diverse-order compiler atlas.  Their scope is nevertheless
sharp:

* zero fractional holes plus near-independent compiler-image pair
  codegrees does not imply an integral near-cover;
* no Pippenger--Spencer-, second-moment-, or pair-spectrum theorem can be
  invoked from those statistics alone; and
* using one common option over all depths only strengthens the
  obstruction, since failure at one typed depth already gives failure of
  the aggregate target.

The exact surviving positive targets are therefore higher order.
Equivalent or sufficient formulations include:

1. prove directly that the multilinear minimum in (0.3) is \(o(W)\);
2. assign all but \(o(W)\) targets to home packets so that each packet's
   assigned bundle lies inside one legal compiler image; or
3. exhibit a distribution on complete global assignments under which the
   probability of being uncovered sums to \(o(W)\).

The second formulation is precisely the compiler-image-shaped bundle
gate.  Pair enumerators can help verify a proposed higher-order bundle
design, but they cannot generate it by themselves.

