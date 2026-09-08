# Exact remaining synchronization theorem (brief model prompt)

## Definitions

Let

\[
n=2m+1,\qquad W=\binom nm,\qquad N_q=\binom n{m-q},
\qquad c_q=\left\lfloor\frac W{N_q}\right\rfloor.
\]

Choose any integer depth

\[
H=\lceil\sqrt m\,\omega(m)\rceil,
\qquad \omega(m)\to\infty,
\qquad H=o(m).
\]

An **exact middle wreath factor** is a family \(\mathcal F\) of \(W/n\)
cyclic orders whose length-\(m\) cyclic intervals partition
\(\binom{[n]}m\).  Such factors are already known to exist.  For the unique
pointed occurrence \(X=I_\pi(j,m)\), put

\[
L_q^{\mathcal F}(X)=I_\pi(j,m-q).
\]

A **balanced nested resolution** is a family of maps

\[
P_q:\binom{[n]}m\to\binom{[n]}{m-q}\qquad(0\le q\le H)
\]

such that \(P_0(X)=X\), each \(P_{q+1}(X)\) is obtained from \(P_q(X)\)
by deleting one point, and every depth-\(q\) fiber has size either
\(c_q\) or \(c_q+1\).  Such resolutions are already known to exist by an
integral lower-bounded-flow argument.

Define the labelled synchronization error

\[
e_q(\mathcal F,P)
=\#\{X:L_q^{\mathcal F}(X)\ne P_q(X)\}.
\]

## The one missing theorem

Prove that there are exact middle wreath factors \(\mathcal F_m\) and
balanced nested resolutions \(P^{(m)}\) for which

\[
\boxed{
\sum_{q=1}^{H}
\frac{e_q(\mathcal F_m,P^{(m)})}{c_q}=o(W).
}
\tag{SYNC}
\]

The factor and resolution must be chosen jointly.  Separate factors at
different depths, fractional mixtures, or independently balanced rank
histograms do not prove (SYNC).

## Fixed-window overload form and labelled sufficient form

For fixed `A>0`, put

\[
K_A=\lceil A\sqrt m\rceil,
\qquad
\beta_m(A)=\min_F\frac1W
\sum_{q=1}^{K_A}\frac{O_q(F)}{c_q}.
\]

The moving-window **overload theorem (MWB)** is equivalent, by
diagonalization, to

\[
\boxed{\beta_m(A)\to0\quad\text{for every fixed }A.}
\tag{GW}
\]

Indeed, on every fixed window

\[
\log\frac W{N_q}=\frac{q^2}{m}+O_A(m^{-1/2}),
\]

so `1<=c_q<=C_A`: the quota capacities are bounded independently of `m`.
The corresponding exact labelled theorem is the stronger sufficient
statement:

\[
\boxed{
\text{For every fixed }A,
\text{ find one }(F_m,P_m)\text{ with }
\sum_{q\le K_A}\frac{e_q(F_m,P_m)}{c_q}=o(W).
}
\tag{CA_A}
\]

Proving `(CA_A)` for every fixed `A` proves labelled (SYNC), and hence MWB,
by choosing a slowly growing diagonal `A=A(m)`.  This removes the need to
guess the growth rate of `omega(m)` inside the local theorem.

Do **not** assert the converse.  Small overload controls unlabelled rank
histograms; it does not by itself produce a nearby common nested owner
coupling.  Thus `(GW)` is exactly equivalent to MWB, while `(CA_A)` is a
strictly stronger sufficient lane unless an additional stability theorem
from balanced histograms to one nested labelled flow is proved.

Balanced quota vectors at adjacent ranks cannot be selected independently:
already for `n=9`, one can give the eight pairs containing a fixed point
quota four while giving every parent triple containing that point quota one,
creating demand 32 against supply 28.  The common nested resolution must be
chosen jointly across all depths, as in the lower-bounded-flow theorem.

## Why this finishes the asymptotic OR theorem

Let \(\mu_q(S)\) be the number of pointed wreath intervals equal to \(S\),
and let \(O_q\) be its minimum overload above a floor/ceiling-balanced quota
vector.  Histogram coupling gives

\[
O_q(\mathcal F_m)\le e_q(\mathcal F_m,P^{(m)}),
\qquad
M_q(\mathcal F_m)\le \frac{O_q(\mathcal F_m)}{c_q}.
\]

Thus (SYNC) implies total central-band defect \(o(W)\).  The literal wreath
word costs

\[
W+O(HW/m)+2\sum_{q\le H}M_q=W+o(W),
\]

and the audited symmetric-chain product word covers both outer tails in
\(o(W)\) entries because \(H/\sqrt m\to\infty\).  Hence

\[
\nu(2m+1)\le W+o(W).
\]

The standard trimmed one-bit lift then gives

\[
\nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}
\]

for both parities.

## Equivalent owner-tail target

If

\[
a(X)=\max\{a\le H:L_q^{\mathcal F}(X)=P_q(X)
\text{ for every }q\le a\},
\]

then it is enough to prove

\[
\boxed{
\sum_X\Psi_{m,H}(a(X))=o(W),
\qquad
\Psi_{m,H}(a)=\sum_{q=a+1}^{H}\frac1{c_q}.
}
\]

A simpler sufficient form is

\[
\sum_X(H-a(X))e^{-a(X)^2/m}=o(W).
\]

Do **not** replace the finite tail by the untruncated condition
\(\sum_X e^{-a(X)^2/m}/(1+a(X)/\sqrt m)=o(W/\sqrt m)\): at the intended
depth it fails even when \(a(X)=H\) for every owner.

## What a valid proof must supply

1. One integral exact wreath factor, not a fractional factor or partial
   packing.
2. One common integral nested resolution through all depths \(q\le H\).
3. A support-feasible cyclic switching, absorber, or reconfiguration
   argument proving the weighted labelled mismatch bound.
4. Quantitative estimates uniform as \(m\to\infty\).

Everything after (SYNC)—the overload charge, literal factorization, seam
accounting, outer-tail word, and parity lift—is already proved.

## Equivalent absorption route

One may instead take

\[
Q=\left\lceil\sqrt{\tfrac12m\log m}\right\rceil.
\]

The weighted contribution of every depth `q>=Q` is automatic for an
arbitrary exact factor.  More precisely, with

\[
g(q)=\frac{q(q+1)}{m+q+1},
\]

one has

\[
\sum_{q=Q}^{H}\frac{O_q(F)}{c_q}
\le
O\!\left(
W\frac mQe^{-g(Q)}
\right),
\]

because

\[
g(q+1)-g(q)\ge\frac{q+1}{2(m+1)}.
\]

Thus the displayed exact `Q` gives normalized cost
`O(1/sqrt(log m))`.  The sharp sufficient asymptotic condition is

\[
\frac{Q^2}{m}-\frac12\log m+\frac12\log\log m\to+\infty.
\]

Do not replace it by the ambiguous shorthand
`Q=(1/sqrt(2)+o(1))sqrt(m log m)`: an unrestricted `o(1)` may approach from
below too quickly.

For `q<Q`, choose balanced quota vectors `b_q` and
construct a quota-safe wreath submatching `M`, extendible to the same exact
factor `F`.  Put

\[
s_q(S)=b_q(S)-\mu_q^M(S),
\qquad C=F\setminus M.
\]

It is enough to prove the weighted completion-spill bound

\[
\boxed{
\sum_{q<Q}\frac1{c_q}
\sum_S\bigl(\mu_q^C(S)-s_q(S)\bigr)_+=o(W).
}
\tag{ABS}
\]

A simpler, stronger target is

\[
|C|=o\!\left(\frac{W}{n\sqrt m}\right),
\]

because `sum_(q<Q) 1/c_q=Theta(sqrt(m))`.  Ordinary almost-perfect
conflict-free matching is insufficient: the exceptionally small leave must
be extendible by actual wreaths into the same exact factor.
