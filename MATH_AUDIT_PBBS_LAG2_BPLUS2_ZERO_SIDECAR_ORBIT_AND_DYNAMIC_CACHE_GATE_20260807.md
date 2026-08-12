# The lag-two \(B+2\) hinge: zero-sidecar orbit and the dynamic-cache gate

**Date:** 2026-08-07  
**Status:** unconditional local/orbit audit and exact overlap reduction.  The
packet removes the local q1 sidecar.  It does not by itself prove a global
\(B+2\) word: overlapping copies are exactly a constrained sliding-union
cache problem.

## 1. Literal packet

Put

\[
 n=2m+1,\qquad L=d+2,\qquad a=m-d-2.
\tag{1.1}
\]

Choose pairwise disjoint data

\[
 M,\ C,\ \{x,u,y,v\},
 \qquad |M|=a,\quad |C|=d,
\tag{1.2}
\]

and nonempty source letters

\[
 K_1,\ldots,K_{d-1}\subseteq M,
 \qquad \bigcup_{i=1}^{d-1}K_i=M.
\tag{1.3}
\]

On positions \(0,\ldots,L+1\), use

\[
 x,\ u,\ K_1,\ldots,K_{d-1},\ C,\ y,\ v.
\tag{1.4}
\]

Write \(R=M\dot\cup C\), so \(|R|=m-2\).  The three consecutive
length-\(L\) owner windows are

\[
 T_-=R+u+x,\qquad T_0=R+u+y,\qquad T_+=R+y+v.
\tag{1.5}
\]

They form a simple rank-\(m\) Johnson path.  Both lower colours are native
length-\((L-1)\) source cells:

\[
 I_-=T_-\cap T_0=R+u,
 \qquad
 I_+=T_0\cap T_+=R+y.
\tag{1.6}
\]

Both upper colours are native length-\((L+1)\) source cells:

\[
 J_-=T_-\cup T_0=R+u+x+y,
 \qquad
 J_+=T_0\cup T_+=R+u+y+v.
\tag{1.7}
\]

At the endpoint immediately before \(C\), the final \(d-1\) and \(d\)
source cells are

\[
 M,\qquad U=M+u,
\tag{1.8}
\]

and after appending \(y\), the forced successor coatom is

\[
 Y=R+y.
\tag{1.9}
\]

Hence (1.4) realizes the full local promotion history and both immediate
palettes with no external q1 or immediate-upper ticket.  This is the exact
gain over the width-\((d+1)\) three-owner hinge.

## 2. Prospective orbit degrees

Put

\[
 c_0=\binom{m-2}{d},\qquad N=m+d+2.
\tag{2.1}
\]

Suppressing the internal cover (1.3), the number of labelled set-valued
packets is

\[
 \boxed{
 E=\binom n{m-2}c_0(m+3)_4
   =\frac{n!}{a!d!(m-1)!}.}
\tag{2.2}
\]

For a fixed flag \((M,U=M+u)\), the prospective completion degree is

\[
 \boxed{D_F=\binom Nd(m+2)_3.}
\tag{2.3}
\]

For one fixed resource in one specified slot,

\[
 \boxed{D_O=c_0(m)_2(m+1)_2}
\tag{2.4}
\]

for each owner,

\[
 \boxed{D_L=c_0(m-1)(m+2)_3}
\tag{2.5}
\]

for each lower colour, and

\[
 \boxed{D_U=D_O}
\tag{2.6}
\]

for each upper colour.  These are exactly the already-audited symmetric
three-owner orbit degrees: the width shift changes literal availability,
not the named set-valued orbit.

The largest typed pair-codegree between two nonflag resources is

\[
 \boxed{\lambda_{\max}=c_0(m-1)(m+1)_2,}
\tag{2.7}
\]

attained by a nested lower--owner pair.  Thus

\[
 \frac{\lambda_{\max}}{D_L}=\frac1{m+2},
 \qquad
 \frac{\lambda_{\max}}{D_O}=\frac1m.
\tag{2.8}
\]

If a full ordered chain \((K_i)\) is part of the task, no multiplier is
present.  If only \(M\) is fixed and arbitrary nonempty covers are counted,
all degrees acquire the common factor

\[
 \kappa_{\rm cov}(a,d-1)
 =\sum_{j=0}^{d-1}(-1)^j\binom{d-1}{j}
       \bigl(2^{d-1-j}-1\bigr)^a.
\tag{2.9}
\]

If the \(K_i\) are required to be the disjoint nonempty differences of a
strict chain, the common factor is

\[
 \kappa_{\rm part}(a,d-1)=(d-1)!\,S(a,d-1).
\tag{2.10}
\]

Because these factors are common, they do not improve any normalized
resource load or matching estimate.

## 3. Exact support conflicts

Let a packet start at source position \(s\).  It forces singleton letters
at

\[
 s,\quad s+1,\quad s+L,\quad s+L+1,
\tag{3.1}
\]

and a rank-\(d\) letter at

\[
 s+L-1.
\tag{3.2}
\]

For \(d\ge2\), two packet starts cannot differ by

\[
 \boxed{1,\ 2,\ L-2,\ L-1.}
\tag{3.3}
\]

Indeed, at differences \(1,2\), the later rank-\(d\) cell lands on the
earlier \(y\)- or \(v\)-singleton.  At differences \(L-2,L-1\), the
earlier rank-\(d\) cell lands on the later \(u\)- or \(x\)-singleton.

In particular, distinct clean hinges cannot share any of their three owner
occurrences: their starts differ by at least three.  Therefore a one-copy
rank-\(m\) chronology has the exact capacity bound

\[
 \boxed{H\le \left\lfloor\frac{W}{3}\right\rfloor}
\tag{3.4}
\]

for clean lag-two hinges whose \(3H\) owner **target values** are globally
distinct among the exactly \(W\) rank-\(m\) targets.  A \(W+1\) count
would refer to physical closure occurrences and is not a target-capacity
bound.

This is still a positive-density capacity.  Moreover, (3.3) alone does
not force \(O(W/L)\) disjoint supports.  The graph on source starts with
forbidden differences (3.3) has maximum degree at most eight, so it has
an independent set of at least one ninth of its vertices.  Thus the
position-size constraints alone permit \(\Omega(W)\) overlapping
supports.

The latter assertion is only a support statement.  It does not assign
consistent literal set values.

## 4. Exact dynamic-cache formulation

Let \((A_t)\) be one ambient source word and let \(S\) be the selected set
of packet starts.  For every \(s\in S\), define

\[
 M_s=\bigcup_{t=s+2}^{s+L-2}A_t,
 \qquad
 C_s=A_{s+L-1}.
\tag{4.1}
\]

The overlapping supports have the local set-valued clean-hinge identities
if and only if, for every \(s\in S\),

1. \(A_s,A_{s+1},A_{s+L},A_{s+L+1}\) are four distinct singletons;
2. \(|M_s|=a\) and \(|C_s|=d\);
3. \(M_s,C_s\), and the four singleton labels are pairwise disjoint; and
4. every internal source letter is nonempty.

For a complete global PBBS realization one must additionally require that
\((M_s,M_s+A_{s+1})\) is the prescribed flag task, that the individual
internal letters realize any prescribed full chain (not only its union),
and that flag/forced-coatom targets, owner/lower/upper targets, residence,
the common cap, and the terminal compiler all have their required global
multiplicities and incidences.

Condition (4.1) is a sliding-union cache: one source letter may be a
\(K\)-piece for several packets, a \(C\)-bank for one packet, and a
singleton endpoint for another only when those literal prescriptions
agree.  This is precisely the extra information absent from the symmetric
orbit table.

The resource-disjoint hypergraph model is therefore proof-safe but too
strong.  Conversely, a start set satisfying (3.3) is necessary but not
sufficient.  A positive-density theorem requires a trajectory through
the cache states (4.1), together with the one-copy middle/upper palettes,
residence, and the lower compiler.

## 5. Scope verdict

The clean lag-two packet closes a real local gate:

\[
 \boxed{\text{promotion flag + three owners + both q1 colours + both
 upper colours are all literal in one history.}}
\]

Its prospective orbit is large and has normalized codegree
\(O(m^{-1})\).  The support geometry permits a positive-density start
set, but every packet consumes three distinct owner occurrences and the
literal overlaps are governed by the dynamic cache (4.1).

Thus the remaining theorem is not another local ticket calculation.  It
is a global cache/factor theorem: construct one source trajectory that
visits the required promotion tasks while making the middle owners and
upper colours one-copy and preserving the lower compiler.
