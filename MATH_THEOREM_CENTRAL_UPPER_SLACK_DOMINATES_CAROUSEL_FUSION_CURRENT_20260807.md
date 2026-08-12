# Central binomial slack dominates the complete carousel fusion current

**Date:** 2026-08-07  
**Status:** unconditional scalar theorem.  It proves that enough duplicate
upper occurrences exist at every relevant rank; it does not place the named
duplicates on prescribed seams.

## 1. Upper occurrence slack

Put

\[
 R=\left\lceil\frac k2\right\rceil,
 \qquad W={k\choose R},
 \qquad q=d+1,
 \qquad M=k-R+q.
\tag{1.1}
\]

A cyclic owner chronology has (W) endpoint positions at every fixed upper
offset (s\ge1), whereas the number of named rank-(R+s) targets is

\[
 U_s={k\choose R+s}.
\]

Define its unavoidable scalar duplicate bank

\[
 S_s=W-U_s.
\tag{1.2}
\]

### Theorem 1.1 (central upper-slack inequality)

If (k=2m), then for (1\le s\le m),

\[
 \boxed{S_s\ge\frac{s}{m+1}W.}
\tag{1.3}
\]

If (k=2m-1), then for (1\le s\le m-1),

\[
 \boxed{S_s\ge\frac{s}{m}W.}
\tag{1.4}
\]

#### Proof

For (k=2m,R=m), put

\[
 a_s=\frac{{2m\choose m+s}}{{2m\choose m}}.
\]

At (s=1), (a_1=m/(m+1)).  Moreover

\[
 \frac{a_s}{a_{s-1}}=\frac{m-s+1}{m+s}
 \le\frac{m-s+1}{m-s+2}.
\]

Induction gives

\[
 a_s\le\frac{m-s+1}{m+1},
\]

which is equivalent to (1.3).

For (k=2m-1,R=m), put

\[
 b_s=\frac{{2m-1\choose m+s}}{{2m-1\choose m}}.
\]

Here (b_1=(m-1)/(m+1)\le(m-1)/m), and

\[
 \frac{b_s}{b_{s-1}}=\frac{m-s}{m+s}
 \le\frac{m-s}{m-s+1}.
\]

Thus (b_s\le(m-s)/m), proving (1.4).  \(□\)

## 2. Comparison with seam current

Suppose the owner shore is partitioned into (c) closed carousels, each of
size in

\[
 \{M-2,M-1,M\}.
\tag{2.1}
\]

For (d\ge2), hence (q\ge3),

\[
 \boxed{
 c\le
 \begin{cases}
 W/(m+1),&k=2m,\\
 W/m,&k=2m-1.
 \end{cases}}
\tag{2.2}
\]

Indeed (M-2=m+q-2\ge m+1) in the even case, while
(M-2=m+q-3\ge m) in the odd case.

Combining (1.3)--(1.4) with (2.2) gives the exact domination

\[
 \boxed{S_s\ge cs.}
\tag{2.3}

## 3. Meaning for carousel fusion

The common-state fusion theorem shows that if (c) component seams are
changed, then at source length

\[
 j=q+s=d+1+s
\]

the number of deleted old crossing occurrences is exactly

\[
 c(j-d-1)=cs,
\tag{3.1}
\]

as long as a crossing path meets at most one selected seam.  Equation (2.3)
therefore says:

\[
 \boxed{
 \text{At every such upper rank, the forced duplicate bank is at least as
 large as the entire fusion current.}}
\tag{3.2}
\]

So the upper obstruction to fusing (Theta(W/k)) carousel components is not
scalar.  In principle every deleted crossing occurrence can be chosen from a
duplicate occurrence of its named target.

For the final few widths, where a path can meet more than one selected seam
or a nonmaximal carousel has already reached its full period, the dedicated
full-ground rail reserve is the appropriate protected witness bank.  This
note makes no claim that arbitrary seam choices preserve those terminal
targets.

## 4. Exact remaining upper-fusion lemma

The needed strengthening is now incidence-level:

> Select one fusion interface at each carousel so that, simultaneously at
> every upper offset (s), all (cs) old crossing occurrences lie in the
> duplicate occurrence bank, while the newly created crossings retain a
> witness for every target and the lower q1 palette is preserved.

Theorem 1.1 proves every rank-wise capacity inequality for that statement.
It does not prove the common occurrence-labelled selection.  In particular,
it does not contradict examples with private seam signatures; it shows that
such examples use the wrong globally correlated seam placement.
