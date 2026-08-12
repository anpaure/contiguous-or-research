# Rank-two recoupling by edge colour: exact threshold and the nonregularity gate

**Date:** 2026-08-07  
**Method:** exact incidence accounting in the frame--owner recoupling
hypergraph  
**Status:** proof-safe reduction and obstruction audit. A constant-factor
edge colouring would close rank-\(s\) recoupling, but no presently justified
regularization or growing-rank chromatic-index theorem supplies it.

## 1. Recoupling parameters

Let

\[
p=d+1,\qquad \ell=3p,
\qquad R=3^{p-1},
\tag{1.1}
\]

and let \(W={n\choose m}\). From the moment-core/Kirkman theorem, after
harmless thinning one may take a target-disjoint frame family
\(\mathscr F\) with

\[
3p|\mathscr F|=(\rho+o(1))W,
\qquad 0<\rho\le\rho_0:=\frac{e^{-\pi}}{32}.
\tag{1.2}
\]

Every frame has \(R\) distinct translated queue rings. The exact
recoupling hypergraph \(\mathcal G\) has vertex set

\[
{[n]\choose m}\mathbin{\dot\cup}\mathscr F
\tag{1.3}
\]

and one \((3p+1)\)-edge \(\{F\}\cup C\) for every translated ring \(C\)
in frame \(F\). Hence

\[
|E(\mathcal G)|=R|\mathscr F|
=\left(\frac{\rho}{3p}+o(1)\right)RW.
\tag{1.4}
\]

## 2. Exact edge-colour threshold

### Proposition 2.1 (averaging threshold)

If

\[
\chi'(\mathcal G)\le(A+o(1))R,
\tag{2.1}
\]

then \(\mathcal G\) has a matching of size at least

\[
\left(\frac{\rho}{3pA}-o(1)\right)W.
\tag{2.2}

Consequently the rank-\(s\) recoupling target

\[
|M|\ge(\theta+o(1))\frac{W}{3p}
\tag{2.3}

follows whenever

\[
\boxed{A<\frac\rho\theta.}
\tag{2.4}

At the full proved source density \(\rho_0=e^{-\pi}/32\),

\[
\boxed{
\frac{\rho_0}{\theta}
=\frac{e^{-\pi}}
{128\sum_{a\ge1}e^{-4\pi a^2}}
>96.}
\tag{2.5}
\]

Thus even a \(96R\)-colouring would suffice; a near-optimal
\((1+o(1))R\)-colouring would have enormous slack.

#### Proof

Every colour class is a matching. The largest colour class has size at
least \(|E(\mathcal G)|/\chi'(\mathcal G)\). Substitute (1.4) and compare
with (2.3). \(\square\)

## 3. Exact degrees and local codegrees

For an owner \(X\), put

\[
d_{\rm fib}(X)=
|\{F\in\mathscr F:X\text{ belongs to the full owner fibre of }F\}|.
\tag{3.1}
\]

Then

\[
d_{\mathcal G}(F)=R,
\qquad
d_{\mathcal G}(X)=p\,d_{\rm fib}(X).
\tag{3.2}
\]

The average owner degree is

\[
\frac1W\sum_Xd_{\mathcal G}(X)
=\frac{3p|E(\mathcal G)|}{W}
=(\rho+o(1))R.
\tag{3.3}
\]

Thus the frame shore has degree \(R\), while the owner shore has average
degree only \(\rho R\). The missing regularization row is the pointwise
estimate

\[
\boxed{
p\,d_{\rm fib}(X)\le(1+o(1))R
\quad\text{for every owner }X,}
\tag{3.4}

or a weighted/quarantined substitute sufficient for edge colouring.
The stronger near-average form would be

\[
p\,d_{\rm fib}(X)\le(\rho+o(1))R
\quad\text{for every nonquarantined owner }X.
\tag{3.4a}
\]

The exact mixed codegrees are

\[
d_{\mathcal G}(F,F')=0\quad(F\ne F'),
\tag{3.5}
\]

and

\[
d_{\mathcal G}(F,X)=
\begin{cases}
p,&X\text{ belongs to the fibre of }F,\\
0,&\text{otherwise}.
\end{cases}
\tag{3.6}
\]

For owners \(X,Y\), let \(r_F(X,Y)\) be the number of translated rings in
frame \(F\) containing both. Then

\[
d_{\mathcal G}(X,Y)
=\sum_{F:X,Y\in G_F}r_F(X,Y),
\qquad 0\le r_F(X,Y)\le p.
\tag{3.7}
\]

If \(X,Y\) differ in one phase coordinate inside a common frame, then

\[
r_F(X,Y)=1.
\tag{3.8}
\]

Indeed the distance-one graph of the ternary queue states is exactly one
\(3p\)-cycle in each translate, and double counting shows every oriented
Hamming-distance-one pair lies in exactly one translated cycle.

Equations (3.4) and a uniform bound on the sum in (3.7) are not consequences
of the moment-core distance-three theorem: that theorem separates the
rank-\(s\) upper shadows, whereas one rank-\(m\) owner may contain many of
the selected cores.

## 4. Why standard colour bounds do not close the row

Even if the degree cap (3.4) is granted, greedy colouring of the line graph
gives only

\[
\chi'(\mathcal G)\le(3p+1)R,
\tag{4.1}
\]

If the stronger near-average form (3.4a) is granted, the same calculation
improves only to

\[
\chi'(\mathcal G)\le
\bigl(1+3p\rho+o(p)\bigr)R.
\tag{4.2}
\]

Both coefficients exceed the fixed threshold (2.5) for sufficiently large
\(p\).

The Pippenger--Spencer and Kahn near-\(R\) chromatic-index theorems have
constants depending on the edge rank. Their fixed-rank conclusions cannot
be applied diagonally to rank \(3p+1\to\infty\). The exact moment/Kirkman
construction presently supplies neither a uniform-in-\(p\) version of
those theorems nor the maximum-degree and owner--owner codegree bounds that
such an application would first require.

## 5. Exact remaining edge-colour lemma

The edge-colour route is reduced to:

> **Uniform recoupling colour lemma.** Choose or symmetrize the
> moment-core/Kirkman target-clean frame family so that the owner degrees
> and the overlap sums (3.7) are uniformly controlled, and prove
> \[
> \chi'(\mathcal G)\le96R.
> \]

This lemma would prove the rank-\(s\) owner--source recoupling immediately
by Proposition 2.1. It is not presently proved.

The newer core--bank gauge decoration theorem offers a different route:
keep the already owner-disjoint one-third queue packing and choose among
\(2^{3p}\) exact source decorations per ring. That route avoids the
nonregular frame-owner incidence (3.1), and is therefore currently more
promising than forcing (3.4) for the moment/Kirkman family.
