# One-chip insertion spheres: exact matching ledger and Gaussian-prefix obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, search, or external input is
used.

## 0. Verdict

Put

\[
 n=2m+1,
 \qquad
 T={1\over n}\binom nm=\operatorname {Cat}_m.
\tag{0.1}
\]

Write an odd central circular-gap form as

\[
 d={\bf1}+y,
 \qquad y\in\mathbb Z_{\ge0}^m,
 \qquad |y|=m+1,
\tag{0.2}
\]

and a balanced length-\(2m\) parent as

\[
 z={\bf1}+x,
 \qquad x\in\mathbb Z_{\ge0}^m,
 \qquad |x|=m.
\tag{0.3}
\]

The simple insertion sphere of the parent necklace \([x]\) is

\[
 E([x])=\{[x+e_i]:i\in\mathbb Z_m\}.
\tag{0.4}
\]

The exact audit has two sharply different conclusions.

1. **Middle matching.**  The simple quotient hypergraph has exact vertex
   degree

   \[
                    \deg([y])=|\operatorname {supp}y|.
   \tag{0.5}
   \]

   Its average degree is \((m+1)/2\).  Apart from an exponentially small
   set of approximately periodic vertices, its maximum pair codegree is
   one.  Periodic parents are also exponentially sparse and merely replace
   an edge of size \(m\) by an edge of its least period.

   There is no fractional or support-profile Hall obstruction: an explicit
   fractional matching covers \(T-o(T)\) vertex mass, and the unique formal
   support-profile flow is positive and lies far below the parent supply.
   However, these facts do **not** prove an integral matching covering
   \(T-o(T)\).  The rank and the typical degree are both linear in \(m\),
   and the conflict graph already contains induced odd holes in the central
   support strata.  Thus neither linearity, ordinary Hall, nor total
   unimodularity closes the rounding.  The unaugmented near-perfect middle
   matching remains a genuine integral gate.

2. **Gaussian prefixes.**  The common-prefix augmentation is impossible,
   independently of the middle matching.  A depth-\(q\) prefix obtained
   from a one-chip packet necessarily has a circular gap at least \(q+2\).
   Among rank-\(m-q\) target forms, the proportion having such a gap is at
   most

   \[
   (m-q)
   {\binom{2m-q-1}{m-q-1}\over\binom{2m}{m-q-1}}
   \le
   \exp\{-q\log2+O(q^2/m+\log m)\}.
   \tag{0.6}
   \]

   Hence for \(q=A\sqrt m+O(1)\), fixed \(A>0\), the complete one-chip
   catalogue cannot reach a \(1-o(1)\) proportion of the depth-\(q\)
   target orbits.  Since

   \[
   \binom n{m-q}=(e^{-A^2+o(1)})\binom nm,
   \tag{0.7}
   \]

   every selected packet family leaves at least

   \[
                   (e^{-A^2}-o(1))\binom nm
   \tag{0.8}
   \]

   physical depth-\(q\) targets missing.  This is a linear, statewise
   missing-shadow obstruction.  The raw supply/demand ratio
   \(e^{A^2+o(1)}\) counts repeated supply on the exponentially thin
   large-gap target class and therefore is not a Hall calculation.

Thus a solution of the middle insertion-sphere matching would still be a
strong component theorem, but one-chip prefixes alone cannot yield the
Gaussian all-rank coefficient-one theorem.  A successful compiler must
remove the \(q\) symbols in more than one circular gap, equivalently use a
nonconsecutive or re-atlased prefix chronology.

## 1. Rooted and quotient hypergraphs

Let

\[
 \widetilde X_m=\{x\in\mathbb Z_{\ge0}^m:|x|=m\},
 \qquad
 \widetilde Y_m=\{y\in\mathbb Z_{\ge0}^m:|y|=m+1\}.
\tag{1.1}
\]

For rooted \(x\), define

\[
                    \widetilde E_x=\{x+e_i:1\le i\le m\}.
\tag{1.2}
\]

This is an \(m\)-uniform simple hypergraph.  The cyclic group \(C_m\)
rotates coordinates.  Its action on \(\widetilde Y_m\) is free: if a word
were an \(h>1\) fold, then \(h\mid m\) and \(h\mid m+1\), which is
impossible.  Therefore

\[
 |Y_m|={1\over m}\binom{2m}{m-1}=T.
\tag{1.3}
\]

A parent \(x\) can be periodic.  Let \(r(x)\mid m\) be its least
coordinate period.  The distinct quotient children of \([x]\) are

\[
             [x+e_0],[x+e_1],\ldots,[x+e_{r(x)-1}],
\tag{1.4}
\]

so

\[
                         |E([x])|=r(x).
\tag{1.5}
\]

This is the **simple** quotient hypergraph relevant to disjoint packet
selection.  Repeated rootings or literal insertion positions do not create
new matching choices; Section 4 keeps their multiplicities separately.

## 2. Exact degrees and support distribution

### Theorem 2.1 (simple vertex degree)

For \(F=[y]\in Y_m\),

\[
                         \deg F=s(y):=|\operatorname {supp}y|.
\tag{2.1}
\]

#### Proof

An incident parent is obtained by choosing \(i\in\operatorname {supp}y\)
and taking \([y-e_i]\).  Conversely every incident parent arises this
way.  Suppose

\[
                         [y-e_i]=[y-e_j].
\tag{2.2}
\]

Then the two incidences put \([y]\) twice in the same one-chip packet.
The packet phase, or directly the freeness of the odd orbit together with
the one-chip chronology, forces the two active rootings to agree.  Hence
\(i=j\).  Thus the \(s(y)\) active coordinates give distinct quotient
parents. \(\square\)

The number of vertices of degree \(s\) is

\[
              V_s={1\over m}\binom ms\binom m{s-1}.
\tag{2.3}
\]

Indeed one chooses the support and then a positive composition of \(m+1\)
on it.  Consequently

\[
 \sum_sV_s=T,
 \qquad
 \sum_s sV_s=\binom{2m-1}{m-1}={m+1\over2}T.
\tag{2.4}
\]

Thus

\[
                         \mathbb E s={m+1\over2}.
\tag{2.5}
\]

The second factorial moment follows by marking an ordered pair of positive
coordinates:

\[
 \sum_s s(s-1)V_s
 =(m-1)\binom{2m-2}{m-1}.
\tag{2.6}
\]

Therefore the exact variance is

\[
                     \operatorname {Var}(s)
                     ={m^2-1\over4(2m-1)}.
\tag{2.7}
\]

In particular, all but \(o(T)\) vertices have
\(s=m/2+o(m)\).

## 3. Parent periods, edge sizes, and average codegrees

Let

\[
                         C_r=\binom{2r-1}{r-1}.
\tag{3.1}
\]

This is the number of rooted weak compositions of \(r\) into \(r\)
parts.  The number of rooted parent blocks of least period exactly \(r\)
is

\[
                         A_r=\sum_{d\mid r}\mu(r/d)C_d,
\tag{3.2}
\]

and the number of parent necklaces of least period \(r\) is

\[
                         N_r={A_r\over r}.
\tag{3.3}
\]

Hence the exact number of simple quotient edges is

\[
 B_m=\sum_{r\mid m}N_r
 ={1\over m}\sum_{h\mid m}\varphi(h)
       \binom{2m/h-1}{m/h-1}.
\tag{3.4}
\]

The exact edge-size ledger is

\[
 \sum_E|E|=\sum_{r\mid m}rN_r
 =\binom{2m-1}{m-1}={m+1\over2}T.
\tag{3.5}
\]

All proper-period edges together number at most

\[
                   2^{m+o(m)}=e^{-\Omega(m)}T,
\tag{3.6}
\]

and the same remains true after multiplying their count by \(m\).

For distinct vertices \(F,G\), let

\[
                   \lambda(F,G)=|\{E:F,G\in E\}|.
\tag{3.7}
\]

For rooted representatives \(y,y'\), this codegree has the exact
rotation formula

\[
 \lambda([y],[y'])=
 \left|\left\{
 [y-e_a]:
 \begin{array}{l}
 a\in\operatorname {supp}y,\text{ and for some }t\in\mathbb Z_m,\\
 b\in\operatorname {supp}y',\quad
 y-e_a=R^t(y'-e_b)
 \end{array}
 \right\}\right|.
\tag{3.7a}
\]

In particular

\[
             0\le\lambda(F,G)\le
             \min\{\deg F,\deg G\}\le m.
\tag{3.7b}
\]

Then the exact average pair-codegree identity is

\[
 \sum_{\{F,G\}}\lambda(F,G)
 =\sum_{r\mid m}N_r\binom r2,
\tag{3.8}
\]

and hence

\[
 {1\over\binom T2}\sum_{\{F,G\}}\lambda(F,G)
 ={\sum_{r\mid m}N_r\binom r2\over\binom T2}
 ={m^2+O(m)\over2T}.
\tag{3.9}
\]

The last estimate uses

\[
 N_m={1\over m}\binom{2m-1}{m-1}+O(2^{m+o(m)})
 =\left({m+1\over2m}+O(e^{-c m})\right)T,
\tag{3.9a}
\]

for an absolute \(c>0\).

In the rooted hypergraph there is a complementary exact local formula.
If \(|\operatorname {supp}x|=k\), then \(\widetilde E_x\) meets exactly

\[
                  k(k-1)+(m-k)k=k(m-1)
\tag{3.9b}
\]

other rooted edges: its \(k\) support-preserving children have degree
\(k\), and its \(m-k\) support-creating children have degree \(k+1\).
Rooted linearity prevents double counting.  Since a uniform rooted parent
has mean support \(m^2/(2m-1)\), the average rooted packet-conflict degree
is

\[
                         {m^2(m-1)\over2m-1}
                         ={m^2\over2}+O(m).
\tag{3.9c}
\]

There is also an exact dual first moment.  If two parent packets are
chosen uniformly, their average intersection is determined by

\[
 \sum_{E<E'}|E\cap E'|
 =\sum_F\binom{\deg F}{2}
 ={m-1\over2}\binom{2m-2}{m-1}.
\tag{3.10}
\]

Thus the average codegree is exponentially small over all vertex pairs,
while a typical packet has \(\Theta(m^2)\) packet conflicts.  These are
different statistics and must not be interchanged.

### Proposition 3.1 (codegree-one outside an exponential quarantine)

Let \(R\) be cyclic rotation and put

\[
 \mathcal Q_m=\{[y]:\text{ for some }0<t<m,
                     \ \|y-R^ty\|_1\le4\}.
\tag{3.11}
\]

Then

\[
                         |\mathcal Q_m|
                         \le e^{-c m}T
\tag{3.12}
\]

for an absolute \(c>0\), and

\[
 F,G\notin\mathcal Q_m,\quad F\ne G
 \quad\Longrightarrow\quad
                         \lambda(F,G)\le1.
\tag{3.13}
\]

#### Proof

If \(F=[y]\) and \(G=[y']\) have two distinct common parents, there are
two different rotational alignments \(u,v\) and coordinate pairs such
that

\[
 y-R^uy'=e_a-e_b,
 \qquad
 y-R^vy'=e_c-e_d.
\tag{3.14}
\]

The two alignments cannot differ only by the stabilizer of the same
parent, because the common parents are distinct.  Eliminating \(y'\)
therefore gives, for a nonzero rotation \(t\),

\[
 y-R^ty=(e_a-e_b)-R^t(e_c-e_d),
\tag{3.15}
\]

whose \(\ell^1\)-norm is at most four.  Thus \(F\in\mathcal Q_m\).

For the count, fix \(t\ne0\) and put \(g=\gcd(m,t)\le m/2\).  Outside
the at most four break positions in (3.15), \(y\) is constant along the
cycles of \(R^t\).  It is consequently determined by at most \(g+4\)
nonnegative plateau values, the break positions, and their cyclic
incidence.  Ignoring the positive plateau lengths only overcounts, and
gives

\[
 |\{y:|y|=m+1,\ \|y-R^ty\|_1\le4\}|
 \le m^{O(1)}\binom{3m/2+6}{m/2+4}.
\tag{3.16}
\]

Summing over \(t\), and comparing with
\(\binom{2m}{m-1}\), proves (3.12). \(\square\)

The quarantine is needed for an honest quotient statement.  The rooted
hypergraph (1.2) is exactly linear without any exception: two distinct
rooted children have at most one common rooted predecessor.

## 4. Simple support versus two multihypergraphs

There are three ledgers which are easy to conflate.

### 4.1 Simple quotient support

One parent necklace gives one edge of size \(r(x)\).  Vertex degree is
exactly (2.1).  This is the only ledger relevant to matching number.

### 4.2 Root/phase occurrence multihypergraph

If all \(m\) distinguished parent rootings are retained, a parent of least
period \(r\) repeats each of its \(r\) simple child forms \(m/r\) times.
Its multiedge size is therefore \(m\).  The occurrence degree of a vertex
is

\[
                  \deg_{\rm ph}(F)
                  =\sum_{E\ni F}{m\over|E|},
\tag{4.1}
\]

and its average is

\[
 {1\over T}\sum_F\deg_{\rm ph}(F)
 ={mB_m\over T}
 ={m+1\over2}+O(e^{-c m}).
\tag{4.2}
\]

The correction is supported entirely on periodic parents.  These parallel
occurrences do not enlarge a matching.

### 4.3 Literal binary insertion slots

For the positive parent gap \(z_i=1+x_i\), there are \(z_i\) literal
positions in the corresponding zero run which all produce the same simple
child \(z+e_i\).  Thus a rooted parent has weighted insertion total

\[
                         \sum_i z_i=2m.
\tag{4.3}
\]

For an odd child gap word \(d\), deleting any of the \(d_i-1\) zeros in
gap \(i\) produces the same simple parent \(d-e_i\), and

\[
                         \sum_i(d_i-1)=m+1.
\tag{4.4}
\]

This literal occurrence incidence is biregular after roots are retained:
row total \(2m\), column total \(m+1\).  It is useful for a fractional
mass audit but supplies no additional disjoint insertion spheres.  Using
\(2m\) as the simple packet size, or \(m+1\) as the simple vertex degree,
is therefore incorrect.

## 5. Exact support-profile flow and the absence of a fractional Hall cut

A parent \(x\) with support size \(k\) has exactly

* \(k\) children of support \(k\), obtained by incrementing a positive
  coordinate; and
* \(m-k\) children of support \(k+1\), obtained by incrementing a zero
  coordinate.

Ignore the exponentially small periodic residue.  If \(c_k\) packets of
parent support \(k\) occur in a perfect packing, the support ledger must be

\[
             V_s=s c_s+(m-s+1)c_{s-1}.
\tag{5.1}
\]

The unique formal solution is

\[
 c_s^*={1\over m(m+1)}\binom ms
                  \left(\binom ms-(-1)^s\right).
\tag{5.2}
\]

Indeed the rooted recurrence is

\[
 \widetilde c_s={1\over s}
   \left(\binom ms\binom m{s-1}-(m-s+1)\widetilde c_{s-1}\right),
\tag{5.3}
\]

and unrolling it gives

\[
 \widetilde c_s
 ={m!^2\over(m-s)!s!}
   \sum_{j=1}^s{(-1)^{s-j}\over j!(m-j+1)!}
 ={1\over m+1}\binom ms
                  \left(\binom ms-(-1)^s\right).
\tag{5.4}
\]

Division by the free orbit size \(m\) gives (5.2).

The number of rooted parents of support \(s\) is

\[
                         P_s=\binom ms\binom{m-1}{s-1}.
\tag{5.5}
\]

Hence the required central selection fraction is

\[
 {\widetilde c_s\over P_s}
 ={m\over s(m+1)}
   \left(1-{(-1)^s\over\binom ms}\right)
 ={1+o(1)\over s}.
\tag{5.6}
\]

It is positive and strictly below one.  In the central window it is
\((2+o(1))/m\).  Thus no support stratum, nor any union detected by this
two-level flow, has a positive-density capacity deficit.  Nonintegrality of
some values in (5.2) can force a finite exact residue, but not a linear
leave.

There is also a direct fractional near-factor, without solving (5.2)
pointwise.  Let \(\omega=\omega(m)\to\infty\) with
\(\omega=o(\sqrt m)\), and put

\[
                         K=\left\lfloor {m\over2}
                                 +\omega\sqrt m\right\rfloor.
\tag{5.7}
\]

Give weight \(1/K\) to every simple parent packet whose parent support is
at most \(K-1\), and weight zero to all other packets.  A child of support
\(s\le K-1\) has all its \(s\) parents retained, hence load \(s/K\).  A
child of support \(K\) can see only parents of support \(K-1\), and hence
has load at most one.  A child of larger support has load zero.  Therefore
this is a feasible fractional matching.  By (2.5)--(2.7), its objective is

\[
       \sum_E|E|x_E=\sum_F\sum_{E\ni F}x_E=T-o(T).
\tag{5.8}
\]

So every fractional matching dual has value at least \(T-o(T)\).  Any
middle obstruction is necessarily an **integral configuration
obstruction**, not an ordinary weighted Hall cut.

The remaining rounding is not automatic.  The packet conflict graph on
rooted parents has

\[
 x\sim x'
 \quad\Longleftrightarrow\quad
 x'-x=e_i-e_j
\tag{5.9}
\]

for some \(i\ne j\).  It already has induced odd holes in the bulk.  To
see this, choose a nonnegative base vector \(b\) of sum \(m-2\), with
central-size support, with five fixed coordinates positive, and with no
nontrivial rotation at \(\ell^1\)-distance at most eight.  Such choices
exist for all sufficiently large \(m\) by the same plateau count as
(3.16), even after the support and five-coordinate restrictions.  For the
five cyclic pairs

\[
                         S_i=\{i,i+1\}\subset\mathbb Z_5,
\tag{5.10}
\]

the parents \(x^{(i)}=b+\mathbf1_{S_i}\) form an induced \(C_5\):
consecutive pairs differ by one unit transfer and nonconsecutive pairs
differ in four coordinates.  The separation condition on \(b\) prevents
quotient rotation from identifying two of these parents or adding a
chord.  Thus both the rooted and quotient conflict graphs contain an
induced \(C_5\); the corresponding five shared child rows give the usual
odd-cycle submatrix.  The incidence matrix is therefore not balanced or
totally unimodular.  This finite odd hole is not a positive-density no-go,
but it proves that fractional near-perfectness cannot simply be declared
integral.

Accordingly the current rigorous middle boundary is

\[
 \boxed{\nu^*(\mathcal H_m)=T-o(T),\qquad
        \nu(\mathcal H_m)\ge(1/2-o(1))T,}
\tag{5.11}
\]

where the objectives count covered vertices.  Proving
\(\nu(\mathcal H_m)=T-o(T)\) still requires a special integral sewing,
coloring, or absorption theorem for (5.9).

## 6. Exact prefix completion kernel

Let \(q\ge1\), \(k=m-q\), and let a rooted rank-\(k\) target have positive
circular-gap composition

\[
                         g=(g_1,\ldots,g_k),
 \qquad \sum_i g_i=n.
\tag{6.1}
\]

At a packet phase, the first \(k-1\) target gaps are consecutive parent
gaps.  The remaining \(q+1\) parent gaps are omitted at the end of the
prefix, and the one extra chip lies there as well.  Hence the closing
target gap is exactly

\[
                         g_i=1+u_1+\cdots+u_{q+1},
 \qquad u_j\ge1.
\tag{6.2}
\]

For an aperiodic target the exact number of full-catalogue parent-phase
completions is therefore

\[
                  D_q(g)=\sum_{i=1}^k\binom{g_i-2}{q},
\tag{6.3}
\]

with the binomial coefficient interpreted as zero when \(g_i<q+2\).
Indeed, after choosing the closing gap, one chooses a positive composition
of \(g_i-1\) into \(q+1\) omitted parent gaps.  All other parent gaps are
then fixed.

If \(g\) has translation stabilizer order \(h\), sum (6.3) over one least
gap period, equivalently divide the full cyclic sum by \(h\).  Such targets
are exponentially sparse for \(q=O(\sqrt m)\), and the reachability
criterion is unchanged:

\[
                 D_q(g)>0
                 \quad\Longleftrightarrow\quad
                 \max_i g_i\ge q+2.
\tag{6.4}
\]

This is the exact compatibility kernel missing from a mere
supply/demand count.

## 7. Gaussian-prefix no-go

### Theorem 7.1 (large-gap obstruction)

For \(q=A\sqrt m+O(1)\), fixed \(A>0\), the proportion of rank-\(m-q\)
translation orbits reachable by any one-chip prefix is \(o(1)\).

#### Proof

There are

\[
                         \binom{2m}{k-1}
\tag{7.1}
\]

rooted positive compositions of \(n\) into \(k=m-q\) gaps.  If a fixed
gap is at least \(q+2\), subtracting \(q+1\) from it leaves a positive
composition of \(2m-q\) into \(k\) parts.  Thus the union bound gives

\[
 \Pr(\max_i g_i\ge q+2)
 \le
 k{\binom{2m-q-1}{k-1}\over\binom{2m}{k-1}}.
\tag{7.2}
\]

Since \(k-1=m-q-1\),

\[
 {\binom{2m-q-1}{k-1}\over\binom{2m}{k-1}}
 =\prod_{t=0}^{q}{m+q+1-t\over2m-t}.
\tag{7.3}
\]

Taking logarithms yields

\[
 \log(7.2)
 \le \log m-(q+1)\log2+O(q^2/m).
\tag{7.4}
\]

For \(q=A\sqrt m+O(1)\), the right side tends to \(-\infty\).  The
periodic target forms contribute only \(e^{-\Omega(m)}\) relatively, so
passing from rooted forms to translation orbits does not change the
conclusion. \(\square\)

The physical rank-\(m-q\) layer has size

\[
 N_q=\binom{2m+1}{m-q}
     =(e^{-A^2+o(1)})\binom{2m+1}{m}.
\tag{7.5}
\]

By Theorem 7.1, even selecting **every** parent packet can reach only
\(o(N_q)\) distinct targets at this depth.  A fortiori any disjoint middle
packet selection leaves

\[
 N_q-o(N_q)
 =(e^{-A^2}-o(1))\binom{2m+1}{m}
\tag{7.6}
\]

targets missing.

The total occurrence identity remains true: summing (6.3) over all target
forms reproduces the complete parent-phase count.  It is simply extremely
nonuniform.  Targets with a \(q\)-scale gap carry all the supply, while a
\(1-o(1)\) target majority has degree zero.  Therefore the marginal ratio

\[
 {T\over |\mathscr O_q|}=e^{A^2+o(1)}
\tag{7.7}
\]

is not evidence for Hall expansion.

## 8. Exact surviving gate and minimal escape

The one-chip packet theorem still gives a valuable unaugmented target:

> Find an integral matching in the simple quotient hypergraph (0.4)
> covering \(T-o(T)\) odd central forms.

Sections 2--5 show that periodic residues, low degrees, average
codegrees, support capacity, and the fractional matching LP do not refute
this target.  Its exact obstacle is integral packing in the unit-transfer
conflict graph (5.9).

The following stronger statement is false:

> Use the same one-chip packets and their consecutive packet prefixes to
> cover the full Gaussian lower band with \(o(W)\) holes.

The minimal chronological escape is exact.  At depth \(q\), the omitted
middle symbols must be allowed to occupy at least two separated circular
arcs for a typical target, instead of one terminal arc.  Equivalently one
needs at least one of:

1. a nonconsecutive prefix compiler;
2. a re-atlasing/cross-parent splice before the depth-\(q\) readout; or
3. an independent lower-shadow completion not constrained to the
   one-chip packet order.

Without such an operation, the large-gap zero-degree cut (6.4) is
unavoidable and already gives a linear missing-shadow obstruction at one
Gaussian depth.
