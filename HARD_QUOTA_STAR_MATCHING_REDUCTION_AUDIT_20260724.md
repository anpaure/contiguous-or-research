# Audit of the hard-quota star-matching reduction

Date: 2026-07-24

Audited source: HARD_QUOTA_STAR_MATCHING_REDUCTION_RAW_20260724.md.

Method: symbolic theorem audit only. No web search, finite search, or solver was used.

## 0. Executive verdict

The proposed reduction has a correct conditional core, but the codegree heuristic does not prove that its hypotheses can be achieved.

The following claims are **valid**:

- the reciprocal quota mass is \(O(\sqrt m)\), in fact \(\Theta(\sqrt m)\);
- a quota-safe core \(G\) inside an exact factor \(F=G\sqcup B\) incurs at most \(n|B|\) overload at each depth;
- the half-\(\ell^1\) formula for \(O_q\) is exact for full-mass load and quota vectors;
- a matching in the **full** wreath hypergraph saturating \(P_v\) is exactly a perfect exact factor;
- the stated unoriented degree and distinct-pair codegree formulas are correct;
- the maximum normalized codegree for two distinct \(P_v\)-vertices is exactly \(2/[m(m+1)]\).

The following corrections are necessary:

1. The pair-codegree formula applies only to distinct vertices, \(1\le d\le m\). At \(d=0\) it overcounts by a factor two.
2. Small \(|B|\) implies MWB only together with quota domination at every depth of a valid common window and with the same \(F,G,B\) throughout that window.
3. “Matching saturating \(P_v\)” must mean a matching in the full hypergraph. A matching of the projected \(P_v\)-traces may collide on \(Q_v\).
4. The \(P_v\)-projection is naturally a two-fold multihypergraph for \(m\ge2\); collapsing it halves its degrees and codegrees but leaves their ratio unchanged.
5. The full wreath hypergraph has maximum normalized codegree \(2/(m+1)=\Theta(m^{-1})\), attained by disjoint middle sets on the \(Q_v\) side or across the \(P_v,Q_v\) sides.
6. The hard lower-rank resources also have \(\Theta(m^{-1})\) correlations already at depth one.
7. The edge size grows from \(m\) in the \(P_v\)-projection to \(2m+1\) in the full hypergraph and to \(n(H+1)\) in the natural \(H\)-depth resource encoding.
8. Consequently, (5) proves regularity, a fractional perfect matching, and small pair correlations on the \(P_v\) projection only. It proves no integral almost-perfect matching rate, no \(Q_v\)-conflict resolution, no quota-safe packing, and no extendible residual.

The strongest proved conclusion is the conditional hard-quota exceptional-completion lemma in item (20).

## 1. Twenty audited statements

### (1) Basic mass identities

**Verdict: VALID.** Let

\[
n=2m+1,\qquad
W=\binom{n}{m},\qquad
N_q=\binom{n}{m-q},\qquad
t_m=\frac Wn.
\]

Then

\[
t_m
=\frac{1}{2m+1}\binom{2m+1}{m}
=\frac{1}{m+1}\binom{2m}{m}
=\operatorname{Cat}_m.
\]

In particular \(t_m\) is an integer and \(W=nt_m\). An exact factor has exactly \(t_m\) wreaths because every wreath support consists of \(n\) middle sets.

### (2) Exact formula for \(\lambda_q\)

**Verdict: VALID.** For \(1\le q\le m-1\),

\[
\lambda_q:=\frac{W}{N_q}
=\frac{(m-q)!(m+q+1)!}{m!(m+1)!}
=\prod_{i=0}^{q-1}\frac{m+2+i}{m-i}.
\]

Equivalently,

\[
\lambda_q
=\prod_{i=0}^{q-1}
\left(1+\frac{2(i+1)}{m-i}\right).
\]

### (3) Passing from \(\lambda_q\) to the integer floor \(c_q\)

**Verdict: VALID.** Since \(\lambda_q\ge1\) and

\[
\lfloor x\rfloor\ge \frac x2\qquad(x\ge1),
\]

one has

\[
c_q=\lfloor\lambda_q\rfloor\ge\frac{\lambda_q}{2},
\qquad
\frac1{c_q}\le\frac2{\lambda_q}.
\]

There is no missing factor in this step.

### (4) Gaussian lower bound for \(\log\lambda_q\)

**Verdict: VALID, WITH A SLIGHTLY STRONGER CONSTANT.** Put

\[
x_i=\frac{2(i+1)}{m-i}.
\]

The inequality

\[
\log(1+x)\ge\frac{x}{1+x}\qquad(x\ge0)
\]

gives

\[
\log\lambda_q
\ge
\sum_{i=0}^{q-1}\frac{2(i+1)}{m+i+2}.
\]

Because \(i\le m-2\), one has \(m+i+2\le2m\), and therefore

\[
\boxed{
\log\lambda_q\ge\frac{q(q+1)}{2m}.
}
\]

The raw bound \(q(q+1)/(2m+1)\) is thus correct but slightly weaker.

### (5) Reciprocal quota mass

**Verdict: VALID.** From (3) and (4),

\[
\begin{aligned}
S_m
&:=\sum_{q=1}^{m-1}\frac1{c_q}\\
&\le
2\sum_{q=1}^{m-1}
\exp\!\left(-\frac{q(q+1)}{2m}\right)\\
&\le
2\sum_{q=1}^{\infty}e^{-q^2/(2m)}\\
&\le
2\int_0^\infty e^{-x^2/(2m)}\,dx
=\sqrt{2\pi m}.
\end{aligned}
\]

Thus

\[
\boxed{
\sum_{q=1}^{m-1}\frac1{c_q}=O(\sqrt m)
}
\]

with an absolute constant.

The order is sharp. Uniformly for \(q\le R\sqrt m\), with fixed \(R\),

\[
\log\lambda_q
=\frac{q(q+1)}m+O_R(m^{-1/2}).
\]

The floor discontinuities occur at only finitely many points on every compact rescaled interval, and the preceding Gaussian bound controls the tail. Hence

\[
\boxed{
S_m=(I+o(1))\sqrt m,
\qquad
I=\int_0^\infty
\frac{dx}{\lfloor e^{x^2}\rfloor}.
}
\]

Equivalently,

\[
I=
\sum_{k\ge1}
\frac{\sqrt{\log(k+1)}-\sqrt{\log k}}{k},
\qquad
\frac{\sqrt\pi}{2}\le I\le\sqrt\pi.
\]

Only the upper bound is needed for the reduction.

### (6) Occurrence mass of an exceptional family

**Verdict: VALID.** Let an exact factor split as

\[
F=G\sqcup B,
\qquad b:=|B|.
\]

At each depth \(q\), every wreath contributes its \(n\) cyclic intervals of length \(m-q\). These intervals are distinct for \(q\le m-1\). Consequently

\[
\sum_S\mu_q^B(S)=nb,
\qquad
\sum_S\mu_q^G(S)=W-nb.
\]

This uses the same split \(F=G\sqcup B\) at every controlled depth.

### (7) Exact exceptional-family charging

**Verdict: VALID.** Suppose \(b_q\) is a balanced full-mass quota vector,

\[
b_q(S)\in\{c_q,c_q+1\},
\qquad
\sum_Sb_q(S)=W,
\]

and

\[
\mu_q^G(S)\le b_q(S)\qquad\text{for every }S.
\]

Put \(s_q=b_q-\mu_q^G\ge0\). Then

\[
\sum_Ss_q(S)=nb
\]

and

\[
\mu_q^F-b_q=\mu_q^B-s_q.
\]

Therefore

\[
\sum_S(\mu_q^F(S)-b_q(S))_+
\le
\sum_S\mu_q^B(S)
=nb.
\]

Taking the minimum over balanced quotas yields

\[
\boxed{O_q(F)\le nb.}
\]

There is no additional factor two: positive discrepancy already equals half the \(\ell^1\) discrepancy because \(\mu_q^F\) and \(b_q\) have the same total mass.

### (8) Weighted exceptional charge

**Verdict: VALID.** For every \(H\le m-1\) on which the quota domination in (7) holds,

\[
\begin{aligned}
\sum_{q\le H}\frac{O_q(F)}{c_q}
&\le
nb\sum_{q\le H}\frac1{c_q}\\
&\le nb\,S_m\\
&\le nb\sqrt{2\pi m}\\
&=
W\,\frac b{t_m}\sqrt{2\pi m}.
\end{aligned}
\]

Thus the raw estimate

\[
O\!\left(W\sqrt m\,\frac{|B|}{t_m}\right)
\]

is correctly normalized.

### (9) Exact size thresholds and quantifiers for MWB

**Verdict: CORRECTED IN SCOPE.** Under the quota hypothesis,

\[
b=o(t_m/\sqrt m)
\quad\Longrightarrow\quad
\sum_{q\le H}\frac{O_q(F)}{c_q}=o(W),
\]

and

\[
b\le C\,\frac{t_m}{m}
\quad\Longrightarrow\quad
\sum_{q\le H}\frac{O_q(F)}{c_q}
\le C\sqrt{2\pi}\,\frac W{\sqrt m}.
\]

Small \(b\) by itself proves nothing about overload; it must be coupled to the domination \(\mu_q^G\le b_q\).

To conclude MWB, the quota hypothesis and one of the displayed exceptional-size bounds must hold with one of the following quantifier patterns:

1. one sequence \(H(m)=\sqrt m\,\omega(m)\), with \(\omega(m)\to\infty\) and \(H=o(m)\), and one common \(F_m,G_m,B_m\) satisfying the quota condition for every \(1\le q\le H(m)\); or
2. for every fixed \(A\), one common witness satisfying the quota condition simultaneously for every \(1\le q\le\lceil A\sqrt m\rceil\), followed by the standard diagonalization.

A construction for only one fixed \(A\) does not prove MWB. The quota vectors may be chosen independently at different depths because this is an unlabelled overload reduction, but the factor and its split must be common across all depths in the window. No labelled common-owner synchronization follows.

### (10) Half-\(\ell^1\) characterization of \(O_q\)

**Verdict: VALID WITH FULL-MASS QUANTIFIERS.** Let \(\mu\) be a nonnegative integer load vector on \(N_q\) targets with

\[
\sum_S\mu(S)=W.
\]

Let \(\mathcal B_q\) be the family of all vectors

\[
b(S)\in\{c_q,c_q+1\},
\qquad
\sum_Sb(S)=W.
\]

Equivalently, exactly

\[
\rho_q:=W-c_qN_q
\]

entries of \(b\) equal \(c_q+1\). For each \(b\in\mathcal B_q\), equality of total masses gives

\[
\sum_S(\mu(S)-b(S))_+
=\frac12\|\mu-b\|_1.
\]

Minimizing yields

\[
\boxed{
O_q(\mu)
=\frac12\min_{b\in\mathcal B_q}\|\mu-b\|_1.
}
\]

For an intrinsic formula put \(\delta_S=\mu(S)-c_q\) and

\[
D^-=\sum_S(-\delta_S)_+,
\qquad
D^+=\sum_S(\delta_S-1)_+.
\]

If \(T=\sum_{\delta_S\ge1}\delta_S\) and
\(a=\#\{S:\delta_S\ge1\}\), then

\[
D^-=T-\rho_q,\qquad D^+=T-a,
\]

and assigning high quotas to as many positive cells as possible gives

\[
O_q=T-\min(\rho_q,a)=\max(D^-,D^+).
\]

The half-\(\ell^1\) identity is not an identity for the partial load \(\mu_q^G\), whose total is \(W-nb\).

For later use, a balanced quota dominating a partial integer vector \(\eta\) exists if and only if

\[
\max_S\eta(S)\le c_q+1,
\qquad
\#\{S:\eta(S)=c_q+1\}\le\rho_q.
\]

This exact ceiling-count condition is not detected by the \(P_v\)-codegree calculation.

### (11) Exact sizes of the two star sides

**Verdict: VALID.** Fix \(v\in[n]\) and define

\[
P_v=\{A\in\tbinom{[n]}m:v\in A\},
\qquad
Q_v=\{A\in\tbinom{[n]}m:v\notin A\}.
\]

Then

\[
|P_v|
=\binom{2m}{m-1}
=m\,t_m,
\]

\[
|Q_v|
=\binom{2m}{m}
=(m+1)t_m.
\]

Their sum is \(nt_m=W\).

### (12) Star profile of one wreath

**Verdict: VALID.** In a cyclic order of \(n\) coordinates, a fixed coordinate \(v\) lies in exactly \(m\) of the \(n\) cyclic length-\(m\) intervals: the start may occupy any of the \(m\) positions ending at \(v\). Hence every wreath support contains exactly

\[
m\text{ vertices of }P_v
\quad\text{and}\quad
m+1\text{ vertices of }Q_v.
\]

This statement is independent of the orientation of the cyclic order.

### (13) Exact star-saturation/perfect-factor equivalence

**Verdict: VALID, WITH “FULL” ESSENTIAL.** Let \(M\) be a matching in the full wreath-support hypergraph; thus its supports are disjoint on both \(P_v\) and \(Q_v\). If \(M\) saturates \(P_v\), then

\[
|M|=\frac{|P_v|}{m}=t_m.
\]

It covers

\[
n|M|=nt_m=W
\]

distinct middle vertices, so it covers the entire middle layer and is a perfect exact factor.

Conversely, every perfect exact factor is a full-hypergraph matching and saturates \(P_v\). Therefore

\[
\boxed{
\text{full wreath matching saturating }P_v
\iff
\text{perfect exact factor}.
}
\]

More precisely, suppose only that the \(P_v\)-traces of \(t_m\) selected supports partition \(P_v\). Their \(Q_v\)-traces contain exactly

\[
(m+1)t_m=|Q_v|
\]

incidences. The selected supports form a perfect factor if and only if these \(Q_v\)-incidences are injective, equivalently if and only if they partition \(Q_v\). One \(Q_v\)-collision necessarily creates a \(Q_v\)-hole.

### (14) Unoriented-support normalization

**Verdict: VALID.** For \(m\ge1\), a wreath support determines its cyclic order up to reversal. Indeed, on the \(n\) middle windows in a support, Johnson-distance-one adjacency is exactly the cycle of consecutive starts. The set differences along that cycle recover the coordinate order up to reversing and rotating it.

Thus the number of unoriented wreath supports is

\[
|\mathcal E_m|=\frac{(n-1)!}{2}.
\]

Each support has two oriented cyclic-order representatives modulo rotation, related by reversal, or \(2n\) linear representatives. All counts below use the unoriented-support convention. Counting oriented cycles would multiply every degree and codegree by two and would leave every normalized ratio unchanged.

Because reversal preserves the family of cyclic intervals at every length, an unoriented support also determines all unlabelled lower-rank histograms used in the hard quotas.

### (15) Single-vertex degree

**Verdict: VALID.** Fix a middle set \(A\). In an oriented cyclic order containing \(A\) as a length-\(m\) interval, order the \(m\) elements of \(A\) internally in \(m!\) ways, collapse \(A\) to one block, and cyclically order that block with the \(m+1\) complementary labels in \((m+1)!\) ways. Hence the oriented degree is

\[
D_m^{\rm or}=m!(m+1)!.
\]

Reversal acts freely and pairs these cycles, so the unoriented degree is

\[
\boxed{
D_m=\frac{m!(m+1)!}{2}.
}
\]

The incidence double count

\[
|\mathcal E_m|\,n=W D_m
\]

gives the same value.

### (16) Distinct-pair codegree

**Verdict: VALID FOR \(1\le d\le m\); CORRECTED AT \(d=0\).** Let \(A\ne B\) be middle sets and

\[
|A\setminus B|=|B\setminus A|=d.
\]

Partition the coordinates into

\[
X=A\setminus B,\quad
I=A\cap B,\quad
Y=B\setminus A,\quad
Z=[n]\setminus(A\cup B),
\]

of sizes

\[
d,\quad m-d,\quad d,\quad m+1-d.
\]

An oriented cyclic order containing both \(A\) and \(B\) has one of the two reverse block patterns

\[
X,I,Y,Z
\qquad\text{or}\qquad
X,Z,Y,I,
\]

with arbitrary internal order in each block. Thus the oriented count is

\[
2d!^2(m-d)!(m+1-d)!.
\]

After quotienting by reversal,

\[
\boxed{
D_m(A,B)
=d!^2(m-d)!(m+1-d)!,
\qquad 1\le d\le m.
}
\]

Consequently

\[
\boxed{
\frac{D_m(A,B)}{D_m}
=
\frac{2}
{\binom md\binom{m+1}d}.
}
\]

At \(d=0\), \(A=B\) and the actual codegree is

\[
D_m(A,A)=D_m.
\]

The factorial expression would give \(m!(m+1)!=2D_m\), because the two block patterns coincide. The raw formula must explicitly exclude \(d=0\).

An independent check is useful: within a support containing \(A\), exactly two other windows lie at each set-distance \(d=1,\ldots,m\), while the number of middle sets at distance \(d\) from \(A\) is
\(\binom md\binom{m+1}d\). Double counting these incidences gives the same ratio.

### (17) \(P_v\)-codegree versus full-hypergraph codegree

**Verdict: RAW (5) VALID AND EXACT; ITS SCOPE IS ONLY \(P_v\).** If \(A,B\in P_v\) are distinct, then they share \(v\), so

\[
1\le d\le m-1.
\]

On this range

\[
\binom md\ge m,
\qquad
\binom{m+1}d\ge m+1,
\]

with simultaneous equality at \(d=1\). Therefore, for \(m\ge2\),

\[
\boxed{
\max_{A\ne B\in P_v}
\frac{D_m(A,B)}{D_m}
=\frac{2}{m(m+1)}.
}
\]

The maximum codegree itself is

\[
(m-1)!m!,
\]

attained at \(d=1\).

The boundary ledger is

\[
\begin{array}{c|c|c}
d&D_m(A,B)&D_m(A,B)/D_m\\ \hline
0&D_m&1\\
1&(m-1)!m!&2/[m(m+1)]\\
m-1&2((m-1)!)^2&4/[m^2(m+1)]\\
m&m!^2&2/(m+1).
\end{array}
\]

The last line is decisive. Distinct disjoint middle sets have \(d=m\), so the maximum normalized codegree in the **full** wreath hypergraph is

\[
\boxed{
\max_{A\ne B}
\frac{D_m(A,B)}{D_m}
=\frac{2}{m+1}
=\Theta(m^{-1}).
}
\]

Such pairs occur across \(P_v,Q_v\): every \(A\in P_v\) has \(m+1\) disjoint \(Q_v\)-sets. They also occur inside \(Q_v\): complementary \(m\)-sets in \([n]\setminus\{v\}\) are disjoint. Thus retaining the \(Q_v\) conflicts loses one power of \(m\) from the normalized codegree.

### (18) Exact force of the \(P_v\)-projection

**Verdict: FRACTIONAL REGULARITY ONLY; NO INTEGRAL MATCHING CONCLUSION.** Let \(\mathcal H_{P_v}\) be the candidate-indexed multihypergraph on \(P_v\), with one \(m\)-edge \(E\cap P_v\) for every full wreath support \(E\). It is exactly \(D_m\)-regular, has \(t_mD_m\) candidate edges, and has maximum normalized distinct-pair codegree \(2/[m(m+1)]\). The weights

\[
x_E=\frac1{D_m}
\]

therefore form a fractional perfect matching of \(\mathcal H_{P_v}\).

For \(m\ge2\), the projection to unordered \(P_v\)-traces is exactly two-to-one. To see this, list the \(m\) \(v\)-containing windows as

\[
T_0,\ldots,T_{m-1}
\]

in start order. Their induced Johnson graph is a path, so the unordered trace determines this order up to reversal. If

\[
r_i=T_{i-1}\setminus T_i,
\qquad
s_i=T_i\setminus T_{i-1},
\]

then the trace determines the cyclic core

\[
(r_1,\ldots,r_{m-1},v,s_1,\ldots,s_{m-1})
\]

up to reversal. Exactly two coordinates \(x,y\) are absent from the trace union, and they must fill the complementary two-position gap. The two orders \(xy\) and \(yx\) give the two distinct full supports.

Consequently, after collapsing parallel \(P_v\)-traces,

\[
|\mathcal E(\mathcal H_{P_v}^{\rm simple})|
=\frac{(n-1)!}{4},
\qquad
\deg=\frac{D_m}{2},
\qquad
\operatorname{codeg}(A,B)=\frac{D_m(A,B)}2.
\]

The normalized ratio is unchanged. Lifting a matching of simple traces requires a global binary choice between the two full supports above each trace, with all chosen \(Q_v\)-parts disjoint.

Thus the unconditional content of (5) is:

- exact regularity of the \(m\)-uniform \(P_v\)-projection;
- a uniform fractional perfect matching;
- \(O(m^{-2})\) pair correlations on that projection.

The codegree calculation does not by itself yield an integral matching. (An uncapacitated integral perfect matching is already known from exact-factor existence, but that fact supplies no hard-quota compatibility.) In particular, a theorem for fixed uniformity cannot be invoked without a version uniform as the edge size \(m\) grows.

It also supplies no quantitative leave. If a full matching \(G\) has \(t_m-b\) edges, its uncovered \(P_v\)-mass is

\[
R_P=mb.
\]

The threshold \(b=o(t_m/\sqrt m)\) requires

\[
\frac{R_P}{|P_v|}=o(m^{-1/2}),
\]

and the convenient threshold \(b=O(t_m/m)\) requires

\[
R_P=O(t_m)=O(|P_v|/m).
\]

A merely qualitative \(1-o(1)\) almost-matching would not supply either required rate.

### (19) \(Q_v\), hard quotas, and growing resource rank

**Verdict: THESE ARE GENUINE UNRESOLVED CONSTRAINTS.**

First, a \(P_v\)-matching can have arbitrary collisions on \(Q_v\). The full matching problem has the larger normalized codegree \(2/(m+1)\) from (17). The equality of total \(Q_v\)-incidence with \(|Q_v|\) does not help unless injectivity is proved.

Second, the lower-rank resource system has its own exact degree and codegree ledger. Put

\[
r=m-q.
\]

For a fixed \(r\)-target \(S\), collapsing \(S\) to one cyclic block shows that the number of unoriented wreaths in which \(S\) is a cyclic \(r\)-window is

\[
\boxed{
D_q^\downarrow
=\frac{r!(n-r)!}{2}
=\frac{(m-q)!(m+q+1)!}{2}
=\lambda_qD_m.
}
\]

Every wreath uses \(n\) distinct resources at this depth.

If \(S\subset A\), with \(|A|=m\) and \(|S|=m-q\), then, conditional on \(A\) being a middle interval, \(S\) is an interval exactly when its elements form one block in the internal linear order of \(A\). Therefore

\[
\boxed{
\frac{\operatorname{codeg}(A,S)}{D_m}
=\frac{(m-q)!(q+1)!}{m!}
=\frac{q+1}{\binom mq}.
}
\]

At \(q=1\), this is exactly

\[
\frac2m.
\]

Likewise, if \(T=S\setminus\{x\}\), then conditional on \(S\) being an interval, \(T\) is an interval precisely when \(x\) is one of its two endpoints. For \(r\ge2\),

\[
\boxed{
\frac{\operatorname{codeg}(S,T)}
{\deg(S)}
=\frac2r.
}
\]

Thus the quota-augmented system has explicit \(\Theta(m^{-1})\) nested correlations throughout a shallow window. It does not inherit the \(P_v\)-pair scale \(O(m^{-2})\).

Third, uniform candidate weights do not solve the hard quota relaxation. Weighting every full wreath by \(1/D_m\) gives load one on every middle vertex but load

\[
\frac{D_q^\downarrow}{D_m}=\lambda_q
\]

on every \(q\)-target. If \(\lambda_q\notin\mathbb Z\), a balanced hard vector has some entries \(c_q<\lambda_q\), so the uniform fractional vector violates all of those floor capacities. Since the total lower-rank load equals the total quota, any **full-mass** fractional vector (equivalently, one of total candidate weight \(t_m\)) dominated by \(b_q\) must in fact meet \(b_q\) exactly. Nonuniform simultaneous rounding is essential.

At depth one, for \(m\ge3\),

\[
\lambda_1=\frac{m+2}{m},
\qquad
c_1=1,
\qquad
\rho_1=W-N_1=\frac{2W}{m+2}.
\]

The hard capacities are therefore \(1\) or \(2\), with only a small prescribed number of high slots. This is the “mean-one first shadow” obstruction in exact form.

Finally, the edge rank grows. The projected star system is \(m\)-uniform; the full wreath hypergraph is \(n=2m+1\)-uniform. Encoding the middle matching resources and \(H\) lower-rank quota classes gives each wreath

\[
n(H+1)
\]

resource incidences. For \(H=\Theta(\sqrt m)\), this is
\(\Theta(m^{3/2})\). Splitting a capacity into clones does not remove the need to assign all of these incidences and adds a global slot-allocation choice.

Accordingly, no standard fixed-uniformity nibble theorem follows from (5). A valid theorem would have to be uniform in the growing edge rank, control the \(Q_v\) conflict system, honor every hard quota, achieve leave \(o(|P_v|/\sqrt m)\) (or the stronger \(O(|P_v|/m)\)), and leave a residual that is exactly wreath-factorable.

### (20) Clean final lemma

The following is the exact reduction proved by the raw argument.

**Hard-quota exceptional-completion lemma.** Let \(m\ge2\) and
\(1\le H\le m-1\). Suppose:

1. \(G\) is a matching in the full unoriented wreath-support hypergraph with
   \[
   |G|=t_m-b;
   \]
2. the uncovered middle vertices admit a partition into \(b\) full wreath supports \(B\), so
   \[
   F:=G\sqcup B
   \]
   is an exact factor;
3. for every \(1\le q\le H\), there is a balanced full-mass quota vector \(b_q\) such that
   \[
   \mu_q^G(S)\le b_q(S)
   \qquad\text{for every target }S.
   \]

Then, for every \(q\le H\),

\[
\boxed{O_q(F)\le nb,}
\]

and

\[
\boxed{
\sum_{q\le H}\frac{O_q(F)}{c_q}
\le
nb\sum_{q=1}^{m-1}\frac1{c_q}
\le
nb\sqrt{2\pi m}.
}
\]

Consequently,

\[
b=o(t_m/\sqrt m)
\quad\Longrightarrow\quad
\sum_{q\le H}\frac{O_q(F)}{c_q}=o(W),
\]

while

\[
b=O(t_m/m)
\quad\Longrightarrow\quad
\sum_{q\le H}\frac{O_q(F)}{c_q}
=O(W/\sqrt m).
\]

If these hypotheses together with
\(b=o(t_m/\sqrt m)\) (in particular, \(b=O_A(t_m/m)\)) are obtained on every fixed Gaussian window, with the same objects throughout each window, diagonalization proves MWB. The lemma is unlabelled and does not produce a common nested resolution.

If \(G\) itself saturates \(P_v\), then item (13) forces \(b=0\) and \(G=F\) to be a perfect factor. The quota inequalities then compare two full-mass vectors:

\[
\mu_q^F\le b_q,
\qquad
\sum_S\mu_q^F(S)=\sum_Sb_q(S)=W,
\]

so in fact

\[
\mu_q^F=b_q
\]

at every controlled depth and the overload is zero.

For \(b>0\), a full matching \(G\) automatically leaves exactly

\[
mb\text{ vertices of }P_v
\quad\text{and}\quad
(m+1)b\text{ vertices of }Q_v,
\]

but these cardinalities do not imply that the residual is a union of \(b\) wreaths. Exact residual completion is a separate hypothesis.

## 2. Final logical status

The raw note establishes a correct sufficient reduction:

\[
\boxed{
\text{quota-safe extendible core}
+\text{ sufficiently small exact completion}
\Longrightarrow
\text{MWB}.
}
\]

It does not establish the antecedent. The degree and \(P_v\)-codegree formulas provide useful local data, but their strongest immediate consequence is a regular fractional star matching. The missing theorem must simultaneously provide:

1. full \(P_v\)- and \(Q_v\)-disjointness;
2. a quantitative leave at most \(o(t_m/\sqrt m)\), preferably \(O(t_m/m)\);
3. all shallow hard-quota capacities;
4. an exactly wreath-factorable residual.

The \(O(m^{-2})\) \(P_v\)-codegree does not, by itself, imply any of these four requirements. The proposal is therefore a valid conditional reduction and a plausible theorem target, not a proof of MWB and not yet an almost-perfect matching theorem.
