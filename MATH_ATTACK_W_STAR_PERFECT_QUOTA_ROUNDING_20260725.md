# Exploration W: star-perfect exact-factor quota rounding

## Status and verdict

Fix \(A>0\).  This report gives an exact finite-\(m\) formulation of the
star-perfect rounding problem, enforces both of the constraints that are
invisible in the projected star matching—\(Q_v\)-disjointness and
depth-one near-covering—and isolates the precise remaining fractional
lemma.

The positive result is the following.

> **Exact factor-first quota-rounding theorem.**  On the fixed window
> \(q\leq A\sqrt m\), let \(\vartheta_A^\star(m)\) be the least fractional
> survival-packet cover mass, minimized over one exact wreath factor and
> one common system of balanced quotas.  Let \(b_A^\star(m)\) be the least
> number of wreaths which must be deleted from one exact factor to leave a
> quota-safe core.  Then
> \[
>  \vartheta_A^\star(m)\leq b_A^\star(m)\leq
>  R_A(m)\vartheta_A^\star(m),
> \]
> where the exact packet-rank bound is
> \[
>  R_A(m)\leq 2+c_{K_A},\qquad
>  K_A=\min\{m-1,\lceil A\sqrt m\rceil\},
> \]
> and \(c_{K_A}=O_A(1)\).  Thus
> \[
>  \vartheta_A^\star(m)=O_A(t_m/m)
>  \quad\Longleftrightarrow\quad
>  b_A^\star(m)=O_A(t_m/m),
> \]
> up to a constant depending only on \(A\).  The rounded core is
> automatically extendible because the deleted wreaths remain inside the
> same exact factor.

This is a genuine dependent-rounding theorem, but its antecedent is not
proved here.  The \(O(m^{-2})\) codegree applies only to the projected
\(P_v\)-traces.  An exact two-lift theorem below shows that \(Q_v\)
compatibility is a global binary exact-cover problem.  A natural static
encoding of even the fixed \(Q_v\)-core already has a normalized
cross-codegree \(2/m\), and the middle/depth-one nested incidence is exactly
\(2/m\).  Inside a fixed exact trace fibre, independent lift bits remain
exponentially unlikely to become exact even if \(O(t_m/m)\) bits may be
changed.  Orbit rounding does preserve exact
factors and the uniform star marginals, but it only relabels every
unlabelled quota defect.

Consequently the \(O(t_m/m)\) scale is **not disproved**.  Depth-one
counting permits it and, for a collision-free depth-one core, shows that
the leading exceptional constant cannot be below \(2+o(1)\).  What is
disproved is the inference that star-side \(O(m^{-2})\) codegree by itself
supplies this scale.

All statements are unlabelled.  No common-owner labelled synchronization
is claimed.

## 1. Notation and exact quotas

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 t=t_m=\frac{W}{n}=\operatorname{Cat}_m .
\]

An unoriented wreath support is the family of the \(n\) cyclic
length-\(m\) intervals in a cyclic order of \([n]\), with reversal
identified.  Let \(\mathcal W_m\) be the set of such supports.  An exact
factor is a set \(F\subseteq\mathcal W_m\) whose supports partition
\(\binom{[n]}m\).  Every exact factor has \(t\) wreaths.

For \(1\leq q\leq m-1\), write

\[
 N_q=\binom n{m-q},\qquad
 \lambda_q=\frac{W}{N_q},\qquad
 c_q=\lfloor\lambda_q\rfloor,\qquad
 \rho_q=W-c_qN_q.
\]

Thus \(0\leq\rho_q<N_q\).  A balanced full-mass quota at depth \(q\) is
a vector

\[
 \beta_q:\binom{[n]}{m-q}\longrightarrow\{c_q,c_q+1\}
\]

with exactly \(\rho_q\) upper entries.  Equivalently,
\(\sum_S\beta_q(S)=W\).

For a wreath family \(G\), let \(\mu_q^G(S)\) be the number of wreaths of
\(G\) in which \(S\) is a cyclic interval of length \(m-q\).  At every
proper length the \(n\) cyclic intervals of one wreath are distinct, so
each wreath contributes exactly \(n\) distinct depth-\(q\) targets.  In
particular,

\[
 \sum_S\mu_q^G(S)=n|G|.                                      \tag{1.1}
\]

A core \(G\) is quota-safe through \(K\) if there are balanced quotas
\((\beta_q)_{q\leq K}\) such that

\[
 \mu_q^G(S)\leq\beta_q(S)
 \quad(1\leq q\leq K,\ S\in\tbinom{[n]}{m-q}).              \tag{1.2}
\]

It is extendible with \(b\) exceptions if there is an exact factor
\(F=G\sqcup B\) with \(|B|=b\).  The same \(F,G,B\) must work at all
controlled depths.  The quota vectors may be chosen independently at
different depths, but their union is handled by one common deletion set.

## 2. The star-perfect matching formulation

Fix a coordinate \(v\in[n]\), and split the middle layer into

\[
 P_v=\{X\in\tbinom{[n]}m:v\in X\},\qquad
 Q_v=\{X\in\tbinom{[n]}m:v\notin X\}.
\]

### Proposition 2.1 (exact star sizes and saturation)

One has

\[
 |P_v|=mt,\qquad |Q_v|=(m+1)t.                              \tag{2.1}
\]

Every wreath contains exactly \(m\) members of \(P_v\) and \(m+1\)
members of \(Q_v\).  Consequently a family of \(t\) wreaths is an exact
factor if and only if its \(P_v\)-parts and its \(Q_v\)-parts are both
pairwise disjoint.

#### Proof

The binomial identities are

\[
 \binom{2m}{m-1}=m\frac1{2m+1}\binom{2m+1}m=mt,
\]

\[
 \binom{2m}{m}=(m+1)\frac1{2m+1}\binom{2m+1}m=(m+1)t.
\]

In a cyclic order, \(v\) belongs to exactly \(m\) cyclic windows of
length \(m\).  The other \(m+1\) avoid it.  If \(t\) wreaths are disjoint
on both star sides, they contain \(mt=|P_v|\) and
\((m+1)t=|Q_v|\) distinct middle vertices, so they partition both sides.
The converse follows from exactness.  \(\square\)

The word “both” is essential.  A perfect matching of projected
\(P_v\)-traces is not yet an exact factor.

### Proposition 2.2 (degree and pair-codegree ledger)

Every middle set belongs to

\[
 D=D_m=\frac{m!(m+1)!}{2}                                  \tag{2.2}
\]

unoriented wreath supports.  If distinct middle sets \(X,Y\) have

\[
 |X\setminus Y|=|Y\setminus X|=d,\qquad 1\leq d\leq m,
\]

then

\[
 D(X,Y)=d!^2(m-d)!(m+1-d)!                                 \tag{2.3}
\]

and

\[
 \frac{D(X,Y)}D=
 \frac{2}{\binom md\binom{m+1}d}.                          \tag{2.4}
\]

For distinct \(X,Y\in P_v\), \(d\leq m-1\), and therefore

\[
 \max_{X\ne Y\in P_v}\frac{D(X,Y)}D
 =\frac{2}{m(m+1)}.                                        \tag{2.5}
\]

In the full middle hypergraph the maximum is instead

\[
 \max_{X\ne Y}\frac{D(X,Y)}D=\frac{2}{m+1},                \tag{2.6}
\]

attained by disjoint middle sets.

#### Proof

For (2.2), linearly order the \(m\) elements of \(X\), regard \(X\) as
one cyclic block, and cyclically order that block with the \(m+1\)
complementary labels.  This gives \(m!(m+1)!\) oriented cycles.  Reversal
acts freely and divides the count by two.

For two distinct sets, partition the coordinates into

\[
 X\setminus Y,\quad X\cap Y,\quad Y\setminus X,\quad
 [n]\setminus(X\cup Y),
\]

of sizes \(d,m-d,d,m+1-d\).  The two reverse block patterns containing
both intervals give the oriented count
\(2d!^2(m-d)!(m+1-d)!\); quotienting by reversal gives (2.3).
Division by (2.2) gives (2.4).  On \(1\leq d\leq m-1\), both binomial
factors are minimized simultaneously at \(d=1\), proving (2.5).  At
\(d=m\), (2.4) is \(2/(m+1)\), proving (2.6).  \(\square\)

Thus \(O(m^{-2})\) is an exact fact about the \(P_v\)-projection, not
about the full matching problem.

## 3. The exact two-lift and \(Q_v\)-synchronization theorem

Let a simple star trace mean the unordered family \(T=E\cap P_v\) of a
wreath support \(E\).

### Theorem 3.1 (two lifts of one simple trace)

For \(m\geq2\), every simple \(P_v\)-trace has exactly two full wreath
lifts.  Up to reversal, its cyclic core can be written

\[
 (r_1,\ldots,r_{m-1},v,s_1,\ldots,s_{m-1},x,y),             \tag{3.1}
\]

and its two lifts interchange the adjacent gap labels \(x,y\).

Put

\[
 R=\{r_1,\ldots,r_{m-1}\},\qquad
 S=\{s_1,\ldots,s_{m-1}\}.
\]

The two \(Q_v\)-traces share a fixed family \(K_T\subset Q_v\) of
\(m-1\) middle sets.  Their variable parts are

\[
 V_T^0=\{S\cup\{x\},R\cup\{y\}\},\qquad
 V_T^1=\{S\cup\{y\},R\cup\{x\}\}.                         \tag{3.2}
\]

The four displayed \(Q_v\)-vertices are distinct and lie outside \(K_T\).
Each pair in (3.2) consists of complementary \(m\)-subsets of
\([n]\setminus\{v\}\).

#### Proof

The \(m\) members of \(T\), ordered by their consecutive starts, induce a
path in the Johnson graph.  Consecutive path vertices reveal the leaving
and entering labels.  Hence the unordered trace reconstructs the two
ordered arms in (3.1), up to reversing the whole path.  Exactly two labels
are absent from the trace union, and they can fill the remaining adjacent
two-position gap only as \(xy\) or \(yx\).

Swapping two adjacent labels changes a cyclic interval of a fixed proper
length only when the interval contains exactly one of them.  At middle
length there are exactly two such old intervals and two such new
intervals, giving (3.2); the other \(m-1\) \(Q_v\)-intervals form \(K_T\).
All labels in \(R,S,\{x,y\}\) are distinct, which proves distinctness.
Finally

\[
 [n]\setminus\{v\}=R\sqcup S\sqcup\{x,y\},
\]

so the two members of either variable pair are complementary.  \(\square\)

Here and below, disjointness of \(Q_v\)-families means that they have no
equal middle-set vertex.  It does not mean that the underlying coordinate
sets are disjoint.

### Theorem 3.2 (exact \(Q_v\)-lift criterion and 2-SAT form)

Assume \(m\geq2\), and let \(\mathcal T\) be any family of pairwise-disjoint simple
\(P_v\)-traces.  It has a choice of full lifts forming a full-hypergraph
matching if and only if all three conditions hold:

1. the fixed families \(K_T\), \(T\in\mathcal T\), are pairwise disjoint;
2. for every \(T\), the chosen \(V_T^{\varepsilon_T}\) avoids
   \(\bigcup_UK_U\);
3. the chosen pairs \(V_T^{\varepsilon_T}\) are pairwise disjoint.

After condition 1 is checked, conditions 2 and 3 form an exact 2-CNF
satisfiability instance.  An option which meets a fixed core gives a unit
clause forbidding that option.  A collision between option \(\epsilon\) of
\(T\) and option \(\delta\) of \(U\) gives the binary clause

\[
 (\varepsilon_T\ne\epsilon)\ \vee\
 (\varepsilon_U\ne\delta).                                 \tag{3.3}
\]

If \(|\mathcal T|=t\) and the traces partition \(P_v\), satisfiability is
equivalent to an exact factor.  If \(|\mathcal T|=t-b\), satisfiability
only produces a full matching leaving \(mb\) vertices of \(P_v\) and
\((m+1)b\) vertices of \(Q_v\); it does not imply that the leave is
factorable.

#### Proof

The \(Q_v\)-part of a lift is exactly
\(K_T\sqcup V_T^{\varepsilon_T}\).  Pairwise disjointness of these parts
is therefore equivalent to conditions 1--3.  Every forbidden event
involving a lift bit involves either one option and a fixed core or two
options, which gives precisely the stated unit and binary clauses.

For \(t\) traces, their chosen \(Q_v\)-parts contain
\((m+1)t=|Q_v|\) incidences.  Pairwise disjointness therefore makes them a
partition of \(Q_v\).  Proposition 2.1 finishes the exact-factor claim.
The partial-family leave sizes follow from the same incidence count.  No
completion statement follows from those sizes alone.  \(\square\)

This theorem explicitly enforces the \(Q_v\) condition omitted by a
projected star matching.

### Proposition 3.3 (exact trace and \(Q_v\)-incidence counts)

Projection from full supports to simple traces is two-to-one.  Consequently

\[
 |\mathcal T_v|=\frac{tD}{2}=\frac{(2m)!}{4},\qquad
 \delta_P=\frac D2=\frac{(m+1)m!^2}{4}.                    \tag{3.4}
\]

Here \(\delta_P\) is the degree of every \(P_v\)-vertex in the simple trace
hypergraph.  For a fixed \(Y\in Q_v\), the number of traces with
\(Y\in K_T\) and the number with \(Y\) among the four possible variable
vertices are respectively

\[
 \delta_Q^{\rm fix}=\frac{(m-1)m!^2}{4},\qquad
 \delta_Q^{\rm var}=m!^2.                                  \tag{3.5}
\]

The uniform trace weight \(1/\delta_P=2/D\) gives \(P_v\)-load one,
fixed \(Q_v\)-load

\[
 \frac{\delta_Q^{\rm fix}}{\delta_P}=\frac{m-1}{m+1},
\]

and possible-variable \(Q_v\)-load \(4/(m+1)\).  A fair lift bit retains
half the latter, so its actual variable load is \(2/(m+1)\), and its total
expected \(Q_v\)-load is exactly one.

#### Proof

Theorem 3.1 proves the two-to-one assertion.  Double counting trace--star
incidences gives (3.4).  There are \(tD/2\) traces, each with \(m-1\)
fixed \(Q_v\)-vertices and four possible variable vertices.  Division by
\(|Q_v|=(m+1)t\) gives (3.5).  The load identities follow by division by
\(\delta_P\).  \(\square\)

Thus the star fractional ledger is internally exact.  Its difficulty is
not fractional mass balance; it is correlated integral synchronization.

### Proposition 3.4 (the \(Q_v\)-aware codegree loss)

For \(m\geq2\), augment each simple trace by its unavoidable fixed core
\(K_T\).  Let \(\Delta_2\) denote the maximum codegree of two **distinct**
vertices in this augmented trace hypergraph, and let
\(\delta_{\min}=\delta_Q^{\rm fix}\) be the smaller of the \(P_v\)-degree
and fixed-\(Q_v\) degree.  Then the augmented incidence hypergraph has

\[
 \boxed{\frac{\Delta_2}{\delta_{\min}}\geq\frac{2}{m}.}     \tag{3.6}
\]

In particular, explicitly retaining even the fixed part of
\(Q_v\)-compatibility loses the \(O(m^{-2})\) codegree scale.

#### Proof

Choose disjoint \(X\in P_v\) and \(Y\in Q_v\).  There are \(m!^2\) full
wreath supports containing both, by (2.3) with \(d=m\).  Normalize such a
cycle as an \(X\)-block, the unique label outside \(X\cup Y\), and a
\(Y\)-block.  As the position of \(v\) ranges over the \(m\) positions of
the \(X\)-block, \(Y\) belongs to the invariant fixed core unless \(v\) is
at the one boundary position for which one of the two gap labels is the
outside singleton.  Thus the fixed-core fraction is \((m-1)/m\).  Each
trace with \(Y\in K_T\) accounts for both of its full lifts, so the
augmented cross-codegree is

\[
 c_{PK}=\frac{m-1}{2m}m!^2.                                \tag{3.7}
\]

By (3.5), \(\delta_{\min}=(m-1)m!^2/4\), giving the ratio \(2/m\) for
this particular cross pair and hence (3.6).  \(\square\)

The lower-rank quota system has the same loss without mentioning \(Q_v\).
For \(S\subset X\), \(|X|=m\), \(|S|=m-q\), conditioning on \(X\) being a
middle interval gives

\[
 \frac{\operatorname{codeg}(X,S)}D
 =\frac{(m-q)!(q+1)!}{m!}
 =\frac{q+1}{\binom mq}.                                   \tag{3.8}
\]

Indeed, \(S\) must form one block in the internal linear order of \(X\).
At depth one, (3.8) is exactly \(2/m\).

Equations (3.6) and (3.8) do not prove that a correlated rounding is
impossible.  They prove that a theorem whose only hypothesis is the
projected codegree (2.5) has omitted mandatory correlations.

## 4. Exact marginal-preserving star rounding

There is an unconditional dependent rounding of the uniform star
fractional point to exact factors.  It is deliberately stated because it
separates exact ownership from quota improvement.

### Theorem 4.1 (stabilizer-orbit exact rounding)

Fix an exact factor \(F_0\).  Choose a uniformly random permutation
\(\pi\in\operatorname{Stab}(v)\), and output \(\pi F_0\).  Then, samplewise,
\(\pi F_0\) is an exact factor and hence satisfies both \(P_v\)- and
\(Q_v\)-disjointness.  For every full wreath \(E\) and simple trace \(T\),

\[
 \Pr(E\in\pi F_0)=\frac1D,\qquad
 \Pr(T\text{ is selected})=\frac2D=\frac1{\delta_P}.       \tag{4.1}
\]

Conditioned on selecting \(T\), its two lifts each have probability
\(1/2\).

#### Proof

The stabilizer of \(v\) is transitive on full wreath supports: rotate two
cyclic representatives so that \(v\) occupies the same position and map
the remaining labels position by position.  Therefore every full support
has the same inclusion probability.  Since every sample contains \(t\)
supports and

\[
 |\mathcal W_m|=tD=\frac{(2m)!}{2},
\]

that probability is \(1/D\).  A simple trace has two lifts, and an exact
factor can contain at most one of them because they have the same
\(P_v\)-vertices.  Summing their equal marginals gives \(2/D\) and the
conditional fair bit.  Exactness is preserved by relabelling.  \(\square\)

For every depth,

\[
 \mu_q^{\pi F_0}(S)=\mu_q^{F_0}(\pi^{-1}S).                 \tag{4.2}
\]

Thus orbit rounding only permutes the histogram.  It cannot decrease any
ground-permutation-invariant unlabelled collision functional.

### Theorem 4.2 (marginal-preserving laws do not relax an invariant factor objective)

Let \(\Phi\) be any real functional on exact factors invariant under ground
permutations.  Then

\[
 \inf_{\substack{\mathbb P\text{ on exact factors}\\
          \mathbb E_{\mathbb P}\mathbf1_F=D^{-1}\mathbf1}}
       \mathbb E_{\mathbb P}\Phi(F)
 =\min_{F\text{ exact}}\Phi(F).                            \tag{4.3}
\]

This applies in particular to the optimized packet value and optimized
integral deletion number defined below.

#### Proof

The expectation of \(\Phi\) under any law is at least its deterministic
minimum.  Conversely, orbit-symmetrize a deterministic minimizer as in
Theorem 4.1.  It has the required uniform full-support marginals, and
\(\Phi\) is constant on its orbit.  \(\square\)

Therefore exact-factor dependent rounding solves the ownership equations,
including \(Q_v\), but for an invariant quota objective it is not a
relaxation of the deterministic selection problem.

## 5. Factor-first survival-packet rounding

Fix one exact factor \(F\), one window \(1\leq q\leq K\), and one balanced
quota system \(\beta=(\beta_q)_{q\leq K}\).  For a resource
\(a=(q,S)\), define its owner set

\[
 \mathcal O_a=\{E\in F:S\text{ is a depth-}q
                      \text{ interval of }E\}.              \tag{5.1}
\]

This is an honest set and
\(|\mathcal O_a|=\mu_q^F(S)\).  Define the survival packets of \(a\) by

\[
 \mathcal P_a=
 \{P\subseteq\mathcal O_a:|P|=\beta_q(S)+1\}.              \tag{5.2}
\]

Let \(\mathcal P(F,\beta)\) be the union of these packet families over all
controlled resources.  Resource labels may be retained on parallel packet
copies; this does not change covers.

### Theorem 5.1 (exact packetization)

For \(B\subseteq F\) and \(G=F\setminus B\), the following are equivalent:

1. \(G\) is quota-safe for the chosen \(\beta\);
2. \(B\) meets every packet in \(\mathcal P(F,\beta)\).

#### Proof

At resource \(a\), the residual load is
\(|\mathcal O_a\setminus B|\).  It exceeds \(\beta_q(S)\) if and only if
\(\mathcal O_a\setminus B\) contains a subset of size
\(\beta_q(S)+1\), which is exactly a packet disjoint from \(B\).  The same
\(B\) is used for the union over all depths.  \(\square\)

Let \(\tau(F,\beta)\) be the minimum cardinality of an integral packet
cover, and define the fractional packet-cover value

\[
 \vartheta(F,\beta)=
 \min\left\{
       \sum_{E\in F}x_E:
       0\leq x_E\leq1,
       \ \sum_{E\in P}x_E\geq1
       \quad(P\in\mathcal P(F,\beta))
     \right\}.                                             \tag{5.3}
\]

### Theorem 5.2 (bounded-rank deterministic rounding)

Let

\[
 R(F,\beta)=
 \max_{P\in\mathcal P(F,\beta)}|P|,
\]

with \(R=1\) if there are no packets.  Then

\[
 \boxed{\quad
 \vartheta(F,\beta)\leq\tau(F,\beta)
 \leq R(F,\beta)\vartheta(F,\beta).
 \quad}                                                     \tag{5.4}
\]

The rounded deletion family is a subset of the same exact factor, so its
complement is automatically extendible.

#### Proof

The first inequality is relaxation.  Let \(x\) be a fractional packet
cover and set

\[
 B=\{E\in F:x_E\geq1/R\}.                                  \tag{5.5}
\]

If a packet \(P\) missed \(B\), then every \(x_E<1/R\) on \(P\), whence

\[
 \sum_{E\in P}x_E<|P|/R\leq1,
\]

contradicting (5.3).  Hence \(B\) covers all packets.  Also

\[
 |B|\leq R\sum_Ex_E.
\]

Apply Theorem 5.1.  Since \(F=(F\setminus B)\sqcup B\) remains one exact
factor, no residual-completion lemma is used.  \(\square\)

### Lemma 5.3 (fixed-window packet-rank bound)

For \(m\geq2\), let

\[
 K_A=\min\{m-1,\lceil A\sqrt m\rceil\}.
\]

Since \(\lambda_q\) is increasing in \(q\),

\[
 R(F,\beta)\leq R_A(m):=2+c_{K_A},                          \tag{5.6}
\]

where

\[
 c_{K_A}=\left\lfloor
 \frac{(m-K_A)!(m+K_A+1)!}{m!(m+1)!}
 \right\rfloor.                                           \tag{5.7}
\]

For every fixed \(A\), \(R_A(m)=O_A(1)\).  More explicitly, if

\[
 m\geq M_A:=\left\lceil4(A+1)^2\right\rceil,
\]

then

\[
 R_A(m)\leq
 2+\left\lfloor\exp\bigl(2(A+1)(A+2)\bigr)\right\rfloor.   \tag{5.8}
\]

#### Proof

A balanced quota is \(c_q\) or \(c_q+1\), so a packet has size at most
\(c_q+2\).  The product

\[
 \lambda_q=
 \prod_{i=0}^{q-1}\frac{m+2+i}{m-i}
 =\frac{(m-q)!(m+q+1)!}{m!(m+1)!}                          \tag{5.9}
\]

is increasing, proving (5.6)--(5.7).

For the explicit bound, \(q\leq K_A\leq(A+1)\sqrt m\leq m/2\) under the
stated hypothesis, and

\[
 \begin{aligned}
 \log\lambda_q
 &\leq\sum_{i=0}^{q-1}\frac{2(i+1)}{m-i}\\
 &\leq\frac{q(q+1)}{m-q+1}
 \leq2(A+1)(A+2).
 \end{aligned}                                             \tag{5.10}
\]

Taking floors proves (5.8).  \(\square\)

### Theorem 5.4 (exact star-perfect quota-rounding equivalence)

Define

\[
 \vartheta_A^\star(m)=
 \min_{\substack{F\text{ exact}\\
                   \beta_q\text{ balanced},\ q\leq K_A}}
       \vartheta(F,\beta),                                  \tag{5.11}
\]

and

\[
 b_A^\star(m)=
 \min\left\{|B|:
 \begin{array}{l}
 F\text{ is exact},\ B\subseteq F,\ G=F\setminus B,\\
 \text{and one balanced quota system }\beta
 \text{ obeys }\mu_q^G\leq\beta_q\ (q\leq K_A)
 \end{array}\right\}.                                     \tag{5.12}
\]

Then, for every \(m\geq2\),

\[
 \boxed{
 \vartheta_A^\star(m)\leq b_A^\star(m)
 \leq R_A(m)\vartheta_A^\star(m).
 }                                                          \tag{5.13}
\]

Consequently, for every fixed \(A\),

\[
 \boxed{
 \vartheta_A^\star(m)=O_A(t/m)
 \quad\Longleftrightarrow\quad
 b_A^\star(m)=O_A(t/m),
 }                                                          \tag{5.14}
\]

where either statement produces one extendible quota-safe core with the
claimed exceptional scale.

#### Proof

If \(B\) is feasible in (5.12), Theorem 5.1 makes it an integral packet
cover, hence a fractional cover, and
\(\vartheta_A^\star\leq|B|\).  Conversely, minimize (5.11), apply the
threshold rounding of Theorem 5.2, and use Lemma 5.3.  The deletion family
lies inside the minimizing exact factor.  This proves (5.13), and the
fixed-\(A\) boundedness of \(R_A(m)\) proves (5.14).  \(\square\)

There is also a distributional form.  Suppose a law is supported on exact
star-perfect factors, and each sample \(F\) is supplied with balanced
quotas and a fractional packet cover \(x^F\).  If

\[
 \mathbb E\sum_{E\in F}x_E^F\leq L,
\]

some sample has fractional mass at most \(L\), and Theorem 5.2 produces
an extendible core with at most \(R_A(m)L\) exceptions.  Applying this to
the orbit law of Theorem 4.1 does not create a bound: the optimized value
\(\vartheta_A(F)\) is invariant along the orbit.

The theorem is exact and unconditional.  The assertion

\[
 \boxed{
 \vartheta_A^\star(m)=O_A(t/m)
 }                                                          \tag{SPC_A}
\]

is the unproved mathematical input.

## 6. Depth-one near-covering, with exact constants

The quota condition can be eliminated from the statement of a proposed
core.

### Lemma 6.1 (quota-free domination criterion)

Let \(F=G\sqcup B\) be exact with \(|B|=b\), fix \(q\), and put
\(\eta(S)=\mu_q^G(S)\).  There exists a balanced quota
\(\beta_q\geq\eta\) if and only if

\[
 \max_S\eta(S)\leq c_q+1,\qquad
 \sum_S(c_q-\eta(S))_+\leq nb.                             \tag{6.1}
\]

#### Proof

Assume the ceiling in (6.1), and let

\[
 U=\{S:\eta(S)=c_q+1\},\qquad
 \Delta=\sum_S(c_q-\eta(S))_+.
\]

Using (1.1) and \(|G|=t-b\),

\[
 |U|-\Delta
 =\sum_S(\eta(S)-c_q)
 =(W-nb)-c_qN_q
 =\rho_q-nb.                                               \tag{6.2}
\]

Every member of \(U\) must receive an upper quota.  There are enough upper
slots exactly when \(|U|\leq\rho_q\), which by (6.2) is equivalent to
\(\Delta\leq nb\).  Assign upper quotas to \(U\) and to any additional
\(\rho_q-|U|\) targets.  This proves sufficiency; necessity is immediate
from the same argument.  \(\square\)

At depth one, for \(m\geq3\),

\[
 \lambda_1=\frac{m+2}{m},\qquad c_1=1,\qquad
 N_1=\frac{m}{m+2}W,\qquad
 \rho_1=\frac{2}{m+2}W=\frac{2nt}{m+2}.                    \tag{6.3}
\]

### Corollary 6.2 (exact depth-one ledger)

Let \(n_j\) be the number of depth-one targets of core load \(j\).  The
core is depth-one quota-safe if and only if

\[
 \max_S\mu_1^G(S)\leq2,\qquad n_0\leq nb.                  \tag{6.4}
\]

Under the ceiling condition, one has the exact identity

\[
 \boxed{n_2-n_0=\rho_1-nb.}                                \tag{6.5}
\]

Consequently

\[
 0\leq n_0\leq nb,\qquad
 \max\{0,\rho_1-nb\}\leq n_2\leq\rho_1.                  \tag{6.6}
\]

#### Proof

For \(c_1=1\), the deficit in (6.1) is exactly \(n_0\).  Also

\[
 n_0+n_1+n_2=N_1,\qquad
 n_1+2n_2=W-nb.
\]

Subtracting gives (6.5).  Combining it with \(0\leq n_0\leq nb\) gives
(6.6).  \(\square\)

Thus an exceptional family of size \(b=O_A(t/m)\) forces

\[
 n_0\leq nb=O_A(t).                                        \tag{6.7}
\]

Since \(N_1=\Theta(W)=\Theta(mt)\), the core misses only an
\(O_A(1/m)\) fraction of depth-one targets.  This is the requested
depth-one near-covering, and it is part of the theorem rather than an
unstated nibble heuristic.

The arithmetic does not make the \(O(t/m)\) scale impossible.  If one asks
for the stronger collision-free core \(n_2=0\), then (6.5) forces

\[
 n_0=nb-\rho_1,\qquad
 b\geq\frac{\rho_1}{n}=\frac{2t}{m+2}
 =(2+o(1))\frac tm.                                        \tag{6.8}
\]

This leading constant \(2\) is sharp only at the aggregate, globally
uniform fractional-ledger level: give every full wreath candidate weight
\(1/D\), then scale all weights by \(m/(m+2)\).  The unscaled depth-one
load is \(\lambda_1\), the scaled load is one, and the missing fractional
mass is \(2t/(m+2)\).  This is not the thinning of an arbitrary fixed
factor.  For general quota-safe cores, loads two are allowed, and (6.5)
gives no positive lower bound on \(b\).

No statement here says that the exceptional wreaths physically fill all
the depth-one holes.  The \(nb\) quantity in Lemma 6.1 is quota slack and
the later overload charge.  Actual exact completion is guaranteed only by
factor-first deletion from \(F\).

## 7. Why naive lift rounding cannot supply the theorem

### 7.1 Exact lift-cycle conservation in one trace fibre

Fix an exact factor \(F\) and regard each member as the base lift of its
simple \(P_v\)-trace.  Write its base and twin variable pairs as
\(R_T=V_T^0\) and \(A_T=V_T^1\).  The base fixed cores together with the
pairs \(R_T\) partition \(Q_v\).

If \(A_T\) meets a fixed core, leave \(\phi(T)\) undefined.  Otherwise its
two complementary \(Q_v\)-vertices lie in the residual set and hence equal
one unique complementary base pair \(R_U\); define \(\phi(T)=U\).

### Lemma 7.1 (cycle law)

For \(I\subseteq F\), replacing precisely the traces in \(I\) by their
twin lifts preserves exactness if and only if \(\phi\) is defined on \(I\)
and \(\phi|_I\) is a permutation of \(I\).  Equivalently, \(I\) is a union
of directed cycles of the partial functional graph \(\phi\).

#### Proof

Every \(P_v\)-vertex and every fixed \(Q_v\)-vertex remains unchanged.
Exactness of the variable part is therefore exactly

\[
 \{A_T:T\in I\}=\{R_T:T\in I\}.
\]

By the definition and uniqueness of \(\phi\), this equality is equivalent
to \(\phi(I)=I\) with multiplicity one, hence to the permutation condition.
\(\square\)

For \(m\geq4\), the partial map has no directed cycles of length one, two,
or three.  A one-cycle is impossible because the four variable vertices
in (3.2) are distinct.  For a two-cycle, the four changed sets are

\[
 S\cup\{x\},\ S\cup\{y\},\ R\cup\{x\},\ R\cup\{y\}.
\]

For \(m\geq3\), the only pairs among them with intersection \(m-1\) are
the two pairs sharing the side core \(S\) or \(R\); cross intersections
have size zero or one.  Hence a second trace using the reverse two-cycle
has the same two side cores.  After adjoining \(v\), the two projected
traces share \(S\cup\{v\}\) and \(R\cup\{v\}\), contradicting exactness.

For completeness, a three-cycle projects to a triangle in the folded
Johnson graph on complementary \(m\)-set pairs in
\([n]\setminus\{v\}\).  Choose representatives \(A,B,C\) with
\(|A\cap B|=|A\cap C|=m-1\).  Then
\(|B\cap C|\geq m-2\); folded adjacency allows intersection \(m-1\) or
one, so for \(m\geq4\) it must be \(m-1\).  The resulting ordinary Johnson
triangle is a star or a top.  In either case the three trace edges have a
common side core, and the three \(P_v\)-traces share a middle vertex after
adjoining \(v\), again contradicting exactness.

Let \(c(\phi)\) be the number of directed cycles.  The preceding result
gives

\[
 c(\phi)\leq t/4.                                          \tag{7.1}
\]

By Lemma 7.1, the exact lift assignments in this fixed trace fibre are
precisely the \(2^{c(\phi)}\) unions of cycles.

### Corollary 7.2 (independent-bit obstruction)

For \(m\geq4\), independent fair choices of the \(t\) lift bits form an
exact factor with probability at most

\[
 2^{c(\phi)-t}\leq2^{-3t/4}.                               \tag{7.2}
\]

Even if, after seeing the bits, one may change at most \(b\) lift bits in
an attempt to reach a full exact assignment in this same trace fibre, the
probability of lying within Hamming distance \(b\) of an exact lift
assignment is at most

\[
 2^{c(\phi)-t}\sum_{j=0}^{b}\binom tj.                     \tag{7.3}
\]

For \(b=O(t/m)\), the logarithm of the binomial sum is \(o(t)\), so (7.3)
is \(2^{-3t/4+o(t)}\).

#### Proof

There are \(2^t\) bit vectors and at most \(2^{c(\phi)}\) exact vectors.
The union of their Hamming balls of radius \(b\) has size at most
\(2^{c(\phi)}\sum_{j\leq b}\binom tj\).  For
\(b/t=O(1/m)\), the elementary entropy bound

\[
 \sum_{j=0}^{b}\binom tj
 \leq\exp\bigl(tH(b/t)\bigr)=2^{o(t)}
\]

follows from \(H(x)=-x\log x-(1-x)\log(1-x)\to0\).  \(\square\)

This is a fixed exact full-fibre obstruction.  It does not rule out
cycle-aware dependent bits, correlated choice of the traces themselves, a
generic partial trace matching, deletion followed by completion outside
the original fibre, or a factor-first construction.  It proves only that
independent local lift rounding in this fixed exact fibre remains
exponentially unlikely to become exact after \(O(t/m)\) bit changes.

### 7.2 Stabilizer-invariant fractional thinning

The stabilizer of \(v\) is transitive on the wreath candidates.  Therefore
any deterministic stabilizer-invariant candidate weighting is constant,
say \(x_E=\alpha/D\).  It has total mass \(\alpha t\), middle load
\(\alpha\), and depth-\(q\) target load \(\alpha\lambda_q\).

Suppose one fixed balanced quota is required to dominate this invariant
fractional core.  If the quota has a floor entry, then necessarily

\[
 \alpha\lambda_q\leq c_q,\qquad
 (1-\alpha)t\geq\left(1-\frac{c_q}{\lambda_q}\right)t.      \tag{7.4}
\]

For \(q=\lfloor x\sqrt m\rfloor\), fixed
\(0<x<\sqrt{\log2}\), expansion of (5.9) gives

\[
 \log\lambda_q=\frac{q(q+1)}m+O_x(m^{-1/2}),\qquad
 \lambda_q\longrightarrow e^{x^2}\in(1,2).
\]

Thus \(c_q=1\) for all sufficiently large \(m\), and (7.4) forces

\[
 (1-\alpha)t\geq
 (1-e^{-x^2}+o(1))t=\Omega_x(t),                            \tag{7.5}
\]

not \(O(t/m)\).

This rules out only a fixed-quota, stabilizer-invariant fractional
thinning.  It does not rule out nonuniform balanced quotas, symmetry
breaking in one realization, or an invariant distribution obtained by
co-relabelling a good factor, core, and quota system.  At depth one the
same calculation gives only the sharp fractional loss
\(2t/(m+2)\), in agreement with (6.8).

## 8. Consequence of the target scale and the remaining star-core lemma

Suppose \((SPC_A)\) is proved.  Theorem 5.4 supplies an exact split

\[
 F=G\sqcup B,\qquad |B|=O_A(t/m),\qquad
 \mu_q^G\leq\beta_q\quad(q\leq K_A).                        \tag{8.1}
\]

Let \(O_q(F)\) be the minimum unlabelled overload of the full factor over
balanced depth-\(q\) quotas.  Since every exceptional wreath contributes
\(n\) depth-\(q\) incidences,

\[
 O_q(F)\leq n|B|.                                          \tag{8.2}
\]

Indeed, for the quota in (8.1), put
\(s_q=\beta_q-\mu_q^G\geq0\).  Its total mass is \(n|B|\), and

\[
 (\mu_q^F-\beta_q)_+
 =(\mu_q^B-s_q)_+\leq\mu_q^B.
\]

Summing gives (8.2).  Therefore

\[
 \sum_{q\leq K_A}\frac{O_q(F)}{c_q}
 \leq n|B|K_A
 =O_A(W/\sqrt m)=o(W).                                     \tag{8.3}
\]

For each fixed \(A\), this is the small unlabelled Gaussian-window
overload required by the frozen MWB reduction.  If \((SPC_A)\) is proved
for every fixed \(A>0\) (positive integers suffice), a slow choice
\(A=A(m)\to\infty\) diagonalizes these fixed-window conclusions to MWB.
The factors may depend on both \(m\) and \(A\).  No labelled common-owner
conclusion is inferred.

The precise remaining statement for this star-core strategy is:

> **Star survival-packet conjecture \((SPC_A)\), UNPROVED.**  For every
> fixed \(A>0\) and all sufficiently large \(m\), there exist one exact
> cyclic-wreath factor \(F_{m,A}\), one balanced quota vector at each depth
> \(1\leq q\leq K_A\), and one fractional cover \(x\) of the union of all
> their survival packets such that
> \[
>  \sum_{E\in F_{m,A}}x_E=O_A(t_m/m).
> \]

The common-object quantifier is indispensable.  Separate factors, cores,
or covers for different depths do not imply the conjecture.  The quotas
may differ by depth, but one cover must hit the entire packet union.

Equivalently, by LP duality, there must exist one common choice of \(F\)
and the quotas for which every fractional packing of these packets with
total congestion at most one on each wreath has mass \(O_A(t/m)\).  This
dual form is exact but is no easier from the present star codegree data.

## 9. Adversarial audit and implication scope

1. **Integral ownership is never averaged away.**  Theorems 3.2 and 4.1
   enforce literal \(P_v\)- and \(Q_v\)-disjointness.  Theorem 5.4 deletes
   whole wreaths from one exact factor.

2. **Projected and augmented codegrees are distinguished.**  The value
   \(2/[m(m+1)]\) belongs to pairs in \(P_v\).  Fixed-\(Q_v\) and
   middle/depth-one incidences have order \(1/m\).  No nibble conclusion is
   drawn from either number.

3. **The two-lift problem is not treated as independent.**  The 2-SAT
   criterion includes fixed-core collisions, unit conflicts, and
   option--option conflicts.  For a perfect trace matching, disjointness
   covers \(Q_v\) by exact mass.  For a partial trace matching it gives no
   residual factorization.

4. **Depth one is genuinely near-covered.**  Quota safety is exactly the
   conjunction in (6.4), not merely a bound on average load.  At the target
   scale the number of holes is \(O_A(t)\).

5. **Quota slack is not physical filling.**  The identity
   \(n_2-n_0=\rho_1-nb\) is an arithmetic core ledger.  It does not specify
   where the exceptional wreath incidences land.

6. **The packet LP is the correct relaxation.**  It covers every
   \((\beta+1)\)-subset of each owner set.  It is not silently replaced by
   the different, strictly stronger fractional multicover inequalities
   which directly delete the current overload demand.  The two integral
   formulations are equivalent, but their fractional relaxations need not
   be.

7. **The packet rank is constant only at fixed \(A\).**  The exact bound is
   (5.6)--(5.7).  It may deteriorate arbitrarily when \(A\) grows, so the
   theorem must be proved separately for every fixed window before
   diagonalization.

8. **Orbit rounding is quota-inert only for invariant objectives.**  It
   need not preserve or improve a prescribed labelled quota.  The
   optimized unlabelled packet value is invariant because both targets and
   quotas may be relabelled together.

9. **The independent-bit obstruction is local to one trace fibre.**  It
   does not exclude a global correlated construction.  The
   stabilizer-invariant obstruction is still narrower: it assumes one fixed
   quota dominates one deterministic invariant fractional core.

10. **No global impossibility is claimed.**  Exact factors themselves show
    that \(Q_v\)-synchronization can be perfect.  Depth-one arithmetic also
    permits \(b=0\) if the full factor already has its loads in
    \(\{1,2\}\) with exactly \(\rho_1\) double targets.  None of Sections
    3, 4, 6, or 7 rules out \((SPC_A)\).

11. **The decisive missing step was independently rechecked.**  The exact
    constants in the star trace ledger, the two-lift decomposition, the
    depth-one quota criterion, and the factor-\(R_A\) threshold rounding
    were recomputed independently.  The audit found no route from the
    \(O(m^{-2})\) projected codegree to the unproved bound
    \((SPC_A)\).

## Final boundary

The star-perfect formulation does support an exact dependent-rounding
theorem: exact factors give marginal-preserving star roundings, the
two-lift criterion enforces \(Q_v\) literally, and a fractional
survival-packet cover rounds deterministically to an extendible quota-safe
core with only a fixed-\(A\) loss.  At depth one such a core automatically
misses only \(O(t)\) targets when \(O(t/m)\) wreaths are exceptional.

What remains open within this strategy is not the last integrality step.
It is the construction of one exact factor whose common multidepth
survival-packet LP has value \(O_A(t/m)\).  This condition is sufficient,
not asserted necessary for MWB by every possible route.  The projected
\(O(m^{-2})\) codegree does not control that LP because the mandatory
\(Q_v\) and depth-one correlations already live at scale \(1/m\).  No
exact covariance invariant or counting obstruction found here forbids the
desired \(O(t/m)\) scale.
