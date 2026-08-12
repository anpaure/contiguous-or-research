# Structured packet resolutions: Latin negative covariance and the sparse whole-frame obstruction

Date: 2026-07-26

Method: pure mathematics only.  The only properties of the recursive
context-array factor used below are literal packet legality and the existence,
at every protected signed depth, of one target occurrence per covered middle
owner.  No crossed recursion is used.

## 0. Verdict

Put

\[
 n=2m,\qquad \Omega=\binom{[n]}m,\qquad W=|\Omega|,
 \qquad N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.
\tag{0.1}
\]

There are two different operations which must not be conflated.

1. Averaging complete fixed-frame resolutions can make their **mean** target
   profile uniform, but it cannot lower the expected floor energy.  At
   \(q=A\sqrt m+o(\sqrt m)\), every complete fixed-frame resolution has
   \(\Omega_A(W)\) floor energy.  This remains true for an arbitrary
   distribution over arbitrarily many coordinate frames.
2. Interleaving packets from different frames inside one integral owner
   resolution can create genuine negative covariance.  A precise way to do
   this is to divide the owners into common blocks, give every block the same
   number of integral packet-tiling options, and assign the option labels by
   one global permutation.  The resulting covariance has an exact closed
   formula, given in Theorem 4.1.

There is a further obstruction even before integral rounding.  A convex
combination of \(L\) complete fixed-frame resolutions cannot have bounded
pointwise target load at Gaussian depth unless

\[
 L\ge
 \exp\!\left((A/2+o(1))\sqrt m\log m\right).
\tag{0.2}
\]

This holds without any assumption about how transverse or orthogonal their
coordinate pairings are.  Thus a polynomial, or more generally an
\(\exp(o(\sqrt m\log m))\)-sized, orthogonal frame family does not cancel the
fixed-profile obstruction.  The complete translation one-factorization of
the coordinates is included in this no-go.  The same leading lower bound
holds if the compiler discards the small-dimensional pair strata and starts
only at active dimension \(s=4H+O(1)\); see Corollary 3.2.

This pointwise statement has an important complementary side.  If one first
averages *inside* each frame orbit, then \(L=H^2\omega_m\) random coordinate
frames, where \(\omega_m\to\infty\), have a deterministic realization whose
average profile differs from uniform by only \(o(W)\) in aggregate \(L^1\),
simultaneously over all \(q\le H\) and both signs.  For \(H=A\sqrt m\), one
may take \(L=m\log m\).  Thus a small collection of frame orbits really does
cancel the **aggregate Gaussian fixed-profile cut before owner conflicts**.
It does not cancel floor covariance, and it is not a small-support mixture of
individual integral whole-resolution states.

The exact surviving constructive statement is therefore the following.

> **Latin packet-resolution gate.**  Construct common owner blocks and
> multiframe packet tilings whose incidence arrays satisfy the all-depth
> inequality (4.10).  Then one deterministic permutation of the option
> labels gives an owner-perfect resolution with total floor energy \(o(W)\).

This is strictly stronger than an orthogonal family of whole frames: it asks
for common owner blocks on which different frame packets can be retiled
independently.  Nothing in frame orthogonality alone supplies those blocks.

## 1. Floor energy is integer-minimal variance

Fix one signed depth \(q\).  An integral owner-perfect packet resolution
produces a target load vector

\[
 Z=(Z_T)_{T\in\mathcal T_q},\qquad
 \mathcal T_q=\binom{[n]}{m\pm q},\qquad
 \sum_T Z_T=W.
\tag{1.1}
\]

Put

\[
 \lambda_q={W\over N_q}=c_q+\alpha_q,qquad
 c_q=\lfloor\lambda_q\rfloor,qquad 0\le\alpha_q<1,
\tag{1.2}
\]

and define the floor energy

\[
 Q_q(Z)=\sum_{T\in\mathcal T_q}
       (Z_T-c_q)(Z_T-c_q-1).
\tag{1.3}
\]

Every summand in (1.3) is a nonnegative even integer.  It vanishes exactly
when \(Z_T\in\{c_q,c_q+1\}\).

### Lemma 1.1 (exact variance identity)

Let \(Z\) be a random integral load vector satisfying (1.1) in every
outcome, and suppose its one-point means are uniform:

\[
                         \mathbb E Z_T=\lambda_q
                         \quad(T\in\mathcal T_q).
\tag{1.4}
\]

Then

\[
 \boxed{
 \mathbb E Q_q
 =\sum_T\operatorname {Var}(Z_T)
   -N_q\alpha_q(1-\alpha_q).}
\tag{1.5}
\]

Consequently

\[
 \sum_T\operatorname {Var}(Z_T)
 \ge N_q\alpha_q(1-\alpha_q),
\tag{1.6}
\]

with equality if and only if every \(Z_T\) is supported on
\(\{c_q,c_q+1\}\).  Moreover

\[
 \sum_T\Pr\bigl(Z_T\notin\{c_q,c_q+1\}\bigr)
 \le {1\over2}\mathbb E Q_q.
\tag{1.7}
\]

#### Proof

Expanding one summand and using (1.4) gives

\[
\begin{aligned}
 \mathbb E[(Z_T-c_q)(Z_T-c_q-1)]
 &=\operatorname {Var}(Z_T)
   +\lambda_q^2-(2c_q+1)\lambda_q+c_q(c_q+1)\\
 &=\operatorname {Var}(Z_T)-\alpha_q(1-\alpha_q).
\end{aligned}
\]

Summing proves (1.5).  For an integer-valued random variable of mean
\(c+\alpha\), the nonnegativity of
\((Z-c)(Z-c-1)\) gives
\(\operatorname {Var}(Z)\ge\alpha(1-\alpha)\), with equality precisely
when the displayed product vanishes almost surely.  This proves (1.6) and
its equality statement.  Off \(\{c,c+1\}\), the product is at least two;
Markov's inequality summed over \(T\) gives (1.7). \(\square\)

Thus uniform first moments are only the zero-frequency condition.  The
needed negative covariance is the much stronger assertion that the total
variance is within \(o(W)\) of its smallest value permitted by integrality.

## 2. Complete-frame mixing never has small floor energy

Fix a perfect matching \(M\) of the \(2m\) coordinates.  For a lower target
\(T\) of rank \(m-q\), let \(f_M(T)\) be its number of full \(M\)-pairs.
The exact numbers of targets and middle starts in pair type \(f\) are

\[
 T_{f,q}={m!\,2^{m-2f-q}\over
              f!(f+q)!(m-2f-q)!},
 \qquad
 V_f={m!\,2^{m-2f}\over f!^2(m-2f)!}.
\tag{2.1}
\]

Every complete resolution confined to \(M\) has exactly \(V_f\) target
occurrences in type \(f\).  Hence it misses at least

\[
 D_{m,q}=\sum_f(T_{f,q}-V_f)_+
\tag{2.2}
\]

lower targets.  The same holds on the upper side by complementation.  This
is the resolution-free type-incidence theorem: emptying a window of split
pairs preserves the number of full pairs.

### Theorem 2.1 (whole-resolution covariance no-go)

Let a random integral state be chosen from any collection of complete
fixed-pair resolutions; the coordinate matching and the internal resolution
may both depend arbitrarily on the state.  Then, outcome by outcome,

\[
 \boxed{Q_q\ge c_q(c_q+1)D_{m,q}\ge2D_{m,q}.}
\tag{2.3}
\]

If \(q=A\sqrt m+o(\sqrt m)\), \(A>0\), then

\[
 {D_{m,q}\over W}\longrightarrow
 \delta(A):=e^{-A^2}\Phi(A/2)-\Phi(-3A/2)>0,
\tag{2.4}
\]

and therefore

\[
                         \mathbb E Q_q\ge
                         (2\delta(A)+o(1))W.
\tag{2.5}
\]

In particular, even a distribution whose averaged target profile is exactly
uniform cannot satisfy \(\mathbb E Q_q=o(W)\).

#### Proof

For \(q\ge1\), \(N_q<W\), so \(c_q\ge1\).  Every missed target has load
zero and contributes \(c_q(c_q+1)\) to (1.3).  Equation (2.2) therefore
gives (2.3) in each state.  Averaging cannot change the bound.

For completeness, (2.4) follows from the exact ratio

\[
 {T_{f,q}\over V_f}
 ={(m-2f)_{\underline q}\over2^q(f+1)^{\overline q}}
\tag{2.6}
\]

and the uniform local central limits, with
\(f=m/4+x\sqrt m\),

\[
 {V_f\over W}={4\over\sqrt{2\pi m}}e^{-8x^2}(1+o(1)),
\quad
 {T_{f,q}\over W}={4\over\sqrt{2\pi m}}
 e^{-A^2-8(x+A/2)^2}(1+o(1)).
\tag{2.7}
\]

The inequality \(T_{f,q}>V_f\) has limiting boundary \(x=-3A/8\).
Summing the difference on the corresponding half-line gives (2.4).
The tails outside \(|x|\le K\) are uniformly negligible by the ratio form
of Stirling's estimate, and then \(K\to\infty\).  Positivity is strict
because the two limiting Gaussian densities cross and are not identical.
Substitution in (2.3) proves (2.5). \(\square\)

The obstruction is not a failure of independence.  It holds for every
coupling of the choice of complete frame and complete internal resolution.
What it excludes is using one complete frame state per outcome.

If a physical construction permits \(E_q\) depth-\(q\) starts in an outcome
to leave its declared frame, the identical capacity proof gives at least
\(D_{m,q}-E_q\) holes: every exceptional start can repair at most one target.
Thus (2.5) is unchanged whenever \(E_q=o(W)\).  This is the form applicable
when exponentially light small-dimensional strata are handled separately.

## 3. A sparse catalogue cannot even flatten the fractional profile

The preceding theorem concerns the energy of integral outcomes.  There is
also a support-size obstruction at the fractional, one-point level.

For a fixed frame \(M\), every complete resolution has total type-
\(f\) occurrence mass \(V_f\).  Since there are \(T_{f,q}\) targets of that
type, some target has multiplicity at least

\[
 \lambda_{f,q}:={V_f\over T_{f,q}}
 ={2^q(f+1)^{\overline q}\over(m-2f)_{\underline q}}.
\tag{3.1}
\]

### Theorem 3.1 (aligned-target support lower bound)

Let \(R_1,\ldots,R_L\) be arbitrary complete fixed-pair resolutions, with
arbitrary coordinate frames, and let \(w_1,\ldots,w_L>0\) sum to one.
Write \(z_i(T)\) for the depth-\(q\) target multiplicity in \(R_i\).  If

\[
                    \sum_iw_i z_i(T)\le C
                    \quad\hbox{for every target }T,
\tag{3.2}
\]

then

\[
 \boxed{
 L\ge {1\over C}
       \left({m-q\over q+1}\right)^{q}.}
\tag{3.3}
\]

More precisely, every individual weight satisfies

\[
 w_i\le C\left({q+1\over m-q}\right)^q.
\tag{3.4}
\]

#### Proof

Fix \(i\), let \(M_i\) be its coordinate frame, and put

\[
                         f_*=\left\lfloor{m-q\over2}\right\rfloor.
\tag{3.5}
\]

The type \(f_*\) is nonempty: take \(f_*\) complete \(M_i\)-pairs and,
when \(m-q\) is odd, one endpoint of one further pair.  By the type-total
identity, some target \(T_i\) of this type has
\(z_i(T_i)\ge\lambda_{f_*,q}\).  Now

\[
 m-2f_*\in\{q,q+1\},\qquad 2(f_*+1)\ge m-q.
\tag{3.6}
\]

Using (3.1),

\[
 \lambda_{f_*,q}
 \ge {2^q(f_*+1)^q\over(q+1)^q}
 \ge\left({m-q\over q+1}\right)^q.
\tag{3.7}
\]

All target loads are nonnegative.  Thus (3.2), evaluated at \(T_i\), gives

\[
 C\ge\sum_jw_jz_j(T_i)\ge w_i z_i(T_i)
 \ge w_i\left({m-q\over q+1}\right)^q,
\]

which is (3.4).  Some \(w_i\ge1/L\), giving (3.3). \(\square\)

At Gaussian depth \(q=A\sqrt m+o(\sqrt m)\),

\[
 \log\left({m-q\over q+1}\right)^q
 ={A\over2}\sqrt m\log m+O_A(\sqrt m).
\tag{3.8}
\]

On the other hand,

\[
 {W\over N_q}
 =\prod_{i=0}^{q-1}{m+i+1\over m-i}
 =e^{A^2+o(1)}.
\tag{3.9}
\]

Thus asking (3.2) with the uniform fractional target load
\(C=(1+o(1))W/N_q=O_A(1)\) proves (0.2).

Theorem 3.1 applies, in particular, to an edge-disjoint one-factorization
of \(K_{2m}\), to mutually orthogonal one-factorizations, and to arbitrary
conjugates of such families.  Orthogonality does not affect the aligned
type \(f_*\) spike.

### Corollary 3.2 (the floor-corrected bulk version)

Fix an integer \(s_0\ge q\), of the same parity as \(m\), and put
\(f_0=(m-s_0)/2\).  Suppose every catalogue state resolves every middle
owner of pair type \(f_0\) inside its declared coordinate frame.  Under the
pointwise bound (3.2),

\[
 \boxed{
 L\ge {1\over C}\left({m-s_0\over s_0}\right)^q.}
\tag{3.14}
\]

In particular, for \(q=H=A\sqrt m+o(\sqrt m)\) and
\(s_0=4H+O(1)\),

\[
 \log L\ge {A\over2}\sqrt m\log m+O_A(\sqrt m)-\log C.
\tag{3.15}
\]

#### Proof

The type-total identity again supplies a target of multiplicity at least
\(\lambda_{f_0,q}\).  Since \(m-2f_0=s_0\), (3.1) gives

\[
 \lambda_{f_0,q}
 \ge {2^qf_0^q\over s_0^q}
 =\left({m-s_0\over s_0}\right)^q.
\]

Repeat the maximum-weight argument of Theorem 3.1.  Substitution of
\(s_0=4q+O(1)\) gives (3.15). \(\square\)

### Remark 3.3 (what one one-factorization actually cancels)

Let \(M_1,\ldots,M_{2m-1}\) be a one-factorization.  Then for every target
\(T\),

\[
 {1\over2m-1}\sum_a f_{M_a}(T)
 ={\binom{|T|}2\over2m-1}.
\tag{3.10}
\]

Indeed every coordinate edge internal to \(T\) occurs in exactly one
matching.  Hence a one-factorization kills the linear full-pair profile.
It does not kill nonlinear profiles.  For two disjoint coordinate edges
\(e,e'\), the probability, under the uniform choice of a class of this
one-factorization, that both lie in the chosen matching is either
\(0\) or \(1/(2m-1)\).  Under a uniform random perfect matching it is

\[
                         {1\over(2m-1)(2m-3)}.
\tag{3.11}
\]

Thus the degree-two matching harmonic already survives.

More generally, if a distribution on perfect matchings contains every
fixed \(k\)-matching with the same probability for \(k\le K\), that
probability is forced to be

\[
 \rho_k={1\over(2m-1)(2m-3)\cdots(2m-(2k-1))}.
\tag{3.12}
\]

For every target \(T\), it then reproduces the first \(K\) factorial
moments of \(f_M(T)\) under the full perfect-matching orbit, because

\[
 \mathbb E\binom{f_M(T)}k
 =\rho_k\,{|T|!\over(|T|-2k)!2^kk!}.
\tag{3.13}
\]

Equations (3.10)--(3.13) precisely locate the failure: an orthogonal
one-factorization is only first-moment exact.  The Gaussian-depth profile
(3.1) is not linear in \(f\), and Theorem 3.1 shows that bounded-degree
moment cancellation cannot hide its extreme aligned values in a sparse
nonnegative mixture.

### Theorem 3.4 (sparse frame-orbit cancellation of the aggregate cut)

For a perfect matching \(M\), let

\[
 g_{M,q}(T)=\lambda_{f_M(T),q}
\tag{3.16}
\]

be the target profile obtained by averaging a complete fixed-\(M\)
resolution over the hyperoctahedral stabilizer of \(M\).  This definition is
independent of the internal resolution, by the type-total identity.

Let \(H\le A\sqrt m\), and let \(L\) perfect matchings be chosen
independently and uniformly from all coordinate frames.  Their average
profile is

\[
                         \bar g_q(T)={1\over L}\sum_{\ell=1}^L
                         g_{M_\ell,q}(T).
\tag{3.17}
\]

There is a constant \(C_A\) such that

\[
 \mathbb E\sum_{\epsilon\in\{-,+\}}\sum_{q=1}^H
 \sum_{T\in\mathcal T_{q,\epsilon}}
 \left|\bar g_q(T)-{W\over N_q}\right|
 \le {C_AHW\over\sqrt L}.
\tag{3.18}
\]

Consequently, if \(L/H^2\to\infty\), there is a deterministic collection
of \(L\) frames for which the left side of (3.18) is \(o(W)\).  The frames
may additionally be required to be distinct and to have pairwise common-edge
overlap

\[
                         O\!\left({\log L\over\log\log L}\right).
\tag{3.19}
\]

In particular, \(L=m\log m\) works for \(H=A\sqrt m\).

#### Proof

Fix a target \(T\) of rank \(m-q\), and choose \(M\) uniformly.  A double
count of pairs \((M,T)\) shows

\[
 \Pr(f_M(T)=f)={T_{f,q}\over N_q}.
\tag{3.20}
\]

Therefore

\[
 \mathbb E_M g_{M,q}(T)
 =\sum_f{T_{f,q}\over N_q}{V_f\over T_{f,q}}
 ={W\over N_q}.
\tag{3.21}
\]

The same Stirling expansion as in (2.7) gives a uniform second-moment
estimate.  More precisely, if \(q/\sqrt m\to a\in[0,A]\), then

\[
 \boxed{
 \sum_f{T_{f,q}\over N_q}\lambda_{f,q}^2
 =e^{6a^2}+o_A(1).}
\tag{3.22}
\]

Here is the accounting.  On writing \(f=m/4+x\sqrt m\), division of
(2.7) by \(N_q/W=e^{-a^2+o(1)}\) and (2.6) give, uniformly for bounded
\(x\),

\[
 {T_{f,q}\over N_q}
 ={4\over\sqrt{2\pi m}}e^{-8(x+a/2)^2}(1+o_A(1)),
 \qquad
 \lambda_{f,q}=e^{8ax+3a^2+o_A(1)}.
\tag{3.23}
\]

Their product in (3.22) is a Gaussian Riemann sum proportional to

\[
 e^{-8(x+a/2)^2+16ax+6a^2}
 =e^{6a^2}e^{-8(x-a/2)^2}.
\tag{3.24}
\]

The tails are uniform in \(a\in[0,A]\).  One direct verification uses the
successive-term ratios

\[
 {V_{f+1}\over V_f}
 ={(m-2f)(m-2f-1)\over4(f+1)^2},
\quad
 {T_{f+1,q}\over T_{f,q}}
 ={(m-2f-q)(m-2f-q-1)\over4(f+1)(f+q+1)}.
\tag{3.25}
\]

For \(|x|\ge K\) but \(f\) in a fixed linear neighborhood of \(m/4\),
these ratios bound the summand \(V_f^2/T_{f,q}\) by
\(C_Ae^{-c(x-a/2)^2}/\sqrt m\).  Outside that neighborhood, Stirling's
strict entropy gap at the unique maximum \(f/m=1/4\) gives
\(e^{-c_Am}\); the factor caused by \(q=O_A(\sqrt m)\) is only
\(e^{O_A(\sqrt m\log m)}\).  Letting first \(m\to\infty\) and then
\(K\to\infty\) proves (3.22), uniformly on the compact interval
\([0,A]\).

Equations (3.21)--(3.22) imply

\[
 \mathbb E_M\sum_T
 \left(g_{M,q}(T)-{W\over N_q}\right)^2
 \le C_AW
\tag{3.26}
\]

uniformly for \(q\le H\).  Independence of the \(M_\ell\)'s divides the
right side by \(L\).  Cauchy--Schwarz on each target layer, followed by
summation over the \(2H\) signed depths, proves (3.18).

It remains only to justify the optional transversality assertion.  For two
independent uniform perfect matchings, conditional on the first, the chance
that the second contains some prescribed \(k\) of its edges is

\[
 {1\over(2m-1)(2m-3)\cdots(2m-(2k-1))}.
\]

The union bound over the \(\binom mk\) choices shows, for \(k=o(m)\),

\[
 \Pr(|M\cap M'|\ge k)\le (2e/k)^k.
\tag{3.27}
\]

Taking \(k=C\log L/\log\log L\) with a sufficiently large absolute
constant makes the union bound over all \(L^2\) pairs tend to zero; repeated
frames are then absent as well.  Markov's inequality gives probability at
least one half that the aggregate error is at most twice the right side of
(3.18).  Hence both properties hold simultaneously for some deterministic
sample. \(\square\)

Theorem 3.4 is exactly a pre-conflict result.  It says that frame diversity
need not be exponential to erase the aggregate fixed-profile Hall cut at the
fractional level.  But choosing one of these whole frames still incurs
\(\Omega_A(W)\) floor energy by Theorem 2.1.  The negative covariance must
therefore be created by mixing their packets inside one owner resolution,
which is the purpose of the next section.

If the certified compiler is installed only in pair strata with active
dimension at least \(4H+O(1)\), delete the remaining terms from
\(g_{M,q}\).  Those strata lie a linear distance from the central
\(f=m/4+O(\sqrt m)\) saddle, so their total contribution to (3.18), summed
over \(q\le H\), is \(e^{-\Omega(m)}W=o(W)\).  The same sparse aggregate
cancellation conclusion therefore holds with the exact floor-corrected
compiler range.

## 4. A genuine correlated law: Latin permutation of common blocks

We now give a deterministic existence theorem which can, in principle,
attain the required negative covariance.  Its hypotheses make explicit the
structure which whole-frame averaging lacks.

Partition the middle owners into \(b\) disjoint common blocks

\[
                         \Omega=\Omega_1\sqcup\cdots\sqcup\Omega_b.
\tag{4.1}
\]

For every block \(i\) and every label \(a\in[b]\), suppose
\(\mathcal R_{i,a}\) is an integral tiling of \(\Omega_i\) by valid
packets.  Different labels may use different coordinate frames.  Choosing
one label in every block is automatically owner-perfect; there are no owner
conflicts left to resolve.

For a signed depth \(q\), a target \(T\), and a block-option pair \((i,a)\),
let

\[
 d^{q,T}_{ia}\in\mathbb Z_{\ge0}
\tag{4.2}
\]

be the number of target occurrences contributed by \(\mathcal R_{i,a}\).
Define

\[
\begin{aligned}
 S_{q,T}&=\sum_{i,a}d^{q,T}_{ia},\\
 r_{i;q,T}&=\sum_a d^{q,T}_{ia},\\
 s_{a;q,T}&=\sum_i d^{q,T}_{ia}.
\end{aligned}
\tag{4.3}

Choose a permutation \(\pi\in S_b\) and use option \(\pi(i)\) in block
\(i\).  The resulting load is

\[
                         Z_{q,T}(\pi)=\sum_i d^{q,T}_{i,\pi(i)}.
\tag{4.4}
\]

### Theorem 4.1 (exact Latin covariance formula)

For a uniformly random \(\pi\in S_b\),

\[
 \mathbb E Z_{q,T}={S_{q,T}\over b},
\tag{4.5}
\]

and

\[
 \boxed{
 \mathbb E[Z_{q,T}(Z_{q,T}-1)]
 ={S_{q,T}^2-\sum_i r_{i;q,T}^2-\sum_a s_{a;q,T}^2
       +\sum_{i,a}(d^{q,T}_{ia})^2
       \over b(b-1)}.}
\tag{4.6}
\]

Suppose the one-point array is exactly balanced at every protected signed
depth:

\[
                         S_{q,T}=b\lambda_q
                         \quad\hbox{for every }q,T.
\tag{4.7}
\]

Put

\[
\begin{aligned}
 \Gamma_q:=\sum_{T\in\mathcal T_q}\Bigg[
 &{S_{q,T}^2-\sum_i r_{i;q,T}^2-\sum_a s_{a;q,T}^2
       +\sum_{i,a}(d^{q,T}_{ia})^2\over b(b-1)}\\
 &\hspace{18mm}-2c_q{S_{q,T}\over b}+c_q(c_q+1)
 \Bigg].
\end{aligned}
\tag{4.8}
\]

Then

\[
                         \boxed{\Gamma_q=\mathbb E Q_q\ge0.}
\tag{4.9}
\]

In particular, if simultaneously over the two signs and all \(q\le H\),

\[
                         \boxed{
 \sum_{\epsilon\in\{-,+\}}\sum_{q=1}^H\Gamma_{q,\epsilon}=o(W),}
\tag{4.10}
\]

then some deterministic permutation \(\pi\) gives

\[
 \sum_{\epsilon\in\{-,+\}}\sum_{q=1}^H Q_{q,\epsilon}(\pi)=o(W).
\tag{4.11}
\]

It is an owner-perfect multiframe packet resolution, and its total number
of missed protected targets is \(o(W)\).

#### Proof

For fixed \(i\), \(\pi(i)\) is uniform on \([b]\), proving (4.5).  For
\(i\ne j\), the ordered pair \((\pi(i),\pi(j))\) is uniform over ordered
distinct labels.  Hence

\[
 \mathbb E[Z(Z-1)]
 ={1\over b(b-1)}
   \sum_{i\ne j}\sum_{a\ne a'}d_{ia}d_{ja'}.
\tag{4.12}
\]

Inclusion--exclusion on the two equalities \(i=j\) and \(a=a'\) gives

\[
 \sum_{i\ne j}\sum_{a\ne a'}d_{ia}d_{ja'}
 =S^2-\sum_i r_i^2-\sum_a s_a^2+\sum_{i,a}d_{ia}^2,
\]

which proves (4.6).  Since

\[
 Q_q=\sum_T[Z_{q,T}(Z_{q,T}-1)-2c_qZ_{q,T}+c_q(c_q+1)],
\]

(4.5)--(4.8) prove (4.9).  Average the nonnegative total floor energy over
\(\pi\); (4.10) yields one permutation satisfying (4.11).  Each block
option tiles exactly its own fixed block, so this choice is owner-perfect.
Finally the floor-energy missing-target inequality gives
\(\#\{T:Z_{q,T}=0\}\le Q_q/2\), because here \(W>N_q\); summing proves the
last claim. \(\square\)

The two negative square terms in (4.6) are the exact covariance benefit of
sampling option labels without replacement.  Formula (4.10), not pairwise
owner codegree, is the quantitative condition which a transverse packet
design has to verify.

### Corollary 4.2 (cyclic orthogonal-array form)

Index blocks and labels by \(\mathbb Z_b\), and restrict to the \(b\)
cyclic Latin choices \(\pi_u(i)=i+u\).  Assume (4.7), and write

\[
 Z_{q,T}(u)=\sum_i d^{q,T}_{i,i+u},\qquad
 \widehat Z_{q,T}(k)={1\over b}\sum_{u\in\mathbb Z_b}
 Z_{q,T}(u)e^{-2\pi iku/b}.
\tag{4.13}
\]

Then

\[
 \boxed{
 {1\over b}\sum_uQ_q(Z(u))
 =\sum_T\sum_{k\ne0}|\widehat Z_{q,T}(k)|^2
   -N_q\alpha_q(1-\alpha_q).}
\tag{4.14}
\]

Thus a cyclic transverse design succeeds if and only if its nonconstant
diagonal Fourier mass is within \(o(W)\) of the unavoidable integer
baseline, simultaneously over all protected depths.

#### Proof

The zero Fourier coefficient is \(\lambda_q\) by (4.7).  Parseval gives

\[
 {1\over b}\sum_u|Z_{q,T}(u)-\lambda_q|^2
 =\sum_{k\ne0}|\widehat Z_{q,T}(k)|^2.
\]

Sum over \(T\) and apply Lemma 1.1 to the uniform random choice of \(u\).
\(\square\)

This corollary states the spectral issue exactly.  Cancelling the mean
profile controls only \(k=0\).  A whole-frame orbit leaves
\(\Omega_A(W)\) excess nonconstant mass by Theorem 2.1.  A successful
packet atlas must cancel that mass *inside each integral outcome* by
Latin-style block interleaving.

## 5. Precise proved boundary

The following points are now rigorous.

1. A random choice of one complete coordinate-frame resolution cannot have
   \(o(W)\) floor energy at any fixed Gaussian depth, no matter how its
   distribution is coupled across depths.
2. A sparse nonnegative average of complete coordinate-frame resolutions
   cannot produce bounded **pointwise** fractional loads there.  It needs at
   least the support size in (0.2).  Nevertheless \(H^2\omega_m\) internally
   symmetrized frame orbits suffice for aggregate \(L^1\) cancellation; rare
   aligned spikes explain why these statements are compatible.
3. Edge-disjoint or orthogonal one-factorizations remove only the linear
   full-pair harmonic.  They do not remove the aligned-target spike or the
   floor variance.
4. There is an exact deterministic correlated selection theorem, Theorem
   4.1, once common owner blocks with multiframe packet-tiling options are
   supplied.  Its hypothesis (4.10) is precisely the required negative
   target covariance, with no owner-conflict error hidden in it.

What is not proved is that the current recursive packet library admits the
common block/options array (4.1)--(4.3) with (4.7) and (4.10).  The next
constructive lemma must build such a common-block Latin packet atlas (or a
comparable chronological design).  Merely enlarging the catalogue of whole
frames cannot do so: polynomially many frame **orbits** remove the fractional
Gaussian profile cut, but whole-state selection retains linear floor energy.
