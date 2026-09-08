# A frozen PBBS reset occurrence has a fibre-one host

**Date:** 2026-08-07  
**Status:** unconditional quantifier correction.  The complete ideal
successor family is a prospective family before the owner occurrence is
chosen.  It is not a binomial menu at one frozen occurrence.

## 1. Setup

Use the odd PBBS parameters

\[
 n=2m+1,\qquad t=m-d.
\]

An upper flag consists of

\[
 M\in\binom{[n]}{t-2},\qquad U=M\cup\{u\}
   \in\binom{[n]}{t-1}.
\]

At an immediate-successor occurrence the forced central equations are

\[
 B\in\binom{[n]\setminus U}{d+1},\qquad
 Y=M\cup B,\qquad T=U\cup B=Y\cup\{u\},
\tag{1.1}
\]

where \(B\) is the fresh exterior of the successor source letter, \(Y\)
is the depth-\(d\) coatom, and \(T\) is the rank-\(m\) owner.  In forward
suffix notation

\[
 Z_{e,j}=A_{e-j+1}\cup\cdots\cup A_e,
\]

the predecessor state and successor equations are

\[
 M=Z_{q-1,d-1},\qquad U=Z_{q-1,d},
\]

\[
 Y=Z_{q,d}=M\cup A_q,\qquad
 \widehat T_q=Z_{q,d+1}=U\cup A_q.
\tag{1.2}
\]

Thus the actual successor letter may be

\[
 A_q=B\cup K,\qquad K\subseteq M,
\tag{1.3}
\]

without changing the central edge.

For a frozen literal history, let \(\widehat T_q\) denote the owner
occurrence ending at a candidate successor position \(q\), and let \(C_q\)
be the maximal safe source envelope there.  Every legal replacement letter
at \(q\) is a subset of \(C_q\), and \(C_q\subseteq\widehat T_q\).

## 2. Fibre-one theorem

### Theorem 2.1

Fix the literal history, the occurrence \(q\), and the flag \((M,u)\).
There is at most one fresh bank \(B\) satisfying (1.1) at \(q\).  It is

\[
 \boxed{B=\widehat T_q\setminus U.}
\tag{2.1}
\]

It is legal exactly when

\[
 (Z_{q-1,d-1},Z_{q-1,d})=(M,U),
\tag{2.2}
\]

\[
 U\subseteq\widehat T_q,\qquad
 |\widehat T_q\setminus U|=d+1,\qquad
 \widehat T_q\setminus U\subseteq C_q,
\tag{2.3}
\]

and there exists a filler \(K\subseteq M\cap C_q\) such that
\(A_q=B\cup K\) passes the required phase, lag, residence, mandatory-core,
and positive-hit tests.  When these conditions hold, the coatom is also
forced:

\[
 \boxed{Y=\widehat T_q\setminus\{u\}.}
\tag{2.4}
\]

#### Proof

Equation \(\widehat T_q=U\cup B\), with \(B\cap U=\varnothing\), gives
(2.1) uniquely.  The predecessor state is necessary and sufficient for
the first two equalities in (1.2); (2.3) gives the prescribed exterior and
its envelope legality.  The remaining freedom in the actual source letter
is exactly the filler \(K\subseteq M\), as in (1.3).  Finally

\[
 Y=M\cup B=(U\setminus\{u\})\cup(\widehat T_q\setminus U)
   =\widehat T_q\setminus\{u\},
\]

which proves (2.4).  The remaining typed tests do not create another
choice.  \(\square\)

### Corollary 2.2 (the safe envelope is a test, not a host menu)

For a frozen owner chronology, the occurrence-labelled compatibility graph
has one right vertex per occurrence, not
\(\binom{|C_q\setminus U|}{d+1}\) independently selectable central edges.
The latter count is an overcount unless changing \(B\) is also allowed to
change \(T_q\), in which case the owner chronology and hence \(C_q\) are no
longer frozen.

## 3. Exact separation of the two quantifiers

Before an owner occurrence is chosen, the complete ideal family for one
flag has

\[
 D=\binom{m+d+2}{d+1}
\]

possible pairs \((Y,T)\), and the ideal rainbow-host theorem may select
among them.  After
\((q,Z_{q-1,d-1},Z_{q-1,d},\widehat T_q,C_q)\) is fixed, Theorem 2.1
contracts that family to zero or one central edge.

Therefore the implication

\[
 \text{large ideal host family}
 \Longrightarrow
 \text{large typed family at a fixed reset occurrence}
\]

is false.  The correct all-dimensional object must use one of the following
two formulations.

1. **Frozen-history formulation.**  First construct the complete literal
   history.  Then match every upper flag to a distinct occurrence satisfying
   the fibre-one tests (2.2)--(2.3) and the separate lag test.
2. **Joint prospective formulation.**  Put the flag, owner occurrence,
   coatom, fresh bank, lag occurrence, and all phase/history data in one
   hyperedge, and select the owner factor and reset hosts simultaneously.

The second formulation retains the large ideal family, but only as part of
the joint factor hypergraph.  It cannot be projected to a fixed envelope
first.

## 4. Consequence for the adaptive-phase programme

The following statements remain valid:

* adaptive SCD rephasing closes the scalar endpoint/reset ledger;
* the complete Boolean universe has enough disjoint ideal central hosts;
* upper, successor, and lag positions fit abstractly.

The surviving theorem is now sharper:

> Construct one literal owner/history factor in which the fibre-one
> occurrence graph, augmented by the lag and phase types, has a matching
> saturating the rephased upper flags.

Pointwise binomial degree at a frozen occurrence is not an available route.
This note proves neither that occurrence matching nor
\(\nu(k)\le B(k)+O(1)\).
