# Growing-uniformity degree and codegree data do not force even two disjoint edges

**Date:** 2026-08-06  
**Method:** projective-plane intersection with a regular decoration layer  
**Status:** unconditional obstruction.  There are simple regular
(K)-uniform hypergraphs with (K=\Theta(q)), exponentially large degree,
(Delta_2/D=\Theta(1/q)), and fractional matching number tending to
infinity, but integral matching number one.  Therefore the numerical data
available for cyclic star packets cannot by themselves imply the required
constant-density integral rounding.

## 1. Construction

Let (q) be a prime power and let

\[
                         b=q^2+q+1.
\]

Take a projective plane of order (q), with point set (P) and line set
(mathcal L).  Thus

\[
 |P|=|\mathcal L|=b,qquad |\ell|=q+1,qquad
 d_{\mathcal L}(p)=q+1,
\]

and every two projective lines meet.

Take a disjoint decoration set (U) of size (b).  Define a hypergraph
(mathcal H_q) on (P\mathbin{\dot\cup}U) by

\[
 E(\mathcal H_q)=
 \left\{\ell\mathbin{\dot\cup}F:
        \ell\in\mathcal L,
        F\in{U\choose q+1}\right\}.                                  \tag{1.1}
\]

This is a simple

\[
                         K=2(q+1)                                      \tag{1.2}
\]

uniform hypergraph with

\[
                         |E|=b{b\choose q+1}.                           \tag{1.3}
\]

## 2. Exact regularity

### Theorem 2.1

Every vertex of (mathcal H_q) has degree

\[
 \boxed{D=(q+1){b\choose q+1}.}                                       \tag{2.1}
\]

#### Proof

A projective point lies on (q+1) lines, and for each such line the
decoration (F) is arbitrary.  Its degree is therefore the right side of
(2.1).

A decoration vertex belongs to

\[
 b{b-1\choose q}
 =(q+1){b\choose q+1}
\]

edges.  Hence the two vertex classes have the same degree.  \(\square\)

The degree is very large:

\[
                         \log D=\Theta(q\log q).                        \tag{2.2}
\]

Thus the obstruction is not caused by a low-degree host.

## 3. Exact pair codegrees

### Theorem 3.1

The three possible pair codegrees, divided by (D), are

\[
\begin{array}{c|c|c}
\text{pair type}&\deg(x,y)&\deg(x,y)/D\\ \hline
P,P&{b\choose q+1}&1/(q+1)\\[1mm]
P,U&(q+1){b-1\choose q}&(q+1)/b\\[1mm]
U,U&b{b-2\choose q-1}&1/(q+1).
\end{array}                                                            \tag{3.1}
\]

Consequently

\[
 \boxed{
 {\Delta_2(\mathcal H_q)\over D}={q+1\over q^2+q+1}
 =\Theta(1/q)=\Theta(1/K).}                                           \tag{3.2}
\]

#### Proof

Two projective points determine one line.  A projective point and a
decoration vertex allow (q+1) choices of the line and
({b-1\choose q}) choices of the rest of the decoration.  Two decoration
vertices allow any of the (b) lines and ({b-2\choose q-1}) choices of
the rest.  Dividing by (2.1), and using
(b-1=q(q+1)), gives (3.1).  The mixed pair is the maximum.  \(\square\)

## 4. Fractional optimum versus integral optimum

### Theorem 4.1

The fractional matching number is

\[
 \boxed{
 \nu^*(\mathcal H_q)={b\over q+1}=q+{1\over q+1},}                    \tag{4.1}
\]

whereas

\[
 \boxed{\nu(\mathcal H_q)=1.}                                        \tag{4.2}
\]

#### Proof

Give every edge weight (1/D).  Regularity makes the load of every vertex
exactly one, so this is a fractional matching of total weight

\[
 {|E|\over D}={b\over q+1}.
\]

Conversely, giving every vertex dual weight (1/K) is a fractional vertex
cover of total weight

\[
 {|P|+|U|\over K}={2b\over2(q+1)}={b\over q+1}.
\]

LP duality proves (4.1).

Any two hyperedges contain two projective lines.  Those lines meet in a
projective point, so the hyperedges intersect.  Thus no matching has two
edges, proving (4.2).  \(\square\)

## 5. Consequence for the cyclic-star rounding gate

The family (mathcal H_q) simultaneously has

* growing uniformity (K=\Theta(q));
* exact regularity;
* exponentially large degree;
* normalized pair codegree (Theta(1/q)); and
* fractional matching number tending to infinity.

Nevertheless its integral matching number is one.  In particular, for any
fixed margin (A), including (A=3000), one has

\[
                         \nu^*(\mathcal H_q)>A\nu(\mathcal H_q)
\]

for all sufficiently large (q).

Hence there is no theorem of the following parameter-only form:

> regular (K=\Theta(n)), exponentially high degree,
> (Delta_2/D=O(1/n)), and a fixed fractional surplus imply a
> positive-density integral matching.

This does **not** obstruct the cyclic-star packet hypergraph itself.  That
host has additional structure absent from (mathcal H_q): modular-sum
bottom separation, balanced-exchange collision laws, and cyclic-interval
fibres.  Indeed, the separate depth-two Dirac construction already uses
that structure to beat the generic obstruction.

The exact mathematical conclusion is narrower but decisive for proof
design:

\[
 \boxed{
 \text{Any successful all-depth star rounding must exploit the
 balanced-exchange/cyclic-order geometry.}}
\]

A black-box nibble whose hypotheses see only (K,D,Delta_2), regularity,
and fractional margin cannot prove the desired star factor.

