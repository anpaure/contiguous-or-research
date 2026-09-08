# Precharged common edges still admit a sub-half repair-root transversal

**Date:** 2026-08-06  
**Method:** forced-load precharging, independent roots on small simple
cycles, Chernoff, and greedy vertex-cover avoidance on large cycles; no
computation or search  
**Status:** unconditional graph theorem.  Polynomially many common-edge
two-cycles need not be removed if their forced endpoint-star loads are
uniformly below one sixth by a fixed linear margin.  The theorem does not
prove that the Hamilton-anchored PBBS completion has such a spread common
bank.

## 1. Coloured factor with forced two-cycles

Let

\[
 {\cal L}={ [2r-1]\choose r-1},\qquad
 {\cal U}={ [2r-1]\choose r},
\tag{1.1}
\]

and let `G` be their inclusion graph.  Let `K` be the coloured union of
two perfect matchings.  Its components consist of:

* a set `D` of common-edge two-cycles; and
* a set `C` of simple even incidence cycles of length at least six.

Assume

\[
                       |D|+|C|\le r^A                 
\tag{1.2}
\]

for a fixed `A`.  Every member `e=zy` of `D` has the forced root `zy`.
Put

\[
 a_D=\max_{x\in{\cal L}}|\{zy\in D:x\subset y\}|,
 \qquad
 b_D=\max_{U\in{\cal U}}|\{zy\in D:z\subset U\}|.
\tag{1.3}
\]

For one subsequently chosen incidence `z_Cy_C` on every simple component,
define the total endpoint exposures

\[
 \alpha=\max_x
  \left(|\{zy\in D:x\subset y\}|+
        |\{C:x\subset y_C\}|\right),
\tag{1.4}
\]

and define `beta` dually.

## 2. Precharged transversal theorem

### Theorem 2.1

Fix constants

\[
                   0<\varepsilon<1/24,
 \qquad
                   0\le\eta<1/6-3\varepsilon.
\tag{2.1}
\]

For all sufficiently large `r`, if

\[
                         a_D,b_D\le\eta r,             
\tag{2.2}
\]

then one may choose one incidence root on every simple component so that,
together with all forced roots in `D`,

\[
 \boxed{
       \alpha,\beta\le
       \left\lfloor(1/2-\varepsilon)r\right\rfloor.}
\tag{2.3}
\]

All selected incidences form a matching after the two coloured copies of
each common edge are coalesced into their one physical root.

#### Proof

Put

\[
 K_* =\left\lfloor(1/2-\varepsilon)r\right\rfloor,
 \qquad
 K_0 =\left\lfloor(1/2-2\varepsilon)r\right\rfloor.
\tag{2.4}
\]

Write `q=|D|+|C|`.  A simple component is **small** when its number
`ell_C` of vertices on either shore is at most `7rq`, and large otherwise.

Choose one incidence independently and uniformly on every small simple
cycle.  For a fixed lower row `x`, its random contribution has mean at
most `r/3`: every simple cycle has `ell_C>=3`, and `x` has exactly `r`
upper neighbours in the whole incidence graph.  Adding the forced load
gives

\[
                         \mu_x\le (1/3+\eta)r.
\tag{2.5}
\]

By (2.1),

\[
                  1/3+\eta<1/2-3\varepsilon
                              <1/2-2\varepsilon.
\tag{2.6}
\]

Hence Chernoff gives

\[
 \Pr[X_x+a_D(x)>K_0]\le e^{-c_{\varepsilon,\eta}r}.
\tag{2.7}
\]

The same estimate holds on the dual shore.  Only polynomially many rows
receive nonzero load: the small cycles contain at most `7rq^2` vertices
per shore and the forced bank is polynomial, while every selected endpoint
lies in `r` opposite-shore stars.  A polynomial union bound therefore
fixes all small-cycle roots so that both total loads are at most `K_0`.

Process the large simple cycles greedily.  Call a row saturated when its
current total load, including the forced and small-cycle roots, is `K_*`.
At every stage at most `q` roots have been installed.  The sum of all
upper-root loads over lower rows is at most `rq`, so the number of saturated
lower rows is less than `3q` for all sufficiently large `r`; the same is
true dually.  Fewer than `3rq` upper vertices and fewer than `3rq` lower
vertices are therefore forbidden by saturated rows.

If all edges of the next large cycle had a forbidden endpoint, those fewer
than `6rq` forbidden vertices would cover the cycle.  But an even cycle
with `ell_C>7rq` vertices on either shore has minimum vertex-cover size
`ell_C`, a contradiction.  Choose an incidence with neither endpoint
forbidden.  It raises no saturated row and preserves the cap `K_*`.
Induction over the large cycles proves (2.3).  \(\square\)

## 3. PBBS consequence

The common-edge obstruction is therefore quantitative rather than
absolute.  For a Hamilton-anchored polynomial-component PBBS completion it
is enough to establish

\[
 \boxed{
 \max_x|N(x)\cap Y_D|,
 \ \max_U|N(U)\cap Z_D|
       \le (1/6-\Omega(1))r,}
\tag{3.1}
\]

where `Z_D,Y_D` are the endpoints of its polynomial common-edge bank.
One then obtains the all-occurrence sub-half component-root matching without
removing those common edges.  This is strictly weaker than constructing
the second perfect matching inside `G-M_0`.

The missing PBBS graph statement is now a **spread-damage completion**:
choose the polynomial alternating repairs around the Hamilton halves so
that their common-edge endpoints obey (3.1).  The present theorem does not
construct that choice or the later root-to-code arms and literal
antecedent.
