# PBBS per-cut literal seams: the linear dominance-staircase theorem

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Exact result

Let

\[
X_{i+1}=X_i-\{r_i\}+\{a_i\},
\qquad X_i\in\binom{\Omega}{m+1},
\tag{0.1}
\]

be a cyclic Johnson walk, and cut it between \(X_{-1}\) and \(X_0\).
Assume

\[
1\le H,\qquad 2H\le m+1.
\tag{0.2}
\]

For \(1\le q\le H\) and \(1\le a\le q\), define the genuinely
cut-crossing lower and upper targets

\[
S_{q,a}
=\bigcap_{j=-a}^{q-a}X_j,
\qquad
U_{q,a}
=\bigcup_{j=-a}^{q-a}X_j.
\tag{0.3}
\]

The window has \(q+1\) owners and \(q\) transitions. Call \(S_{q,a}\)
floor-correct when

\[
|S_{q,a}|=m+1-q.
\tag{0.4}
\]

### Theorem Z13.1 -- linear literal cut chart

There is an explicit nonzero literal word of length

\[
\boxed{4H-1}
\tag{0.5}
\]

which realizes, as contiguous ORs,

1. every floor-correct \(S_{q,a}\) in (0.3); and
2. every \(U_{q,a}\) in (0.3).

The lower block has \(2H-1\) letters and is a Pareto dominance
staircase of actual owner intersections. The upper block is simply the
\(2H\)-owner word

\[
X_{-H},X_{-H+1},\ldots,X_{H-1}.
\tag{0.6}
\]

Thus no endpoint-throughput or interval-incidence lower bound of order
\(\Omega(H^2)\) is possible in this direct literal model. The old
\(\Theta(H^2)\) cost came from appending destroyed targets one at a time.

For the complement-projected PBBS cycle factor, if an active cycle of
length \(\ell\) is cut at \(J\ge1\) residence-transversal edges, its
complete path-erosion plus cut-repair word has length at most

\[
\boxed{\ell+(5H-1)J.}
\tag{0.7}
\]

Consequently, with

\[
W=\binom{2m+1}{m},\qquad
B_m=\operatorname{Cat}_m=\frac{W}{2m+1},
\tag{0.8}
\]

the global central-band word satisfies

\[
\boxed{
L_H\le
W+2HB_m+2(5H-1)\nu_H(P_m).
}
\tag{0.9}
\]

Hence the still-unproved residence estimate

\[
\nu_H(P_m)=O(B_m)
\tag{0.10}
\]

means, along the chosen sequence \(H=H(m)\), that
\(\nu_H(P_m)\le K B_m\) for one constant \(K\) independent of \(m\).
Whenever this holds with \(H=o(m)\), it gives \(L_H=W+o(W)\). The deterministic
literal-seam gate is closed; (0.10), not a quadratic per-cut repair, is
the remaining PBBS input in this architecture.

---

## 1. Two-sided run extents at the cut

Put

\[
C=X_{-1}\cap X_0.
\tag{1.1}
\]

Since \(X_{-1}\) and \(X_0\) are adjacent rank-\((m+1)\) owners,

\[
|C|=m.
\tag{1.2}
\]

For \(1\le s,t\le H\), write

\[
P_{s,t}
=\bigcap_{i=-s}^{t-1}X_i.
\tag{1.3}
\]

The translation to (0.3) is

\[
s=a,\qquad t=q-a+1,
\qquad S_{q,a}=P_{a,q-a+1}.
\tag{1.4}
\]

For every \(x\in C\), define its capped consecutive positive-run extents
through the cut:

\[
\begin{aligned}
u_x&=\max\{u\in[H]:
x\in X_{-u}\cap\cdots\cap X_{-1}\},\\
v_x&=\max\{v\in[H]:
x\in X_0\cap\cdots\cap X_{v-1}\}.
\end{aligned}
\tag{1.5}
\]

Let

\[
p_x=(u_x,v_x)\in[H]^2,
\qquad
\mathcal D=\{p_x:x\in C\}.
\tag{1.6}
\]

### Lemma Z13.2 -- exact dominance formula

For every \((s,t)\in[H]^2\),

\[
\boxed{
P_{s,t}=\{x\in C:u_x\ge s,\ v_x\ge t\}.
}
\tag{1.7}
\]

#### Proof

The defining owner interval contains \(X_{-1}\) and \(X_0\), so its
intersection lies in \(C\). A coordinate \(x\in C\) survives the whole
interval \(X_{-s},\ldots,X_{t-1}\) precisely when its positive run through
the cut extends at least \(s\) owners to the left and \(t\) owners to the
right. This is exactly (1.7). \(\square\)

---

## 2. Floor equality forbids a strict southwest extent

An intersection of \(s+t\) rank-\((m+1)\) owners along a Johnson walk has
the universal lower bound

\[
|P_{s,t}|\ge(m+1)-(s+t-1)=m+2-s-t.
\tag{2.1}
\]

It is floor-correct when equality holds.

### Lemma Z13.3 -- strict-southwest exclusion

If

\[
|P_{s,t}|=m+2-s-t,
\tag{2.2}
\]

then

\[
\boxed{
\nexists x\in C:\quad u_x<s\ \text{and}\ v_x<t.
}
\tag{2.3}
\]

#### Proof

List the \(L=s+t\) owners as

\[
Y_0=X_{-s},Y_1,\ldots,Y_{L-1}=X_{t-1}.
\]

Map every coordinate of \(Y_0\) absent from the full intersection to its
first departure transition. This map is injective into the \(L-1\)
transitions, because each Johnson transition removes exactly one
coordinate.

Suppose \(x\in C\) has \(u_x<s\) and \(v_x<t\). The left inequality means
that \(x\) is absent before its positive run through the cut and therefore
has an internal arrival. The right inequality supplies a later internal
departure.

That later departure cannot be the first departure of an initial
coordinate. If \(x\notin Y_0\), then \(x\) is not initial. If
\(x\in Y_0\), it departed before the displayed internal arrival, so the
later departure is not its first. Thus one transition is outside the image
of the first-departure injection. At most \(L-2\) initial coordinates can
be lost, and therefore

\[
|P_{s,t}|
\ge(m+1)-(L-2)
=m+3-s-t,
\]

contrary to (2.2). \(\square\)

This is the exact way in which floor correctness controls short runs. It
does not assert that short crossing runs are absent. It says their extent
points cannot lie strictly southwest of a requested correct query.

---

## 3. The Pareto staircase

Take the distinct Pareto-minimal points of \(\mathcal D\):

\[
d_1=(\alpha_1,\beta_1),\ldots,
d_r=(\alpha_r,\beta_r),
\tag{3.1}
\]

ordered by increasing first coordinate. Their second coordinates strictly
decrease.

Construct a monotone unit lattice path \(\Gamma\) from \((1,H)\) to
\((H,1)\) through all \(d_i\). Between consecutive required points, move
east first and then south. The path has \(H-1\) east steps and \(H-1\)
south steps, hence

\[
\boxed{|\Gamma|=2H-1.}
\tag{3.2}
\]

### Lemma Z13.4 -- rectangle interception

Let \(q=(s,t)\in[H]^2\) satisfy

\[
\nexists d\in\mathcal D:\quad d_1<s,\ d_2<t.
\tag{3.3}
\]

If \(p\in\mathcal D\) and \(p\ge q\), then

\[
\boxed{\Gamma\cap[q,p]\ne\varnothing.}
\tag{3.4}
\]

#### Proof

Choose a Pareto-minimal \(d\in\mathcal D\) with \(d\le p\). The path
passes through \(d\).

If \(d\ge q\), take \(z=d\). Otherwise (3.3) leaves two cases.

If \(d_1<s\) and \(d_2\ge t\), follow \(\Gamma\) forward. Before its first
coordinate reaches \(s\), every Pareto minimum encountered has second
coordinate at least \(t\), by (3.3). Because every connecting segment
moves east before south, \(\Gamma\) contains

\[
z=(s,z_2),\qquad z_2\ge t.
\]

Monotonicity from \(d\) gives \(z_2\le d_2\le p_2\), and
\(s\le p_1\), so \(q\le z\le p\).

If \(d_1\ge s\) and \(d_2<t\), traverse \(\Gamma\) backward. Backward
traversal crosses the needed height on a vertical segment before moving
west. Condition (3.3) keeps the first coordinate at least \(s\) until
that crossing. Hence

\[
z=(z_1,t),\qquad z_1\ge s.
\]

Also \(z_1\le d_1\le p_1\) and \(t\le p_2\), giving \(q\le z\le p\).
\(\square\)

---

## 4. The \(2H-1\)-letter lower word

For every staircase vertex \(z=(s,t)\in\Gamma\), emit the actual
intersection letter

\[
L_z=P_{s,t}=\bigcap_{i=-s}^{t-1}X_i.
\tag{4.1}
\]

Order these letters along \(\Gamma\).

### Theorem Z13.5 -- simultaneous literalization of all correct lower crossings

If \(P_q\), \(q=(s,t)\), is floor-correct, then

\[
\boxed{
P_q=
\bigcup_{\substack{z\in\Gamma\\z\ge q}}L_z.
}
\tag{4.2}
\]

The indexing vertices in (4.2) form one contiguous subpath of \(\Gamma\).
Every emitted letter is nonempty.

#### Proof

Along \(\Gamma\), first coordinates are nondecreasing and second
coordinates are nonincreasing. Thus \(z_1\ge s\) is a suffix condition,
\(z_2\ge t\) is a prefix condition, and their intersection is one
contiguous subpath.

If \(z\ge q\), (1.7) gives \(L_z=P_z\subseteq P_q\). Conversely, let
\(x\in P_q\). Then \(p_x\ge q\). Lemma Z13.3 supplies (3.3), and Lemma
Z13.4 gives some

\[
z\in\Gamma\cap[q,p_x].
\]

Now \(p_x\ge z\), so (1.7) gives \(x\in L_z\). This proves (4.2).

Finally, \(L_z\) intersects at most \(2H\) owners and hence at most
\(2H-1\) transitions. Therefore

\[
|L_z|\ge(m+1)-(2H-1)=m+2-2H\ge1
\]

by (0.2). \(\square\)

### Exact Pascal-pin identity

For \(s,t<H\), put

\[
R_{s,t}
=P_{s,t}\setminus
\bigl(P_{s+1,t}\cup P_{s,t+1}\bigr).
\tag{4.3}
\]

Then

\[
\boxed{
R_{s,t}=\{x\in C:(u_x,v_x)=(s,t)\},
}
\tag{4.4}
\]

and

\[
\boxed{
P_{s,t}
=P_{s+1,t}\cup R_{s,t}\cup P_{s,t+1}.
}
\tag{4.5}
\]

Thus adjacent facets union to their parent exactly when
\(R_{s,t}=\varnothing\). A nonempty \(R_{s,t}\) is precisely a positive
coordinate run whose capped two-sided extent is \((s,t)\). The staircase
does not repair such broken parents separately: it shares all pins through
the rectangle-interception identity.

---

## 5. Upper crossings and total local length

Emit the second block

\[
X_{-H},X_{-H+1},\ldots,X_{H-1}.
\tag{5.1}
\]

For \(1\le q\le H\) and \(1\le a\le q\), the subword

\[
X_{-a},X_{-a+1},\ldots,X_{q-a}
\]

lies inside (5.1), and its OR is exactly \(U_{q,a}\). Hence the upper
block realizes every crossing union, correct-rank or otherwise.

The lower and upper witnesses remain inside their respective blocks.
Concatenating the blocks therefore gives a nonzero literal word of length

\[
(2H-1)+2H=\boxed{4H-1}.
\tag{5.2}
\]

This proves Theorem Z13.1.

### Endpoint-throughput audit

Call a cut *strongly clean* when all arrival and departure labels on its
two radius-\(H\) arms are globally distinct. Then no positive run of
length at most \(H\) crosses the cut, every relevant Pascal pin in (4.4)
is empty, and all

\[
\sum_{q=1}^Hq=\frac{H(H+1)}2
\tag{5.3}
\]

lower crossing targets are distinct. An \(N\)-letter word has only
\(N(N+1)/2\) nonempty intervals, so pure interval counting gives only

\[
N\ge H.
\tag{5.4}
\]

The linear construction is therefore consistent with the sharp absolute
endpoint count. More explicitly, in the strongly clean case put

\[
D_k=P_{k,H-k+1}\qquad(1\le k\le H).
\]

Repeated use of the pin-free identity (4.5) gives

\[
P_{s,t}=\bigcup_{k=s}^{H-t+1}D_k
\qquad(s+t\le H+1).
\]

Thus the \(H\)-letter word \(D_1,\ldots,D_H\) is a lower chart attaining
(5.4). There is no possible universal \(\Omega(H^2)\)
endpoint-throughput lower bound under the present literal-word rules.

---

## 6. PBBS global cut ledger

Let a complement-projected PBBS cycle \(C\) have \(\ell\) owners. Let
\(D_C\) be a nonempty set of \(J_C\) transition edges meeting every
positive coordinate-residence interval of length at most \(H\).

Cutting at \(D_C\) produces \(J_C\) paths having no internally bounded
positive run of length at most \(H\). The endpoint-capped erosion theorem
therefore gives path words of total length

\[
\ell+HJ_C.
\tag{6.1}
\]

Append the \(4H-1\) chart at every selected cut. Every original
floor-correct lower window or upper window of depth at most \(H\) that was
destroyed by cutting crosses at least one selected edge and is represented
in that edge's chart. If a window crosses several nearby cuts, choose any
one: every chart is defined from the original cyclic owners, so other cuts
do not change its letters or witness.

Thus the active-cycle length is

\[
\boxed{
\ell+HJ_C+(4H-1)J_C
=\ell+(5H-1)J_C.
}
\tag{6.2}
\]

Projected PBBS cycles have length at least \(2m+1\). Indeed, every
\(f\)-cycle has length \(\lambda(2m+1)\); passing to step two preserves
that length when \(\lambda\) is odd and splits it into two cycles of length
\(\lambda(2m+1)/2\) when \(\lambda\) is even. Under (0.2), the
\(2H\)-owner chart neighborhood is therefore unambiguous.

Formula (6.2) holds for every residence transversal. For the global
ledger, choose \(D_C\) to be a minimum transversal and put
\(J_C=\tau_H(C)\). Circular interval packing and transversal duality then
give

\[
J_C\le\nu_H(C)+1\le2\nu_H(C).
\tag{6.3}
\]

Inactive cycles use cyclic erosion at overhead \(2H\) each, and the number
of projected cycles is at most \(B_m\). Since the unextended owner lengths
sum to \(W\), summing (6.2)--(6.3) gives (0.9).

If \(\nu_H(P_m)\le K B_m\), then

\[
\frac{L_H-W}{W}
\le
\frac{2H+2K(5H-1)}{2m+1}
=O_K(H/m).
\tag{6.4}
\]

This is \(o(1)\) whenever \(H=o(m)\).

---

## 7. Exact proved boundary

### Proved

1. For every Johnson cut satisfying \(2H\le m+1\), the
   \(2H-1\)-letter dominance staircase realizes every floor-correct lower
   crossing intersection through depth \(H\).
2. A \(2H\)-owner block realizes every upper crossing union.
3. Their concatenation is a direct nonzero literal word of length
   \(4H-1\).
4. Nearby cuts do not interfere, because each chart uses the original
   cyclic owner sequence.
5. The complete active-cycle cost is exactly bounded by
   \(\ell+(5H-1)J_C\), and the global PBBS bound is (0.9).
6. Three independent audits checked the departure injection, staircase
   interception, union equality, nonzero constant, nearby-cut scope, and
   global coefficients.

The helper letters \(L_z\) need not themselves be owners or flags of the
original exact factor. The correct statement is that they are explicit
nonempty set letters constructed from original owner sets, so the output
is a direct integral literal OR word. No fractional rebundling or
labelled synchronization is used.

### Not proved

1. The Catalan residence-packing estimate (0.10).
2. The resulting coefficient-one theorem without that separate estimate.
3. A claim that the \(4H-1\) constant is globally minimal among arbitrary
   interleaved lower/upper words. Only the linear order and the
   \(\Omega(H)\) clean-case interval lower bound are asserted.

The quadratic PBBS per-cut literal-seam obstruction is therefore
definitively removed. The remaining PBBS gate is residence packing, not
literal crossing-target restoration.
