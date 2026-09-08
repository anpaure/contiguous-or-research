# The saturating Johnson cycle: exact rank-two continuation and the literal first cut

Date: 2026-07-25

Method: pure mathematics only. No search, computation, or solver is used.

## 1. Setup and result

Put

\[
 n=2m+1,\qquad V_q=\binom{[n]}{m-q},\qquad
 N_q=|V_q|,\qquad W=N_0.
\]

Let

\[
 S_0,X_0,S_1,X_1,\ldots,S_{N_1-1},X_{N_1-1},S_0
 \tag{1.1}
\]

be a saturating cycle between ranks \(m-1\) and \(m\): the \(S_i\)'s
are all the members of \(V_1\), the \(X_i\)'s are distinct, and

\[
 S_i\subset X_i\supset S_{i+1}.
\]

Write

\[
 U=\{X_i\},\qquad E=V_0\setminus U,\qquad
 r:=|E|=W-N_1=\frac{2W}{m+2}.
 \tag{1.2}
\]

Orient the first frozen step by \(X_i\mapsto S_i\). Thus the frozen
owners in \(U\) have rank-one load exactly one on every member of \(V_1\).
The cycle gives an exact matching from \(E\) to distinct facets; if its
image is \(H_1\), the total rank-one load is

\[
 a(S)=1+\mathbf 1_{H_1}(S),\qquad |H_1|=r.
 \tag{1.3}
\]

This note proves two sharply separated statements.

1. **Abstract rank-two continuation.** For every \(m\ge37\), every vector
   (1.3), with no condition on the location of \(H_1\), admits an integral
   inclusion flow to a balanced rank-two vector taking only the values one
   and two. In fact one can preserve the stronger decomposition into an
   \(N_1\)-mass balanced core and an injective \(r\)-path residual: the
   residual occupies distinct targets at both ranks, the core is low on
   those targets, and their sum is exactly balanced. Thus the omitted-owner
   construction has no intrinsic Boolean Hall obstruction at transition two
   if second deletions may be chosen freely.

2. **Literal consecutive-intersection continuation.** If instead the
   frozen second target is prescribed by the Johnson cycle, its multiplicity
   histogram \(h\) must satisfy an exact pointwise-and-zero-count test before
   the residual Hall inequalities can even be posed. The complete residual
   family inequality is displayed in (4.8). The saturating-cycle theorem
   supplies none of these rank-two conditions.

The first statement is not a cyclic-factor theorem. A long Johnson cycle is
not a disjoint union of length-\(n\) tight wreaths, and an abstract choice of
the second deletion need not be the literal second deletion in any one exact
wreath factor.

## 2. Exact rank-one matching and cut slack

Every \(S\in V_1\) has \(m+2\) middle supersets. Two distinct ones are its
neighbors in (1.1), and both lie in \(U\). Hence

\[
 e_E(S):=|\{X\in E:S\subset X\}|\le m.
 \tag{2.1}
\]

For any \(\mathcal D\subseteq E\), count its root--facet incidences. Every
root has degree \(m\), whereas (2.1) bounds every facet degree by \(m\):

\[
 m|\mathcal D|
 \le m|\partial\mathcal D|.
\]

Hall therefore gives an injection

\[
 \phi:E\longrightarrow V_1,\qquad \phi(X)\subset X.
 \tag{2.2}
\]

Take \(H_1=\phi(E)\). For \(\mathcal A\subseteq V_1\), let
\(N_1(\mathcal A)\) be its middle supersets. The exact transition-one
collar slack is

\[
 \boxed{
 |E\cap N_1(\mathcal A)|-|H_1\cap\mathcal A|\ge0.}
 \tag{2.3}
\]

Indeed, the distinct preimages under \(\phi\) of the elements of
\(H_1\cap\mathcal A\) all lie in \(E\cap N_1(\mathcal A)\). This proves
all rank-one survival and crossing cuts, not only marginal balance.

## 3. Every balanced rank-one vector extends abstractly to rank two

Between \(V_1\) and \(V_2\), join a parent \(S\) to each
\((m-2)\)-subset of \(S\). Give parent \(S\) the exact supply (1.3), and
give every child lower capacity one and upper capacity two.

### Theorem 3.1

For \(m\ge37\), this capacitated inclusion network has an integral flow of
value \(W\). Consequently its child loads form a balanced vector

\[
 b_2(T)\in\{1,2\},\qquad \sum_{T\in V_2}b_2(T)=W.
 \tag{3.1}
\]

#### Proof

The feasible-transportation form of Hoffman's theorem has exactly two cut
families here:

\[
 a(\mathcal P)\le2|\partial\mathcal P|
 \quad(\mathcal P\subseteq V_1),
 \tag{3.2}
\]

and

\[
 |\mathcal B|\le a(N_2(\mathcal B))
 \quad(\mathcal B\subseteq V_2).
 \tag{3.3}
\]

For completeness, these are sufficient as well as necessary. Split the
usual source--parent--child--sink network, put the exact supplies on the
source arcs and the interval \([1,2]\) on the child--sink arcs, and add the
fixed return arc of value \(W\). In Hoffman's inequality, a finite cut must
contain the neighbors of each parent it contains. The cases in which source
and sink lie on opposite sides give (3.2); the cases in which they lie on
the same side give (3.3), after complementation. There are no further mixed
cuts.

The upward normalized-matching property of the Boolean lattice gives

\[
 |N_2(\mathcal B)|\ge |\mathcal B|.
\]

Since \(a(S)\ge1\), this proves (3.3).

It remains to prove (3.2). Put

\[
 t=|\mathcal P|,\qquad s=|\partial\mathcal P|.
\]

Since there are only \(r\) high parents,

\[
 a(\mathcal P)\le t+\min\{t,r\}.
 \tag{3.4}
\]

Let

\[
 T_0=\binom{2m-3}{m-1}.
\]

If \(t\le T_0\), the Lovasz form of the Kruskal--Katona theorem gives
\(s\ge t\): writing \(t=\binom{x}{m-1}\), one has
\(x\le2m-3\), and therefore

\[
 \frac{\binom{x}{m-2}}{\binom{x}{m-1}}
 =\frac{m-1}{x-m+2}\ge1.
\]

Equations (3.4) and \(s\ge t\) imply (3.2).

If \(t\ge T_0\), normalized matching between the two complete ranks gives

\[
 s\ge\frac{N_2}{N_1}t
 =\frac{m-1}{m+3}t.
\]

Hence

\[
 2s-t\ge\frac{m-5}{m+3}t.
 \tag{3.5}
\]

The exact endpoint calculation is

\[
 \frac{\frac{m-5}{m+3}T_0}{r}
 =
 \frac{m(m+1)(m+2)(m-5)}
 {8(m+3)(4m^2-1)}.
 \tag{3.6}
\]

At \(m=37\), the numerator and denominator in the comparison are

\[
 37\cdot38\cdot39\cdot32=1,754,688,
\]

and

\[
 8\cdot40\cdot5475=1,752,000.
\]

The difference

\[
 m^4-34m^3-109m^2-2m+24
\]

is increasing for \(m\ge37\). Thus (3.6) is at least one throughout this
range. Equations (3.4)--(3.6) give

\[
 2s-t\ge r\ge|H_1\cap\mathcal P|,
\]

which is (3.2).

All lower and upper capacities are integral, so network integrality gives
an integral flow. Finally,

\[
 1<\frac W{N_2}
 =\frac{(m+2)(m+3)}{m(m-1)}<2
\]

for \(m\ge8\). Hence an integral child vector in \([1,2]\) with total
\(W\) is exactly balanced. \(\square\)

Theorem 3.1 permits the copies at each \(S\) to be assigned to their
individual owners, so it gives nested owner paths through rank two. What it
does not do is turn those chosen paths into same-start flags of one literal
exact wreath factor.

### Theorem 3.2 — balanced core plus injective residual through rank two

For \(m\ge37\), there are a set \(R_2\subseteq V_2\) of size \(r\), an
injective inclusion matching

\[
 H_1\longrightarrow R_2,
 \tag{3.7}
\]

and an integral flow of the \(N_1\) frozen core copies, one starting at
each member of \(V_1\), whose rank-two load is one or two and is exactly one
on every member of \(R_2\). Consequently, sending the \(E\)-copy at
\(S\in H_1\) to its matched member of \(R_2\) makes the combined rank-two
load balanced.

#### Proof

The proof of Theorem 3.1 gives \(r\le T_0\) for \(m\ge37\). The
Kruskal--Katona estimate used there therefore gives

\[
 |\partial\mathcal D|\ge|\mathcal D|
 \qquad(\mathcal D\subseteq H_1).
\]

Hall supplies (3.7).

Now give every parent in \(V_1\) supply one. Give every child lower
capacity one, upper capacity one on \(R_2\), and upper capacity two off
\(R_2\). The lower Gale cuts are again automatic. For a parent family
\(\mathcal P\), put \(t=|\mathcal P|\) and
\(s=|\partial\mathcal P|\). Its available child capacity is

\[
 2s-|R_2\cap\partial\mathcal P|
 \ge2s-\min\{s,r\}.
 \tag{3.8}
\]

If \(t\le T_0\), then \(s\ge t\). When \(s\le r\), the right side of
(3.8) equals \(s\ge t\); when \(s\ge r\), it is at least
\(s\ge t\). If \(t\ge T_0\), equations (3.5)--(3.6) give

\[
 2s-r\ge t.
\]

Thus every upper Gale cut holds, and integrality gives the core flow.

Its total mass is \(N_1\). Since every child has load one or two, exactly

\[
 \delta=N_1-N_2
\]

children have load two; none lies in \(R_2\). Adding the injective residual
puts load two on all \(r\) members of \(R_2\). The combined number of high
children is therefore

\[
 \delta+r=(N_1-N_2)+(W-N_1)=W-N_2=\rho_2,
\]

which is exactly the balanced rank-two quota. \(\square\)

## 4. Exact test for the literal cycle-induced second target

Use the natural two-level flag

\[
 X_i\supset S_i\supset S_{i-1}\cap S_i.
 \tag{4.1}
\]

Define

\[
 h(T)=|\{i:S_{i-1}\cap S_i=T\}|,
 \qquad T\in V_2.
 \tag{4.2}
\]

The sets \(S_{i-1}\) and \(S_i\) are distinct \((m-1)\)-facets of a
middle set, so their intersection has size \(m-2\). Thus (4.1) is an
individual nested flag and its frozen rank-two load is exactly \(h\).

For \(m\ge8\), write a balanced rank-two vector as

\[
 b_2(T)=1+\mathbf1_{H_2}(T),\qquad |H_2|=\rho_2=W-N_2.
 \tag{4.3}
\]

Let

\[
 x_j=|\{T\in V_2:h(T)=j\}|.
\]

### Proposition 4.1

There is a balanced vector (4.3) satisfying the survival inequalities
\(h(T)\le b_2(T)\) for every \(T\) if and only if

\[
 \boxed{
 \max_T h(T)\le2,
 \qquad x_0\le r.}
 \tag{4.4}
\]

#### Proof

The first condition is forced by \(b_2\le2\). Assume it. Since

\[
 \sum_T h(T)=N_1,
\]

one has

\[
 x_2-x_0=N_1-N_2=:\delta.
 \tag{4.5}
\]

Every target counted by \(x_2\) must belong to \(H_2\). Also

\[
 \rho_2=W-N_2=r+\delta.
 \tag{4.6}
\]

Therefore all mandatory high targets fit if and only if

\[
 x_2\le\rho_2
 \quad\Longleftrightarrow\quad
 x_0+\delta\le r+\delta
 \quad\Longleftrightarrow\quad
 x_0\le r.
\]

When this holds, put every double target in \(H_2\) and choose the remaining
\(r-x_0\) high positions among the zero and single targets. There are enough
positions because \(\rho_2<N_2\). This proves sufficiency. \(\square\)

Conditional on (4.4), choose such an \(H_2\). The residual multiplicities
at the two adjacent ranks are

\[
 r_1(S)=\mathbf1_{H_1}(S),
 \qquad
 r_2(T)=1+\mathbf1_{H_2}(T)-h(T).
 \tag{4.7}
\]

Consequently the exact residual crossing condition is

\[
 \boxed{
 |\mathcal A|+|H_2\cap\mathcal A|-h(\mathcal A)
 \le |H_1\cap N_2(\mathcal A)|
 \quad(\mathcal A\subseteq V_2).}
 \tag{4.8}
\]

This is Hall's theorem applied to the actual residual parent copies, which
occur once at the members of \(H_1\). In particular:

* if \(h(T)\ge3\), the singleton survival cut fails;
* if \(x_0>r\), there are too many mandatory double targets, so a singleton
  survival cut again fails for every choice of \(H_2\);
* after survival, any family violating (4.8) is the first exact crossing
  countercut.

The saturating-cycle theorem asserts neither (4.4) nor (4.8). Thus the
literal cycle-induced continuation is not established even at rank two,
although Theorem 3.1 proves that a nonliteral abstract rank-two rerouting is
always available.

## 5. Exact general crossing identity and scope

Let \(u_q(T)\) be the load of any proposed frozen flags of the owners in
\(U\), and put

\[
 r_q=b_q-u_q.
\]

For every child family \(\mathcal A\subseteq V_q\), frozen nestedness gives

\[
 |\mathcal C_q(\mathcal A)\setminus E|
 =u_{q-1}(N_q(\mathcal A))-u_q(\mathcal A).
 \tag{5.1}
\]

Subtracting this from the exact balanced collar yields

\[
 \boxed{
 \kappa_q^b(\mathcal A)
 -|\mathcal C_q(\mathcal A)\setminus E|
 =r_{q-1}(N_q(\mathcal A))-r_q(\mathcal A).}
 \tag{5.2}
\]

Thus no containment-shadow estimate for \(E\) alone can replace the
residual family inequalities: the frozen multiplicities \(u_q\) determine
the capacity which remains.

If the same set \(E\) passed (5.2) through
\(K=\lceil A\sqrt m\rceil\), its monotone-release cost would satisfy

\[
 \sum_{q=1}^K\frac{|E|}{c_q}
 \le K|E|=O_A(W/\sqrt m)=o(W).
\]

The present theorem proves this exact program at transition one and proves
an abstract, noncyclic continuation at transition two. It neither provides
a tight-wreath lift of (1.1) nor controls the literal multiplicities and
family cuts beyond rank one. Accordingly it does not prove
\(\mathrm{MR}_A\), \(\mathrm{CA}_A\), or the constant-one conjecture.

## 6. General balanced-core/injective-residual induction and its first mixed cut

There is an exact continuation of Theorem 3.2 throughout the range in which
both the core and full averages lie strictly between one and two. Put

\[
 \alpha_j=\frac{N_1}{N_j},\qquad
 \lambda_j=\frac W{N_j}.
\]

For \(j=O(\log m)\), one has

\[
 1\le\alpha_j<\lambda_j<2
 \tag{6.1}
\]

for all sufficiently large \(m\). A balanced \(N_1\)-mass core at rank
\(j\) then has load one or two, with high set \(C_j\) of exact size

\[
 |C_j|=N_1-N_j.                                  \tag{6.2}
\]

An injective residual has a target set \(R_j\) of exact size

\[
 |R_j|=r=W-N_1.                                  \tag{6.3}
\]

If \(C_j\cap R_j=\varnothing\), their sum is balanced, because its high
set is their disjoint union and

\[
 |C_j|+|R_j|=(N_1-N_j)+(W-N_1)=W-N_j.            \tag{6.4}
\]

Fix a transition \(q\ge2\). Suppose \(C_{q-1},R_{q-1}\subseteq V_{q-1}\)
are disjoint and have the sizes (6.2)--(6.3). Choose an injective inclusion
matching

\[
 R_{q-1}\longrightarrow R_q\subseteq V_q,
 \qquad |R_q|=r.                                 \tag{6.5}
\]

The core parent supply is

\[
 a(S)=1+\mathbf1_{C_{q-1}}(S).
 \tag{6.6}
\]

At the child rank impose lower capacity one everywhere, upper capacity one
on \(R_q\), and upper capacity two off \(R_q\).

### Theorem 6.1 — exact one-step coupled cut

Under (6.1), the balanced core and injective residual extend across
transition \(q\), for the chosen matching (6.5), if and only if

\[
 \boxed{
 |\mathcal P|+|C_{q-1}\cap\mathcal P|
 \le
 2|\partial\mathcal P|-|R_q\cap\partial\mathcal P|
 \quad(\mathcal P\subseteq V_{q-1}).}
 \tag{6.7}
\]

#### Proof

The upper Gale cut for \(\mathcal P\) is exactly (6.7), because the total
capacity of its child neighborhood is two per child, less one for every
member of \(R_q\). The lower Gale cut for a child family \(\mathcal A\) is

\[
 |\mathcal A|
 \le |N_q(\mathcal A)|
    +|C_{q-1}\cap N_q(\mathcal A)|.
\]

It is automatic from normalized matching, which gives
\(|N_q(\mathcal A)|\ge|\mathcal A|\) below the middle rank. Thus (6.7)
is necessary and sufficient. Integral capacities give an integral core
flow.

Its child loads are one or two and sum to \(N_1\); hence exactly
\(N_1-N_q\) children have load two. The imposed upper capacity makes this
new high set \(C_q\) disjoint from \(R_q\). Equations (6.3)--(6.4) then
show that adjoining the residual matching gives the exact full balanced
load. \(\square\)

At \(q=2\), \(C_1=\varnothing\), and Theorem 3.2 proves (6.7) for every
choice of the matched image \(R_2\). At \(q=3\), the term
\(|C_2\cap\mathcal P|\) is present for the first time. Thus (6.7), not an
ordinary root-shadow inequality, is the first genuinely coupled cut in
this induction.

### Proposition 6.2 — residual matchings alone reach half logarithmic depth

Put

\[
 T_q=\binom{2m-2q+1}{m-q+1}.
 \tag{6.8}
\]

If \(r\le T_q\), then every \(r\)-set
\(R_{q-1}\subseteq V_{q-1}\) has an inclusion matching to \(r\) distinct
members of \(V_q\).

#### Proof

For every \(\mathcal D\subseteq R_{q-1}\), write
\(|\mathcal D|=\binom{x}{m-q+1}\). Since
\(|\mathcal D|\le r\le T_q\), one has
\(x\le2(m-q+1)-1\). The Lovasz--Kruskal--Katona bound gives

\[
 |\partial\mathcal D|
 \ge\binom{x}{m-q}
 \ge\binom{x}{m-q+1}
 =|\mathcal D|.
\]

Hall proves the assertion. \(\square\)

Uniformly for \(q=O(\log m)\), the central-binomial estimate gives

\[
 \frac{T_q}{W}=(1+o(1))4^{-q},
 \qquad
 \frac rW=\frac{2}{m+2}.
 \tag{6.9}
\]

Consequently \(r\le T_q\) throughout

\[
 q\le\frac12\log_2m-\omega(1),                  \tag{6.10}
\]

where the approach to the half-logarithmic boundary is one-sided. Thus the
plain SDR part of the induction reaches \((\tfrac12-o(1))\log_2m\).

It does **not** prove (6.7). Taking
\(\mathcal P=C_{q-1}\) in that cut gives the exact requirement

\[
 \boxed{
 |R_q\cap\partial C_{q-1}|
 \le2\bigl(|\partial C_{q-1}|-|C_{q-1}|\bigr).}
 \tag{6.11}
\]

For \(q=O(\log m)\), the high-core size has the expansion

\[
 \frac{|C_{q-1}|}{W}
 =\frac{q(q-1)-2}{m}+O\!\left(\frac{q^4}{m^2}\right).
 \tag{6.12}
\]

Thus the same Kruskal--Katona argument guarantees merely that the right
side of (6.11) is nonnegative while

\[
 4^q q^2=o(m),
 \quad\text{for example}
 \quad
 q\le\frac12\log_2m-\log_2\log m-\omega(1).
 \tag{6.13}
\]

Even in this slightly shorter, still
\((\tfrac12-o(1))\log_2m\) range, it does not keep the chosen residual
image out of the often much smaller shadow surplus. A bound that discards
the placement of
\(R_q\), namely

\[
 |R_q\cap\partial\mathcal P|
 \le\min\{r,|\partial\mathcal P|\},
\]

would require an additive shadow surplus of order \(r\), which the extremal
Kruskal--Katona families need not have. Therefore normalized matching and
ordinary shadow expansion close the residual SDR through (6.10), and keep
the bare core shadow noncontracting through (6.13), but they stop at the
mixed core-high/residual-image cut (6.7), already at transition three.

## 7. The same-floor deep-injectivity cut

Put

\[
 \alpha_q=\frac{N_1}{N_q},\qquad
 \lambda_q=\frac{W}{N_q}.
\]

### Proposition 7.1

Suppose

\[
 \lfloor\alpha_q\rfloor=\lfloor\lambda_q\rfloor=c,
\tag{7.1}
\]

the \(N_1\)-mass core load \(g_q\) and the \(W\)-mass load \(b_q\) are
balanced, and \(g_q\le b_q\) pointwise.  Then

\[
 b_q(T)-g_q(T)\in\{0,1\}
\]

at every target.  Consequently, if this difference is carried by the
owners in (E), then

\[
 \boxed{|\partial_q\mathcal A|\ge|\mathcal A|
 \qquad(\mathcal A\subseteq E).}
\tag{7.2}
\]

#### Proof

Both balanced vectors take values in \(\{c,c+1\}\).  Pointwise domination
makes their difference zero or one, and its total mass is

\[
 \sum_T(b_q(T)-g_q(T))=W-N_1=|E|.
\]

Thus the residual owners occupy distinct depth-\(q\) targets.  The targets
of every subfamily \(\mathcal A\) are distinct members of
\(\partial_q\mathcal A\), proving (7.2). \(\square\)

The known saturation-cycle facet cap does not imply (7.2) at growing
depth.  To see the exact limitation, let

\[
 \ell=\lceil\log_2(m+2)\rceil,
 \qquad |Y|=2m+1-\ell,
 \qquad \mathcal A=\binom Ym.
\tag{7.3}
\]

Then

\[
 \frac{|\mathcal A|}{W}
 =\prod_{j=0}^{\ell-1}
   \frac{m+1-j}{2m+1-j}
 \le2^{-(\ell-1)}
 \le\frac2{m+2}
 =\frac{|E|}{W}.
\tag{7.4}
\]

Every rank-\((m-1)\) set has \(\mathcal A\)-degree either zero or

\[
 |Y|-(m-1)=m+2-\ell\le m,
\tag{7.5}
\]

exactly respecting the pointwise cap proved from the saturating cycle.
Nevertheless,

\[
 \frac{|\partial_\ell\mathcal A|}{|\mathcal A|}
 =\frac{\binom{2m+1-\ell}{m-\ell}}
        {\binom{2m+1-\ell}{m}}
 =\frac{m+1-\ell}{m+1}<1.
\tag{7.6}
\]

Since \(\ell=O(\log m)\), both \(\alpha_\ell\) and \(\lambda_\ell\) lie
in \((1,2)\) for large \(m\), so (7.1) holds with \(c=1\).  The family
(7.3) is not claimed to occur in the actual saturating-cycle leave.  It
proves that the known facet cap and the weaker estimate

\[
 |\partial_q\mathcal A|\ge\frac{N_q}{N_1}|\mathcal A|
\]

cannot establish the balanced-core domination required by (7.2).  New
information about the actual placement of the omitted owners, together
with the mixed cut (6.7), is necessary beyond transition two.
