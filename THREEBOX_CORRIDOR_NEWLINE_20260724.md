# Dominant three-boxes: exact corridor atoms and the forced global-sharing gate

## 1. Scope and outcome

**Post-audit update.**  After the corridor analysis below was completed, the
independent note `MATH_ATTACK_F_DRAY_CONSTRUCTION_20260724.md` produced an
architecture-free quadratic lower bound which refutes DRAY.  I attacked
that proof line by line in Section 11 and found no gap.  Thus the global
corridor braid posed in Section 9 is not merely open: it is impossible.
Sections 2--10 are retained because they give an independent structural
explanation of where the quadratic obstruction comes from.

Put

\[
 P(p,q,r)=[0,p]\times[0,q]\times[0,r]
\]

with coordinatewise maximum, and let \(g_3(p,q,r)\) be the minimum
length of a nonzero word whose contiguous interval maxima contain every
nonzero point of \(P(p,q,r)\).

This note attacks the primitive dominant ray

\[
 p=at,\qquad q=bt,\qquad r=ct,
 \qquad 0<a<b,\quad c>2b.                 \tag{1.1}
\]

Here \(a,b,c\in\mathbb Z_{>0}\) are fixed (normally with
\(\gcd(a,b,c)=1\)) and \(t\in\mathbb Z_{>0}\) tends to infinity.

There cannot be a word of the formerly desired length

\[
 (p+1)(q+1)+o(t^2).
\]

Sections 2--10 give a construction-and-obstruction analysis that makes the
failure mechanism more rigid; Section 11 audits the architecture-free
quadratic lower bound that settles the proposed ray theorem negatively.

1. There is a canonical family of \(p+1\) literal vertical corridor atoms.
   Their concatenation is the usual slice word, but the decomposition gives
   an exact role ledger
   \[
      (p+1)(q+1)+(p+1)r-1.                \tag{1.2}
   \]
2. The formal exact-width endpoint assignment is forced, endpoint by
   endpoint, to keep its first two coordinates fixed throughout the entire
   rank plateau.  Endpoint throughput also shows that exact width itself is
   impossible when the plateau has more than one rank; the unavoidable
   excess is already linear.  Thus vertical corridors are the equality
   geometry after the necessary boundary slack is separated.
3. With \(d\) endpoints of slack, the number of horizontal owner changes at
   one plateau step has an exact turnover bound
   \[
      I_x\le dp,\qquad I_y\le dq.          \tag{1.3}
   \]
4. Any fusion of the canonical corridor atoms in which a physical position
   carries at most three local roles still cannot have asymptotic width on
   (1.1).  Indeed the required average role multiplicity tends to
   \[
      1+\frac cb>3.                        \tag{1.4}
   \]

Within the canonical-certificate architecture, any hypothetical width-scale
construction would have to be a genuinely global, at-least-four-way (and for
general \(c/b\), correspondingly higher-way) corridor braid.  Pairwise portal
fusion, alternating two-arm fusion, and three-way local overlap cannot work.
Section 11 shows that even unrestricted architectures cannot attain the
proposed width-scale asymptotic.

All statements here are finite and deterministic.  No random or fractional
cover is used.

---

## 2. Width and the plateau

Assume throughout that

\[
 0\le p\le q,\qquad r\ge p+q.              \tag{2.1}
\]

The rank generating polynomial is

\[
 (1+z+\cdots+z^p)(1+z+\cdots+z^q)
 (1+z+\cdots+z^r).
\]

For every rank

\[
 p+q\le s\le r,                            \tag{2.2}
\]

there is exactly one point of rank \(s\) over every base point
\((x,y)\in[0,p]\times[0,q]\), namely

\[
 (x,y,s-x-y).
\]

Hence all ranks in (2.2) have size

\[
 N=(p+1)(q+1),                              \tag{2.3}
\]

and this is the width of the box.

Let

\[
 h=r-p-q+1                                      \tag{2.4}
\]

be the number of plateau ranks.  There is a useful exact endpoint-throughput
lower bound.  Endpoint \(j\) has only \(j\) suffix intervals, hence can
represent at most \(\min(h,j)\) distinct plateau-rank points.  A universal
word of length \(n\) must represent \(Nh\) distinct plateau points.  Thus

\[
 Nh\le\sum_{j=1}^{n}\min(h,j).                 \tag{2.5}
\]

When \(n\ge h\), this becomes

\[
 Nh\le hn-\frac{h(h-1)}2,
\]

and therefore

\[
 \boxed{
 g_3(p,q,r)\ge
 N+\left\lceil\frac{r-p-q}{2}\right\rceil.
 }                                                \tag{2.6}
\]

Thus, if \(g_3(p,q,r)\ge h\) (in particular, if \(N\ge h\)), then (2.6)
holds.  For every fixed positive ray, \(N\gg h\), so this harmless
hypothesis holds for all sufficiently large \(t\).  Bound (2.6) is only
linear above width and is fully compatible with the desired \(o(t^2)\)
error, but it records that Theorem 5.1 below is an equality-geometry
statement rather than an assertion that exact width is attainable.

On the ray (1.1), condition \(c>2b>a+b\) implies (2.1) for every
positive \(t\).

---

## 3. The outer-hook chains of the base rectangle

For \(0\le i\le p\), define the saturated chain

\[
\begin{aligned}
 C_i={}&(0,i),(1,i),\ldots,(p-i,i),\\
      &(p-i,i+1),(p-i,i+2),\ldots,(p-i,q).
\end{aligned}                               \tag{3.1}
\]

Repeated corner points are written only once.  Its bottom and top are

\[
 b_i=(0,i),\qquad t_i=(p-i,q),              \tag{3.2}
\]

and its number of edges is

\[
 s_i=p+q-2i.                                \tag{3.3}
\]

### Lemma 3.1 (exact base partition)

The chains \(C_0,\ldots,C_p\) partition
\([0,p]\times[0,q]\).  Consequently

\[
 \sum_{i=0}^{p}(s_i+1)=(p+1)(q+1)=N.        \tag{3.4}
\]

### Proof

If \(x+y\le p\), then \((x,y)\) lies on the horizontal part of
\(C_y\).  If \(x+y>p\), then it lies on the vertical part of
\(C_{p-x}\).  The two cases are disjoint, including their boundary
convention at \(x+y=p\).  This proves the partition.  Summing its chain
sizes proves (3.4). \(\square\)

This is the outer-hook incarnation of

\[
 (1+\cdots+z^p)(1+\cdots+z^q)
 =\sum_{i=0}^{p}z^i(1+\cdots+z^{p+q-2i}).   \tag{3.5}
\]

---

## 4. A literal vertical corridor atom

Orient \(C_i\) from bottom to top and write

\[
 C_i=(v_{i,0},v_{i,1},\ldots,v_{i,s_i}),
 \qquad v_{i,0}=b_i.                        \tag{4.1}
\]

Define the word

\[
\begin{aligned}
 \mathcal A_i={}&
 (v_{i,s_i},0),(v_{i,s_i-1},0),\ldots,(v_{i,0},0),\\
 & (b_i,1),(b_i,2),\ldots,(b_i,r),          \tag{4.2}
\end{aligned}
\]

where \((v,z)\) denotes the corresponding point of the three-box.  For
\(i=0\), delete the unique zero entry \((b_0,0)=(0,0,0)\).

### Lemma 4.1 (exact atom certificate)

The atom \(\mathcal A_i\) represents every point of

\[
 C_i\times[0,r],                             \tag{4.3}
\]

except, as required by the global convention, the origin when \(i=0\).
Its length is

\[
 |\mathcal A_i|=
 \begin{cases}
 s_0+r,&i=0,\\
 s_i+r+1,&1\le i\le p.
 \end{cases}                                 \tag{4.4}
\]

### Proof

Fix \(v_{i,k}\in C_i\) and \(0\le z\le r\).

If \(z=0\) and \(v_{i,k}\ne b_0\), the corresponding literal entry in
the first line of (4.2) is a one-term witness.

If \(z>0\), take the interval beginning at the occurrence of
\((v_{i,k},0)\) and ending at \((b_i,z)\).  Except when \(i=0\), the base
entries between those positions are

\[
 v_{i,k},v_{i,k-1},\ldots,v_{i,0}=b_i,
\]

followed by copies of \(b_i\).  Since these form a descending segment of
one base chain, their coordinatewise maximum is \(v_{i,k}\).  Their third
coordinates are \(0,1,\ldots,z\), whose maximum is \(z\).  The interval
maximum is therefore exactly \((v_{i,k},z)\).

When \(i=0\) and \(k>0\), the deleted final anchor \(v_{0,0}=b_0\) is
simply absent: the interval contains
\(v_{0,k},v_{0,k-1},\ldots,v_{0,1}\), followed by
\((b_0,1),\ldots,(b_0,z)\).  Its coordinatewise maximum is unchanged.

The sole case in which that stated starting occurrence was deleted is
\(i=0,k=0\).  Then the target is \((0,0,z)\), which is itself the literal
entry \((b_0,z)\), so it has a one-term witness.

If \(k=0,z=0,i>0\), the translated bottom \((b_i,0)\) is nonzero and is
present literally.  The only deleted point is the global origin.  Formula
(4.4) is immediate. \(\square\)

### Corollary 4.2 (the exact isolated-corridor ledger)

Concatenating \(\mathcal A_0,\ldots,\mathcal A_p\) gives a genuine
nonzero contiguous-maximum word for all of \(P(p,q,r)\), of length

\[
\begin{aligned}
 L_{\rm iso}
 &=\sum_{i=0}^{p}|\mathcal A_i|\\
 &=\sum_{i=0}^{p}(s_i+1)+(p+1)r-1\\
 &=\boxed{(p+1)(q+1)+(p+1)r-1}.              \tag{4.5}
\end{aligned}
\]

This is the familiar slice bound, but (4.5) separates it into exactly
\(N-1\) displayed base-anchor roles and exactly \((p+1)r\) positive
vertical-reservoir roles.

### Lemma 4.3 (one isolated cylinder is optimal)

Regard \(C_i\times[0,r]\) as a two-chain rectangle, and require all letters
of its local word to lie in that rectangle.  Then the length in (4.4) is
minimum.

### Proof

Parameterize \(C_i\) by \(0,1,\ldots,s_i\).  For every positive point on
the horizontal axis \((k,0)\), a witnessing interval of maximum \((k,0)\)
must contain a letter with first coordinate exactly \(k\) and second
coordinate zero.  These require \(s_i\) distinct letters, plus the local
origin when it is globally nonzero.

Likewise, every positive point \((0,z)\) on the vertical axis forces a
letter with coordinates exactly \((0,z)\).  These require \(r\) further
letters.  The two lists intersect only at the local origin.  Thus the lower
bound is \(s_0+r\) for \(i=0\), where the global origin is omitted, and
\(s_i+r+1\) for \(i>0\).  Lemma 4.1 attains it. \(\square\)

This optimality is deliberately local.  A global word may use points below
a cylinder target but outside the cylinder chain and may factor a base pin
between several letters; that is exactly the freedom a successful braid
must exploit.

---

## 5. Exact-width plateau rigidity

The next theorem is independent of the outer-hook construction.

Let \(A=(A_1,\ldots,A_n)\) be a three-box word.  At endpoint \(j\), the
distinct suffix maxima

\[
 A_j,\quad A_{j-1}\vee A_j,\quad\ldots,\quad
 A_1\vee\cdots\vee A_j                         \tag{5.1}
\]

form an inclusion chain.  Hence one endpoint contains at most one point
of a fixed rank.

### Theorem 5.1 (exact plateau columns)

Suppose \(A\) is universal for \(P(p,q,r)\) and has length exactly
\(N=(p+1)(q+1)\).  Then every endpoint contains exactly one point of every
plateau rank \(s\in[p+q,r]\).  Moreover, for each endpoint \(j\) there is
one base pair \((x_j,y_j)\) such that its plateau points are exactly

\[
 \boxed{(x_j,y_j,s-x_j-y_j)},
 \qquad p+q\le s\le r.                       \tag{5.2}
\]

At each plateau rank, the \(N\) pairs \((x_j,y_j)\) run through the whole
base rectangle once.

### Proof

A plateau rank contains \(N\) points.  Since one endpoint represents at
most one point of that rank and the word has exactly \(N\) endpoints,
universality forces every endpoint to represent one, and the represented
points are all distinct.

Fix consecutive plateau ranks \(s,s+1\).  At one endpoint the two suffix
maxima lie in the same chain and hence are comparable.  Their ranks differ
by one, so the upper point is obtained from the lower by increasing exactly
one coordinate by one.

Write their first coordinates as \(x_j(s)\) and \(x_j(s+1)\).  Since the
rank-\(s\) and rank-\(s+1\) endpoint assignments both run through every
base pair once,

\[
 \sum_jx_j(s)=\sum_jx_j(s+1)
 =(q+1)\frac{p(p+1)}2.                       \tag{5.3}
\]

But every difference \(x_j(s+1)-x_j(s)\) is nonnegative.  Equality of the
sums forces every one of them to be zero.  The same argument with the
second coordinate gives \(y_j(s+1)=y_j(s)\) for every endpoint.  Thus the
third coordinate increases by one.  Iterating over the plateau proves
(5.2). \(\square\)

Together with the throughput slack (2.6), this theorem explains why a
dominant-ray proof cannot avoid vertical sharing merely by choosing a
different symmetric-chain decomposition.  In the formal equality geometry,
vertical ownership on the whole plateau is forced by the two conserved
horizontal moments; a near-width construction may evade it only through
the surplus-endpoint turnover quantified next.

---

## 6. Quantitative turnover with \(d\) extra endpoints

The exact theorem has a useful slack version.  Put

\[
 n=N+d.                                      \tag{6.1}
\]

At every plateau rank choose one witnessing endpoint for each target.  The
chosen endpoints form a set \(E_s\) of size \(N\); this is possible because
distinct same-rank targets require distinct endpoints.  The remaining
\(d\) endpoints are unchosen.  Choices at different ranks need not agree.

For consecutive plateau ranks \(p+q\le s\le r-1\), define

\[
 D_s=E_s\setminus E_{s+1},\qquad
 B_s=E_{s+1}\setminus E_s,
 \qquad k_s=|D_s|=|B_s|\le d.                \tag{6.2}
\]

For \(j\in E_s\cap E_{s+1}\), comparability gives a saturated step.  Let
\(\Delta x_j,\Delta y_j,\Delta z_j\in\{0,1\}\) be its coordinate
increments, so their sum is one.

### Theorem 6.1 (exact horizontal-turnover identities)

Put

\[
 I_x(s)=\sum_{j\in E_s\cap E_{s+1}}\Delta x_j,
 \qquad
 I_y(s)=\sum_{j\in E_s\cap E_{s+1}}\Delta y_j.       \tag{6.3}
\]

Then

\[
\boxed{
 I_x(s)=
 \sum_{j\in D_s}x_j(s)-
 \sum_{j\in B_s}x_j(s+1),
}                                                     \tag{6.4}
\]

and analogously

\[
\boxed{
 I_y(s)=
 \sum_{j\in D_s}y_j(s)-
 \sum_{j\in B_s}y_j(s+1).
}                                                     \tag{6.5}
\]

In particular,

\[
 \boxed{0\le I_x(s)\le k_sp\le dp,\qquad
        0\le I_y(s)\le k_sq\le dq.}          \tag{6.6}
\]

Thus at most \(k_s(p+q)\) common endpoints can make a nonvertical step at
one plateau transition.

### Proof

The selected targets at either rank contain every base pair once, so their
total first-coordinate sums are equal.  Split both sums into common,
departing, and entering endpoints.  On common endpoints the upper first
coordinate is the lower first coordinate plus \(\Delta x_j\).  Rearranging
gives (6.4).  Nonnegativity is automatic from monotonicity, and the upper
bound follows because the departing sum is at most \(k_sp\) while the
entering sum is nonnegative.  The second-coordinate proof is identical.
\(\square\)

For any set (or interval) of transition indices
\(J\subseteq\{p+q,\ldots,r-1\}\), summing (6.6) gives

\[
 \sum_{s\in J}(I_x(s)+I_y(s))
 \le d(p+q)|J|.                              \tag{6.7}
\]

This is the exact price at which extra endpoints can evade the vertical
columns of Theorem 5.1.

---

## 7. A vertical endpoint is a literal record corridor

The previous statements concern endpoint ownership.  The next observation
recovers the physical word geometry.

### Lemma 7.1 (record-corridor certificate)

Suppose one endpoint \(j\) represents the consecutive vertical targets

\[
 (x,y,z_0),(x,y,z_0+1),\ldots,(x,y,z_1).      \tag{7.1}
\]

Then there are strictly decreasing start positions

\[
 \ell_{z_1}<\ell_{z_1-1}<\cdots<\ell_{z_0}\le j
                                                               \tag{7.2}
\]

such that

\[
 \bigvee_{u=\ell_z}^{j}A_u=(x,y,z).           \tag{7.3}
\]

Every entry in the full corridor

\[
 [\ell_{z_1},j]                               \tag{7.4}
\]

has first coordinate at most \(x\) and second coordinate at most \(y\).
For each \(z_0<z\le z_1\), the newly admitted segment
\([\ell_z,\ell_{z-1}-1]\) contains an entry whose third coordinate is
exactly \(z\), and contains no entry with third coordinate exceeding
\(z\).

### Proof

Choose \(\ell_z\) to be the greatest start position of a suffix interval
ending at \(j\) with maximum \((x,y,z)\).  The suffix maxima grow
monotonically as their start moves left.  Distinct consecutive values force
the strict inequalities (7.2), and (7.3) holds by definition.

The maximum over the largest interval is \((x,y,z_1)\), proving the two
horizontal bounds in (7.4).  Passing from the \(z-1\) suffix to the \(z\)
suffix changes only the third maximum and changes it to exactly \(z\),
which proves the last assertion. \(\square\)

Thus the word-level content of Theorem 5.1 is a family of \(N\) long,
heavily overlapping principal-ideal corridors.  The primitive-ray theorem
asks for these corridors to share almost all of their physical letters.

---

## 8. Safe fusions of the canonical atoms

To state a precise architecture barrier, it is useful to formalize what it
means to fuse the atoms of Section 4 without changing their certificates.

For each local atom \(\mathcal A_i\), call each of its displayed positions
a **local role**.  A certificate-preserving safe fusion consists of:

1. one physical word \(W=(W_1,\ldots,W_n)\);
2. for every \(i\), a nondecreasing map \(\phi_i\) from the local positions
   of \(\mathcal A_i\) to the physical positions of \(W\); and
3. for every local witness interval \([u,v]\) used in Lemma 4.1, the
   physical interval
   \[
      [\phi_i(u),\phi_i(v)]
   \]
   has coordinatewise maximum equal to the same target as \([u,v]\).

Thus local roles may be quotiented together and the physical letter need
not equal either original local letter; what is preserved is the complete
family of interval certificates.  This is the natural formal model for
overlapping atoms while allowing a shared letter to do genuinely new work.
The **load** of a physical position is the number of local roles mapped to
it, counted over all \(\phi_i\).

This definition is intentionally narrower than an arbitrary three-box word:
it captures quotient/interleaving braids which retain the canonical
certificates, but makes no claim that every optimal word has this form.

### Theorem 8.1 (bounded-sharing corridor barrier)

If a safe fusion has maximum load at most \(\kappa\), then

\[
 \boxed{
 n\ge
 \frac{N+(p+1)r-1}{\kappa}.
 }                                                     \tag{8.1}
\]

Consequently, on the ray (1.1), any sequence of safe fusions of length
\(N+o(t^2)\), with maximum loads \(\kappa_t\), must satisfy

\[
 \boxed{
 \liminf_{t\to\infty}\kappa_t\ge
 \left\lceil 1+\frac cb\right\rceil.
 }                                                     \tag{8.2}
\]

In particular, because \(c>2b\), no safe fusion of maximum load at most
three can prove the dominant-ray theorem.

### Proof

By (4.5), the number of local roles is exactly

\[
 R=N+(p+1)r-1.                               \tag{8.3}
\]

If every physical position receives at most \(\kappa\) roles, then
\(R\le\kappa n\), proving (8.1).

For \(p=at,q=bt,r=ct\),

\[
 \frac{R}{N}
 =1+\frac{(at+1)ct-1}{(at+1)(bt+1)}
 =1+\frac cb+o(1).                            \tag{8.4}
\]

If \(n=N+o(t^2)=N(1+o(1))\), the average, and hence the maximum, load tends
to at least \(1+c/b\).  Integrality of \(\kappa_t\) gives (8.2).  Since
\(1+c/b>3\), load three is
impossible for all sufficiently large \(t\). \(\square\)

The point of (8.2) is qualitative as well as numerical.  Alternating two
arms, pairwise seam gluing, or a three-atom local patch whose physical
positions carry at most three canonical local roles cannot possibly remove
the quadratic reset term on the strict dominant cone **within this
certificate-preserving fusion architecture**.  The needed object in that
architecture must let one physical corridor simultaneously serve at least
four outer-hook cylinders, and in general about \(1+c/b\) roles.

There is a sharper distributional consequence.  It is not enough to hide
all high multiplicity at one exceptional portal.

### Lemma 8.2 (one atom never repeats a physical position)

For every certificate-preserving safe fusion, each map \(\phi_i\) is
injective.  Consequently every physical position has load at most \(p+1\).

### Proof

Two different horizontal roles of one atom have different one-term targets,
so their images cannot coincide.  For \(i=0\), every positive vertical-axis
role \((b_0,z)\) also has its displayed one-term witness, so those images
are mutually distinct and distinct from the horizontal images.

For \(i>0\), let \(u_i\) be the bottom horizontal role.  The reservoir role
of height \(z\) is the right endpoint of the displayed witness interval for
\((b_i,z)\), whose left endpoint is \(u_i\).  If two reservoir roles had the
same image, the same physical interval would be required to have two
different maxima.  If a reservoir role shared an image with a horizontal
role, monotonicity of \(\phi_i\) would force it also to share the image of
\(u_i\); the corresponding physical interval would then be the one-term
bottom interval, whose third maximum is zero rather than \(z>0\).  Thus all
roles of atom \(i\) have distinct images.  There are \(p+1\) atoms. \(\square\)

### Corollary 8.3 (a linear high-multiplicity spine is forced)

Let \(H_4(W)\) be the number of physical positions of load at least four.
For \(p\ge3\), every safe fusion satisfies

\[
 \boxed{
 H_4(W)\ge
 \frac{N+(p+1)r-1-3n}{p-2}.
 }                                                     \tag{8.5}
\]

In particular, on (1.1), if \(n=N+o(t^2)\), then

\[
 \boxed{
 H_4(W)\ge (c-2b+o(1))t.
 }                                                     \tag{8.6}
\]

### Proof

Positions outside the set counted by \(H_4\) have load at most three, and
Lemma 8.2 bounds every remaining load by \(p+1\).  Hence

\[
 R\le3(n-H_4)+(p+1)H_4=3n+(p-2)H_4.
\]

Use \(R=N+(p+1)r-1\) to obtain (8.5).  If \(n=N+o(t^2)\), its numerator is

\[
 (p+1)r-2N+o(t^2)
 =a(c-2b)t^2+o(t^2),
\]

and \(p-2=at+O(1)\), proving (8.6). \(\square\)

Thus the canonical-fusion version of DRAY requires a literal linear spine
of four-or-more-way sharing, not merely a bounded number of exceptional
seams.

---

## 9. The former sharpened construction target

Before the architecture-free lower bound was supplied, Sections 5--8 left
the following concrete target.

> **Global outer-hook corridor braid.**  For every fixed
> \(0<a<b,c>2b\), with \(p=at,q=bt,r=ct\), safely fuse the atoms
> \(\mathcal A_0,\ldots,\mathcal A_p\) into one word of length
> \[
> (p+1)(q+1)+o(t^2),                           \tag{9.1}
> \]
> allowing physical positions to have unbounded (or at least the
> ray-dependent load required by (8.2)) corridor multiplicity.

By Lemma 4.1 and the safety clause, (9.1) would immediately prove

\[
 g_3(at,bt,ct)=(at+1)(bt+1)+o(t^2),            \tag{9.2}
\]

because the reverse inequality is the width bound.  Section 11 now records
an independent audit of a proof that (9.2), and hence (9.1), is false.

This formulation is stronger than necessary: an optimal word need not be a
safe fusion of the canonical atoms.  Its advantage is that every target
certificate is already fixed and audited.  Only the physical high-
multiplicity interleaving remains.

Theorem 5.1 shows why this is the right kind of strengthening rather than a
random convenience.  At exact width, every plateau owner is vertical, so
any construction must recreate the same long record-corridor phenomenon,
even if it uses a different lower- and upper-tail routing.

---

## 10. Self-audit and exact status

### Proved

1. The chains (3.1) partition the base rectangle.
2. Every atom (4.2) is a literal nonzero contiguous-maximum word for its
   cylinder, with every witness interval displayed.
3. Each atom is minimum among words restricted to its own two-chain
   cylinder.
4. Their isolated length is exactly
   \[
   N+(p+1)r-1.
   \]
5. Plateau endpoint throughput gives the linear lower bound (2.6).
6. Conditional on exact endpoint saturation, the plateau assignment is
   forced into endpointwise vertical columns.
7. With \(d\) surplus endpoints, the exact turnover identities (6.4)--(6.6)
   hold for any chosen rankwise endpoint injections.
8. A vertical endpoint segment forces the literal principal-ideal record
   corridor of Lemma 7.1.
9. Any safe canonical-atom fusion of maximum load \(\kappa\) obeys (8.1).
   In the strict dominant cone, load at most three is asymptotically
   insufficient.
10. Each atom map is injective, so the load is at most \(p+1\); consequently
    every asymptotic-width safe fusion contains at least
    \((c-2b+o(1))t\) positions of load at least four.
11. The architecture-free quadratic obstruction in Section 11 was checked
    independently at each vulnerable step and yields (11.1).

### Not constructed in Sections 2--9 (and resolved negatively in Section 11)

1. The high-multiplicity safe fusion (9.1).
2. A construction outside the canonical safe-fusion architecture.
3. The primitive-ray theorem (9.2).
4. An unrestricted lower bound contradicting the primitive-ray theorem;
   this is supplied and independently audited in Section 11.

The original corridor analysis isolated a **global many-corridor sharing
law** as its remaining gate.  The independent theorem audited next proves
that no such width-scale law can exist, even outside the canonical fusion
architecture.

---

## 11. Independent adversarial audit of the quadratic DRAY obstruction

The note `MATH_ATTACK_F_DRAY_CONSTRUCTION_20260724.md` claims that, for
fixed integers \(0<a<b\) and \(c>2b\),

\[
 \boxed{
 \liminf_{t\to\infty}
 \frac{g_3(at,bt,ct)-(at+1)(bt+1)}{t^2}
 \ge
 \frac{ab(c-2b)}{c+5a+5b}>0.
 }                                                     \tag{11.1}
\]

This would refute DRAY.  The vulnerable points are the ordered-witness
parameterization, the use of one positive pin for a whole threshold run,
and the block-congestion summation.  I checked each independently.

### 11.1 Ordered middle witnesses

Let \(M=(p+1)(q+1)\), let

\[
 h=\left\lfloor\frac{p+q+r}{2}\right\rfloor,
 \qquad \epsilon=p+q+r-2h\in\{0,1\},          \tag{11.2}
\]

and choose one witness \(I_i=[\ell_i,r_i]\) for every rank-\(h\) target,
ordered by increasing \(\ell_i\).  The rank-\(h\) layer is the full
rectangle because \(p+q\le h\le r\).

Two witnesses cannot have the same left endpoint: with a common start they
are nested and their maxima are comparable.  If \(\ell_i<\ell_j\) but
\(r_i\ge r_j\), then \(I_j\subseteq I_i\), giving the same contradiction.
Thus both endpoint sequences are strictly increasing.  For a word of
length \(M+D\), one may write

\[
 \ell_i=i+\alpha_i,qquad r_i=i+\beta_i,
 \qquad 0\le\alpha_1\le\cdots\le\alpha_M\le D,
 \quad 0\le\beta_1\le\cdots\le\beta_M\le D.   \tag{11.3}
\]

There is no hidden assumption here about choosing shortest or unique
witnesses.

### 11.2 Exact lower-rank and start-capacity ledger

The number of nonzero targets below rank \(h\) is

\[
 L_{<h}
 =M\left(h-\frac{p+q}{2}\right)-1
 =M\frac{r-\epsilon}{2}-1.                  \tag{11.4}
\]

At a selected start \(\ell_i\), a below-rank witness must end before
\(r_i\); otherwise it contains \(I_i\) and its maximum dominates a
rank-\(h\) target.  Hence that start supplies at most
\(d_i=r_i-\ell_i\) lower targets.  There are exactly \(D\) unselected
starts, and one start supplies at most \(h-1\) distinct nonzero targets
below rank \(h\), because its interval maxima form a chain.  Therefore

\[
 \boxed{
 L_{<h}\le\sum_{i=1}^{M}d_i+(h-1)D.
 }                                                     \tag{11.5}
\]

The inclusive-endpoint off-by-one is correct: the earlier endpoints at a
selected start are \(\ell_i,\ldots,r_i-1\), exactly \(d_i\) choices.

### 11.3 Short internal threshold run

For any \(p+q+2\) distinct points of the constant-sum middle rectangle,
some coordinate sequence has an internal positive threshold run.  Indeed,
if a nonnegative scalar sequence has no such run, it is valley-shaped.
If all three coordinate sequences were valleys, order their turn positions
as \(\tau_X\le\tau_Y\le\tau_Z\).  Constant sum and distinctness force
\(\tau_X=1,\tau_Z=m\); between the first two turns \(X\) increases
strictly at every step, and between the last two turns \(Z\) decreases
strictly.  The sum of the two available coordinate ranges is at most
\(p+q\), so \(m\le p+q+1\), a contradiction.

Inside any internal run, take a maximal plateau at the largest coordinate
value on that run.  Both adjacent values are strictly lower, including when
the plateau touches an endpoint of the original run.  A coordinate level
of the middle rectangle contains at most \(q+1\) targets.  Thus the new
run has edge length at most \(q\).  This plateau extraction does not assume
that the selected maximum is globally maximal in the entire middle order.

### 11.4 Literal one-pin gap

Let \([u,v]\) be such a positive run at coordinate threshold \(k\), with
negative neighbors \(u-1,v+1\).  Choose **one** physical position \(s\) in
the positive witness \(I_u\) whose relevant coordinate is at least \(k\).
Because \(I_{u-1}\) is negative and \(s\ge\ell_u>\ell_{u-1}\), one must
have \(s>r_{u-1}\).  Because \(I_{v+1}\) is negative and
\(s\le r_u<r_{v+1}\), one must have \(s<\ell_{v+1}\).  Hence

\[
 r_{u-1}+2\le\ell_{v+1},
 \qquad
 \boxed{
 \beta_{u-1}-\alpha_{v+1}\le v-u\le q.
 }                                                     \tag{11.6}
\]

This argument does not use a common pin for different positive witnesses;
one occurrence from \(I_u\) is sufficient.  Repeated physical occurrences
of the threshold do not weaken (11.6).

Monotonicity of \(\alpha,\beta\) now gives

\[
 d_i\le q+\alpha_{v+1}-\alpha_i\quad(i<u),
 \qquad
 d_i\le q+\beta_i-\beta_{u-1}\quad(i>v).      \tag{11.7}
\]

The signs in both inequalities are correct.

### 11.5 Block pairing and congestion

Put \(s_0=p+q+2\), choose the even number

\[
 K=2\left\lfloor\frac{M}{2s_0}\right\rfloor,
\]

and partition the middle order into \(K\) consecutive blocks of sizes
between \(s_0\) and

\[
 B=s_0+\left\lceil\frac{M-Ks_0}{K}\right\rceil.       \tag{11.8}
\]

For all sufficiently large \(t\), \(K\ge2\).  Pair adjacent blocks.  Find
the short internal run inside the first \(s_0\) positions of each block;
its two negative neighbors remain inside that block.

For a pair \(C=[a,b]\), \(C'=[b+1,c]\), use the run of \(C'\) to bound
the indices of \(C\) by the first inequality in (11.7), and use the run of
\(C\) to bound \(C'\) by the second.  This gives

\[
 \sum_{i\in C\cup C'}d_i
 \le q|C\cup C'|
 +B(\alpha_c-\alpha_a)+B(\beta_c-\beta_a).    \tag{11.9}
\]

The paired index spans are disjoint.  Since both slack sequences are
nondecreasing and lie in \([0,D]\),

\[
 \sum_{\rm pairs}(\alpha_c-\alpha_a)\le D,
 \qquad
 \sum_{\rm pairs}(\beta_c-\beta_a)\le D.      \tag{11.10}
\]

No increment is charged across two block pairs.  Therefore

\[
 \boxed{
 \sum_{i=1}^{M}d_i\le qM+2BD.
 }                                                     \tag{11.11}
\]

This is the decisive congestion estimate, and the cross-pairing removes the
usual invalid assumption that all positive witnesses share one pin.

### 11.6 Finite and asymptotic conclusion

Combining (11.4), (11.5), and (11.11) gives

\[
 D\ge
 \frac{M((r-\epsilon)/2-q)-1}{h-1+2B}.        \tag{11.12}
\]

For \(p=at,q=bt,r=ct\),

\[
 \frac{M}{t^2}\to ab,qquad
 \frac ht\to\frac{a+b+c}{2},
 \qquad
 \frac Bt\to a+b.
\]

Dividing (11.12) by \(t^2\) yields exactly (11.1).

### Audit verdict

\[
 \boxed{
 \text{PASS: the quadratic lower bound is architecture-free and DRAY is
 false throughout }0<a<b,\ c>2b.
 }
\]

I found no common-pin assumption, endpoint-direction error, block-boundary
leak, congestion overcount, parity loss, or zero-target error.  The result
does not refute the global Boolean contiguous-OR conjecture; it removes only
the proposed dominant-ray sufficient route.
