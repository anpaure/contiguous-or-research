# Audit of the mesoscopic wreath-cover reduction

Date: 2026-07-25

## 1. Verdict

The proposed mesoscopic cyclic-interval covering statement is a valid
sufficient theorem for the asymptotic constant-one upper bound.  The
independent-random comparison is also correct: a width-scale random family
leaves \(\Theta(W\sqrt m)\) expected holes across a fixed Gaussian-width
central band.

Two scope qualifications are essential.

1. The covering statement below is sufficient, not known to be equivalent
   to constant one; structured cross-rank repair can ask for less than
   literal \(o(W)\) total holes.
2. The affine arithmetic-progression wreaths at prime order give only
   \((n-1)/2=\Theta(n)\) distinct wreaths, versus
   \(W/n\) required at leading scale.  They are an algebraic seed, not a
   positive-density part of the required factor.

## 2. A clean sufficient statement

Put

\[
 n=2m+1,\qquad W=\binom{n}{m}.
\]

Assume that \(H=o(m)\), and that a family \(\mathcal P\) of cyclic orders
has

\[
 |\mathcal P|=(1+o(1))\frac Wn,
\tag{2.1}
\]

while all but \(o(W)\) subsets in the ranks

\[
 m-H,m-H+1,\ldots,m+H+1
\tag{2.2}
\]

are cyclic intervals of orders in \(\mathcal P\).  If additionally

\[
 \sqrt m\,e^{-H^2/m}=o(1),
\tag{2.3}
\]

then

\[
 \nu(2m+1)\le(1+o(1))W.
\tag{2.4}
\]

Condition (2.3) holds, for example, for

\[
 H\ge\left(\frac1{\sqrt2}+\varepsilon\right)
       \sqrt{m\log m}.
\tag{2.5}
\]

The larger cutoff \(H\ge\sqrt{2m\log m}\) is therefore valid but not
sharp for literal tail repair.  A separately proved product-SCD tail word
can weaken the needed scale further to \(H=\sqrt m\,\omega(1)\).

### Proof

For a cyclic order \(\pi=(x_0,\ldots,x_{n-1})\), put

\[
 E_j=I_\pi(j,m-H).
\]

Emit

\[
 E_0,E_1,\ldots,E_{n-1},E_0,E_1,\ldots,E_{2H}.
\tag{2.6}
\]

The union of \(t\ge1\) consecutive entries beginning at \(E_j\) is

\[
 E_j\cup\cdots\cup E_{j+t-1}
   =I_\pi(j,m-H+t-1).
\tag{2.7}
\]

Thus (2.6), of length \(n+2H+1\), realizes every cyclic interval of
\(\pi\) in all ranks (2.2).  Concatenating these blocks costs

\[
 |\mathcal P|(n+2H+1)
   =(1+o(1))W,
\tag{2.8}
\]

because \(H=o(n)\).  Append the \(o(W)\) missing band masks literally.

For the two exterior tails, the binomial Chernoff estimate gives

\[
 2\sum_{r<m-H}\binom nr
 \le 2^{n+1}\exp\!\left(-\frac{2(H+O(1))^2}{n}\right).
\tag{2.9}
\]

Since \(W=\Theta(2^n/\sqrt n)\), the ratio of (2.9) to \(W\) is

\[
 O\!\left(\sqrt m\,e^{-H^2/m+o(1)}\right)=o(1)
\]

by (2.3).  Append only the nonempty exterior masks; the empty mask is
handled separately by the standard one-zero conversion if the literal
all-mask problem is desired.  This proves (2.4).  The trimmed one-bit lift
then transfers the same leading constant to even dimensions. \(\square\)

## 3. Exact independent-random barrier

Let \(N_q=\binom n{m-q}\), \(\lambda_q=W/N_q\), and take \(M\)
independent uniform cyclic orders with

\[
 Mn=CW
\tag{3.1}
\]

for fixed \(C>0\).  A fixed rank-\((m-q)\) set is a cyclic interval of one
order with probability exactly \(n/N_q\).  Hence its miss probability is

\[
 \left(1-\frac n{N_q}\right)^M
   =\exp(-C\lambda_q+o(1)).
\tag{3.2}
\]

Uniformly for \(q=O(\sqrt m)\),

\[
 \lambda_q=\exp(q^2/m+o(1)).
\tag{3.3}
\]

Therefore a signed depth \(q\) contributes

\[
 W\lambda_q^{-1}e^{-C\lambda_q+o(1)}
\tag{3.4}
\]

expected misses.  If \(H\ge c\sqrt m\) for fixed \(c>0\), the Riemann
sum over the two signed ranks gives

\[
 \mathbb E M_{\le H}
 =2W\sqrt m
   \int_0^{H/\sqrt m}
      e^{-u^2-Ce^{u^2}}\,du
   +o(W\sqrt m)
 =\Theta_C(W\sqrt m).
\tag{3.5}
\]

Thus width-scale independent sampling is short by an aggregate factor
\(\sqrt m\).  Increasing the number of orders by a fixed constant factor
changes only the constant in (3.5); a successful construction needs
strong simultaneous negative dependence or exact multi-depth design.

## 4. Arithmetic-progression seed

For prime \(n\) and \(a\ne0\pmod n\), the order

\[
 \pi_a=(0,a,2a,\ldots,(n-1)a)
\]

has as its length-\(r\) intervals exactly the translates of

\[
 \{0,a,\ldots,(r-1)a\}.
\]

Every depth is consequently rainbow within that wreath.  Slopes \(a\) and
\(-a\) give the same unoriented translation orbit, leaving at most
\((n-1)/2\) distinct AP wreaths.  Since

\[
 \frac{(n-1)/2}{W/n}\longrightarrow0
\]

exponentially, the unresolved algebraic question is not construction of
these seed rows but whether they can be completed by exponentially many
further correlated wreaths while retaining near-rainbow shadows.

## 5. Exact rotor/SCD orbit endpoint-splicing reformulation

`MATH_ATTACK_MESOSCOPIC_CYCLIC_INTERVAL_ORBIT_ENDPOINT_SPLICING_20260725.md`
gives a rigid, integral version of the rotor/SCD two-resolution argument.
If \(C\) is one admissible set of pointed cyclic-order states and \(p(C)\)
is the number of maximal rigid rotation runs in \(C\), then the complete
coordinate orbit has exact optimized monochromatic run count

\[
 R_{\rm orb}^{\min}=n!\,p(C).
\]

All open endpoints splice using the deterministic rotation of exact
pointed orders; arbitrary flexible rotor edges are unnecessary.  For the
quota-preserving version, the exact optimum is \(n!\) times the minimum
\(p(C)\) over one admissible integral coverage color.

A decorated full SCD gives \(|C|=W\) and zero band holes.  Thus the orbit
route produces a single exact-coverage color with \(o(W)\) run starts if
and only if one decorated SCD already has \(p(C)=o(W)\).  Orbit symmetry
does not prove this estimate.

The actual near-design threshold is sharper.  Since a rigid run has at
most \(n\) phases,

\[
 p(C)\ge |C|/n.
\]

Extending every run to a whole cyclic order shows that the statement of
Section 2 follows from

\[
 |C|=W+o(W),\qquad h_H(C)=o(W),\qquad
 p(C)=(1+o(1))W/n.
\]

Merely \(p(C)=o(W)\) gives a segmented near-design, not necessarily the
\((1+o(1))W/n\) full orders required in (2.1).  The exact segmented
compiler has length

\[
 |C|+(2H+1)p(C)+h_H(C),
\]

so its coefficient-safe threshold is \(Hp(C)=o(W)\).
