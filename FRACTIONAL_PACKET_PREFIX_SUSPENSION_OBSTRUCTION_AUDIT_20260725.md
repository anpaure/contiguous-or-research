# Independent audit of the prefix-suspension obstruction

Date: 2026-07-25

Scope: independent, pure-mathematical audit of
FRACTIONAL_PACKET_PREFIX_SUSPENSION_OBSTRUCTION_20260725.md, followed by a
general prefix-cylinder extension. No computation, search, or external
result is used.

## 0. Verdict

**PASS after one indexing correction.** The MSW concatenation law,
complemented-prefix colour formula, survival under all defining size-two
switches, packet disjointness, Catalan ratio, and edit-robust lower bound
are correct. The original draft mis-indexed the defining components as
\(\mathcal C_{0,1100R}\) with \(R\in\mathcal D_{m-2}\). The actual
definition is

\[
 \mathcal C_{0,1100V},\qquad V\in\mathcal D_{m-4},
\]

because the component's second parameter \(1100V\) must have semilength
\(m-2\). This is a notational error only; the survival proof below remains
valid.

In particular, the strengthened main statement is correct: for \(m\ge6\),

\[
 \vartheta(F_m^\dagger,\beta)
 \ge \operatorname{Cat}_{m-4}-\operatorname{Cat}_{m-6},
 \tag{0.0}
\]

and at row distance \(d\) the right side becomes
\((\operatorname{Cat}_{m-4}-\operatorname{Cat}_{m-6}-d)_+\).
Its normalized limit is \(15/4096\).

There is also a genuine extension. Any rebundling whose removed canonical
rows lie in Dyck-prefix cylinders of maximum semilength \(r\) leaves a
primitive-prefix packet packing of size

\[
 \mathcal N_{m,r}
 =\sum_{p=r+1}^{m-4}\operatorname{Cat}_{p-1}
                         \operatorname{Cat}_{m-p-4}
 =\operatorname{Cat}_{m-4}
  -\sum_{a=0}^{r-1}\operatorname{Cat}_a
                         \operatorname{Cat}_{m-5-a}.
 \tag{0.1}
\]

If \(r\le(m-5)/2\), then

\[
 \mathcal N_{m,r}\ge\frac12\operatorname{Cat}_{m-4}.
 \tag{0.2}
\]

More generally, for every \(0\le r\le m-5\),

\[
 \mathcal N_{m,r}\ge\operatorname{Cat}_{m-5}.
 \tag{0.3}
\]

Thus no family of Dyck-prefix-cylinder trades of maximum depth at most
\(m-5\) can eliminate the fractional packet obstruction.

## 1. Line-by-line audit

### 1.1 Concatenation

The induction proving

\[
 \pi(PQ)=\pi(P)\Vert(2p+\pi(Q))
 \tag{1.1}
\]

is valid. In \(P=1u0v\), appending \(Q\) changes only the final
\(\pi(v)\)-block of the recursive formula. Its total offset is

\[
 |u|+2+|v|=|P|=2p.
\]

The \(a_i,b_i\) collectively permute the \(2p\) prefix coordinates, so the
first \(p\) complete moves toggle each prefix bit once and no suffix bit.
The state is therefore exactly \(\overline P Q\).

Applying (1.1) twice to \(PwV\) places both colour coordinates
\(a_i,b_{i-1}\) in the seed block. Hence, at time \(p+i\),

\[
 \Gamma_{PwV}=\overline P\,\Gamma_w(x_i)\,V.
 \tag{1.2}
\]

There is no index-shift error.

### 1.2 Shifted target

For \(P=10\), \(\overline P=01\). The seed colour
\(T_0=10111101\) has six ones, so

\[
 01T_0V=0110111101V
\]

has \(1+6+(m-5)=m+2\) ones. Its complement among the \(2m\) finite
coordinates has \(m-2\) elements; adjoining \(\infty\) gives a genuine
rank-\((m-1)\) target.

The three roots \(10w^{(j)}V\) are Dyck words of semilength \(m\).
Distinct \(V\)'s give distinct roots and hence pairwise disjoint triples of
canonical wreaths.

### 1.3 Survival

In general, switching \(\mathcal C_{0,S}\), with
\(S\in\mathcal D_{m-2}\), removes exactly

\[
 1100S,\qquad1010S.
\]

The defining factor \(F_m^\dagger\) uses \(S=1100V\) with
\(V\in\mathcal D_{m-4}\), and therefore removes
\(11001100V\) and \(10101100V\). Every shifted owner starts
\(10\,11=1011\), so every displayed owner survives every defining switch.
Extra owners introduced on right sides are irrelevant because a packet may
be any required-size subset of the full owner set.

### 1.4 Packet packing

At depth one every balanced quota is \(1\) or \(2\). Each surviving
three-owner set therefore contains a packet of size \(2\) or \(3\).
The owner triples are disjoint, so unit weight on one packet per target is
a congestion-one dual packing. This proves

\[
 \vartheta(F_m^\dagger,\beta)\ge\operatorname{Cat}_{m-5}.
\]

If \(d\) rows of \(F_m^\dagger\) are removed, each removed row hits at most
one disjoint triple. At least
\((\operatorname{Cat}_{m-5}-d)_+\) packets remain, proving the edit-robust
bound.

### 1.5 Catalan ratio

\[
 \frac{\operatorname{Cat}_{m-5}}{\operatorname{Cat}_m}
 =\prod_{j=0}^{4}\frac{m+1-j}{2(2m-1-2j)}
\]

is exactly the quotient displayed in the report, and tends to
\(4^{-5}=1/1024\).

## 2. General safe prefix-code theorem

Let \(\mathscr P\) be a prefix-free family of Dyck words. Suppose an exact
factor \(F\) contains every canonical row

\[
 E(Pw^{(j)}V),\qquad
 P\in\mathscr P,\quad j\in\{1,2,3\},\quad
 V\in\mathcal D_{m-p-4}.
 \tag{2.1}
\]

Then every balanced quota system containing depth one satisfies

\[
 \boxed{
 \vartheta(F,\beta)
 \ge\sum_{P\in\mathscr P}\operatorname{Cat}_{m-p-4}.
 }
 \tag{2.2}
\]

Proof: suspension gives the common target word
\(\overline P T_0V\). Prefix-freeness makes all owner roots distinct. It
also makes the complemented code prefix-free, so the target word uniquely
identifies \(P\), then \(V\). Thus resources and owner triples are
distinct. Selecting a packet of size \(2\) or \(3\) in each triple gives
congestion one. The same bound minus \(d\) holds at row distance \(d\),
since one removed row hits at most one selected triple.

## 3. Primitive prefixes evade prefix cylinders

For nonempty \(U\in\mathcal D_u\), define

\[
 [U]_m=\{UZ:Z\in\mathcal D_{m-u}\}.
\]

Suppose a rebundled exact factor retains every canonical row outside a
union of such cylinders whose defining words have maximum semilength
\(r\).

A primitive Dyck word \(P\in\mathcal D_p\) returns to zero only at its
end. There are \(\operatorname{Cat}_{p-1}\) primitive words, via
\(P=1U0\). If \(p>r\), then \(P\) cannot begin with any forbidden Dyck
word: that would force an earlier return to zero. Primitive words of
different lengths are prefix-free for the same reason.

Moreover, \(\overline P\) is a negative primitive excursion. In the
target word \(\overline P T_0V\), its end is the first return of signed
height to zero. Hence targets remain uniquely decodable even across
different \(p\).

Applying (2.2) to all primitive \(P\) with \(r<p\le m-4\) proves

\[
 \vartheta(F,\beta)\ge\mathcal N_{m,r},
\]

with \(\mathcal N_{m,r}\) as in (0.1). The identity follows from Catalan
convolution after setting \(a=p-1\):

\[
 \sum_{a=0}^{m-5}\operatorname{Cat}_a
                         \operatorname{Cat}_{m-5-a}
 =\operatorname{Cat}_{m-4}.
\]

The summand is symmetric under \(a\leftrightarrow m-5-a\). If
\(r\le(m-5)/2\), the retained tail \(a\ge r\) contains at least one full
half of this symmetric convolution, proving (0.2). Since

\[
 \frac{\operatorname{Cat}_{m-4}}{\operatorname{Cat}_m}\to\frac1{256},
\]

the asymptotic packet density is at least \(1/512\).

There is also an endpoint bound which does not require
\(r\le(m-5)/2\). For every \(r\le m-5\), the tail in (0.1) contains its
last term \(a=m-5\). Therefore

\[
 \mathcal N_{m,r}\ge
 \operatorname{Cat}_{m-5}\operatorname{Cat}_0
 =\operatorname{Cat}_{m-5}.
 \tag{3.1}
\]

Its normalized limit is \(1/1024\). Hence the obstruction persists even
when forbidden prefix cylinders reach semilength \(m-5\); the primitive
prefixes of semilength \(m-4\), followed immediately by the fixed seed,
remain available.

One can also treat the endpoint \(r=m-4\) and quantify the number of
forbidden cylinders. Let \(\mathrm{Prim}_r\) be the primitive Dyck words
of semilength \(r\), and put

\[
 b_r=|\mathscr U\cap\mathrm{Prim}_r|.
\]

For a primitive \(P\in\mathrm{Prim}_r\), no shorter nonempty Dyck word is
a prefix of \(P\). Thus among cylinders defined by words of semilength at
most \(r\), the root \(Pw^{(j)}V\) is excluded only when the defining word
is \(P\) itself. We may therefore add every
\(P\in\mathrm{Prim}_r\setminus\mathscr U\) to the safe code, obtaining

\[
 \boxed{
 \vartheta(F,\beta)\ge
 \mathcal N_{m,r}
 +\bigl(\operatorname{Cat}_{r-1}-b_r\bigr)
      \operatorname{Cat}_{m-r-4}.
 }
 \tag{3.2}
\]

In particular, when \(r=m-4\),

\[
 \vartheta(F,\beta)\ge
 \operatorname{Cat}_{m-5}-b_{m-4}.
 \tag{3.3}
\]

Therefore a prefix-cylinder rebundling reaching the maximal usable prefix
depth \(m-4\) must explicitly forbid almost every one of the
\(\operatorname{Cat}_{m-5}\) primitive prefixes at that depth before this
certificate can become \(o(\operatorname{Cat}_m)\). A bounded or
sub-Catalan number of prefix cylinders still leaves linear packet mass.

## 4. Strengthened code for \(F_m^\dagger\)

For the specific forbidden prefixes \(1010,1100\), use

\[
 \mathscr P^\dagger
 =\{10\}\cup
 \{P:P\text{ primitive Dyck of semilength }p\ge3\}.
 \tag{4.1}
\]

The \(P=10\) owner roots start \(1011\), so they are safe. A primitive
word of semilength at least three starts \(11\), cannot begin \(1010\),
and cannot begin \(1100\), which would return to zero after four bits.
The family is prefix-free.

Therefore, for \(m\ge6\), \(F_m^\dagger\) has a disjoint packet family of
exact size

\[
 \begin{aligned}
 \operatorname{Cat}_{m-5}
 +\sum_{p=3}^{m-4}\operatorname{Cat}_{p-1}
                         \operatorname{Cat}_{m-p-4}
 &=\operatorname{Cat}_{m-4}-\operatorname{Cat}_{m-6}.
 \end{aligned}
 \tag{4.2}
\]

The full convolution over \(1\le p\le m-4\) is
\(\operatorname{Cat}_{m-4}\); only \(p=2\), of size
\(\operatorname{Cat}_{m-6}\), is omitted. Consequently,

\[
 \frac{\operatorname{Cat}_{m-4}-\operatorname{Cat}_{m-6}}
      {\operatorname{Cat}_m}
 \longrightarrow
 \frac1{256}-\frac1{4096}
 =\frac{15}{4096}.
 \tag{4.3}
\]

At row distance \(d\), at least

\[
 \bigl(\operatorname{Cat}_{m-4}-\operatorname{Cat}_{m-6}-d\bigr)_+
\]

packets remain. For \(m=5\), the original \(P=10\) construction gives one
packet; (4.2) would require the convention
\(\operatorname{Cat}_{-1}=0\).

## 5. Boundary

This rules out rebundlings supported on Dyck-prefix cylinders of maximum
semilength at most \(m-5\), with a stronger \(1/512\) asymptotic density
through half depth. It does not rule out trades whose removed
canonical support meets essentially every primitive first-return class,
nor an exact factor far from the canonical one which preserves no large
canonical prefix code. It is an obstruction theorem, not a proof or
disproof of \((\mathrm{FSP}_A)\) over the full factor fibre.

## 6. Exact global deletion hypergraph

There is a useful formulation which drops all prefix-cylinder assumptions.
Let

\[
 A=w^{(1)},\qquad B=w^{(2)},\qquad D=1100,
\]

so \(A,B\) are primitive Dyck components of semilength four and
\(w^{(3)}=DD\).

Define a 3-uniform hypergraph on the canonical Dyck roots by

\[
 e(P,V)=\{PAV,PBV,PDDV\},
 \tag{6.1}
\]

where \(P\) is primitive of semilength \(1\le p\le m-4\) and
\(V\in\mathcal D_{m-p-4}\).

These edges are pairwise vertex-disjoint. Indeed, the first return to zero
of any root in (6.1) recovers the end of \(P\). The next seed block
recovers which of \(A,B,DD\) occurs, and the remainder recovers \(V\).
Therefore

\[
 \nu(\mathcal H_m^{\mathrm{prim}})
 =\tau(\mathcal H_m^{\mathrm{prim}})
 =\tau_f(\mathcal H_m^{\mathrm{prim}})
 =\sum_{p=1}^{m-4}\operatorname{Cat}_{p-1}
                         \operatorname{Cat}_{m-p-4}
 =\operatorname{Cat}_{m-4}.
 \tag{6.2}
\]

More exactly, a set of \(d\) canonical-row deletions can hit at most \(d\)
of these edges, and this is attainable by taking one row from each of
\(d\) edges. Thus the minimum number of deletions needed to leave at most
\(s\) primitive-prefix triples intact is

\[
 \boxed{\bigl(\operatorname{Cat}_{m-4}-s\bigr)_+.}
 \tag{6.3}
\]

In particular, reducing this packet family to
\(o(\operatorname{Cat}_m/\sqrt m)\) requires

\[
 d\ge
 \operatorname{Cat}_{m-4}
 -o(\operatorname{Cat}_m/\sqrt m)
 =\left(\frac1{256}-o(1)\right)\operatorname{Cat}_m.
 \tag{6.4}
\]

This exactly characterizes arbitrary canonical-row deletion sets for this
full-depth primitive-prefix matching, not merely cylinder-supported
deletions.

## 7. Multiple placements and a tight global bracket

Allow now every Dyck prefix \(U\), not only a primitive one. The full local
collision hypergraph has edges

\[
 \{UAV,UBV,UDDV\},\qquad |U|/2+|V|/2=m-4.
 \tag{7.1}
\]

Its number of edges is

\[
 \sum_{p=0}^{m-4}\operatorname{Cat}_p
                         \operatorname{Cat}_{m-p-4}
 =\operatorname{Cat}_{m-3}.
 \tag{7.2}
\]

In the free monoid of primitive Dyck components, an edge is the local
replacement \(A\leftrightarrow B\leftrightarrow DD\).

### 7.1 A larger disjoint matching

Let

\[
 \mathcal P(z)=zC(z)
\]

be the generating function of primitive Dyck components and put

\[
 R(z)=\mathcal P(z)-z^2-2z^4.
\]

Thus \(R\) counts all primitive components other than \(D,A,B\).
Call a prefix \(U\) clean if its primitive-component word avoids \(A,B,DD\)
and does not end in \(D\). Every clean word decomposes uniquely into a
sequence of blocks

\[
 D^\varepsilon R,\qquad\varepsilon\in\{0,1\}.
\]

Hence its generating function is

\[
 U_0(z)=
 \frac1{1-(1+z^2)(\mathcal P(z)-z^2-2z^4)}.
 \tag{7.3}
\]

For every clean \(U\) and arbitrary Dyck suffix \(V\), select the edge
\(\{UAV,UBV,UDDV\}\). These selected edges are disjoint: in each of their
three vertices, the inserted \(A,B\), or \(DD\) is the first occurrence of
any marker in \(\{A,B,DD\}\). The clean prefix ends outside \(D\), so no
new \(DD\) straddles the boundary. The first marker therefore uniquely
decodes \(U\), the alternative, and \(V\).

The matching generating function is

\[
 M(z)=z^4U_0(z)C(z).
 \tag{7.4}
\]

Set \(s=\sqrt{1-4z}\). Since

\[
 C(z)=\frac2{1+s},\qquad
 \mathcal P(z)=zC(z)=\frac{1-s}{2},
\]

the denominator in (7.3) has expansion

\[
 1-(1+z^2)(\mathcal P-z^2-2z^4)
 =\frac{1113}{2048}+\frac{17}{32}s+O(s^2).
 \tag{7.5}
\]

No denominator zero occurs in \(|z|<1/4\), because the removed-component
series has nonnegative coefficients and its value at \(1/4\) is
\(935/2048<1\). Standard square-root coefficient extraction therefore
gives

\[
 \frac{[z^m]M(z)}{\operatorname{Cat}_m}
 \longrightarrow
 \delta
 =
 \frac1{256}
 \left[
 \left(\frac{1113}{2048}\right)^{-1}
 +\frac{17}{32}
  \left(\frac{1113}{2048}\right)^{-2}
 \right]
 =
 \frac{17608}{1238769}.
 \tag{7.6}
\]

Thus the full local collision hypergraph has matching and transversal
number at least

\[
 \left(\frac{17608}{1238769}+o(1)\right)
 \operatorname{Cat}_m
 \approx0.014214\,\operatorname{Cat}_m.
 \tag{7.7}
\]

The same disjoint-packet argument makes this an edit-robust lower bound for
the packet LP.

The first-occurrence matching admits a disjoint recursive refinement.
After the clean-prefix stage, every unused root which has an active
occurrence has first marker

\[
 U_0DA\qquad\text{or}\qquad U_0DB,
\]

where \(U_0\) is clean. Indeed, the prefix before a first marker is
marker-free. If it ends outside \(D\), the root was used at the first
stage. If it ends in \(D\), a first \(DD\) marker would start one position
earlier, so the marker must be \(A\) or \(B\). The trailing \(D\) is
unique because the prefix avoids \(DD\).

These dirty prefixes are prefix-free: each ends at the root's first active
occurrence. All roots below distinct dirty prefixes are disjoint and were
unused at the first stage. We may therefore repeat the entire matching
construction independently in the suffix after each dirty prefix, and
iterate.

If \(M_*(z)\) is the recursively refined matching series, its exact
renewal equation is

\[
 M_*
 =z^4U_0C+2z^6U_0M_*.
\]

Consequently

\[
 M_*(z)
 =
 \frac{z^4C(z)}
 {1-(1+z^2)(\mathcal P(z)-z^2-2z^4)-2z^6}.
 \tag{7.7a}
\]

At \(z=1/4\), the new denominator has constant term

\[
 \frac{1113}{2048}-\frac1{2048}
 =\frac{139}{256},
\]

and the same linear coefficient \(17/32\). Its subtracted nonnegative
series has value \(117/256<1\), so there is no smaller-modulus pole.
Therefore the refined matching density is

\[
 \boxed{
 \delta_*
 =
 \frac1{256}
 \left[
 \frac{256}{139}
 +\frac{17}{32}\left(\frac{256}{139}\right)^2
 \right]
 =\frac{275}{19321}
 \approx0.0142332.
 }
 \tag{7.7b}
\]

### 7.2 A parity transversal

There is a close explicit upper bound. Let \(N_A(w)\) be the number of
primitive components of a Dyck root \(w\) equal to \(A\), and delete every
root with \(N_A(w)\) odd.

Every edge in (7.1) has two alternatives with \(N_A=k\) and one
alternative with \(N_A=k+1\). Hence the odd-parity class meets every edge.

Giving the component \(A\) weight \(-1\) instead of \(+1\) yields the
signed generating function

\[
 C_-(z)
 =\frac1{1-(\mathcal P(z)-2z^4)}
 =\frac{C(z)}{1+2z^4C(z)}.
 \tag{7.8}
\]

Therefore the odd-parity transversal has generating function
\((C-C_-)/2\). At \(z=1/4\), the square-root coefficient ratio of
\(C_-\) to \(C\) is

\[
 \left(1+\frac1{64}\right)^{-2}
 =\left(\frac{64}{65}\right)^2.
\]

Consequently the full local collision hypergraph satisfies the asymptotic
bracket

\[
 \boxed{
 \frac{275}{19321}
 \le
 \liminf\frac{\tau(\mathcal H_m^{\mathrm{full}})}
                   {\operatorname{Cat}_m}
 \le
 \limsup\frac{\tau(\mathcal H_m^{\mathrm{full}})}
                   {\operatorname{Cat}_m}
 \le
 \frac{129}{8450}.
 }
 \tag{7.9}
\]

Numerically this is

\[
 0.014233\ldots
 \le \frac{\tau(\mathcal H_m^{\mathrm{full}})}
          {\operatorname{Cat}_m}
 \le0.015266\ldots.
\]

Thus arbitrary canonical-row deletions must remove at least about \(1.42\%\)
of all rows to hit every suspended copy of this single seed, while an
explicit parity deletion of about \(1.53\%\) suffices. Determining the exact
constant is reduced to the local \(A/B/DD\) replacement hypergraph.

## 8. Exact-factor component support: a sharp limitation

The global row-deletion barrier does not automatically strengthen inside
the canonical \(\tau=(2\ 3)\) interaction cube. There is an exact component
2-colouring which makes every local seed triple nonmonochromatic.

Write a canonical root in primitive components

\[
 Q_1Q_2\cdots.
\]

Its \(\tau\)-interaction component label is:

* if \(Q_1\) has semilength at least two, then
  \(j=|Q_1|_{\rm semi}-2\), and \(R=Q_2Q_3\cdots\);
* if \(Q_1=10\), then
  \(j=|Q_2|_{\rm semi}-1\), and \(R=Q_3Q_4\cdots\).

Thus the component is \(\mathcal C_{j,R}\). Define

\[
 \chi(\mathcal C_{j,R})
 =
 a(R)+\left\lfloor\frac j2\right\rfloor
 \pmod2,
 \tag{8.1}
\]

where \(a(R)\) counts primitive components of \(R\) equal to \(A\).

Consider a seed triple \(\{UAV,UBV,UDDV\}\). Except when
\(U=\varnothing\) or \(U=10\), the component head is wholly contained in
\(U\). The three labels have the same \(j\), while their suffix
\(A\)-counts are \(k+1,k,k\). Hence their component colours are not all
equal.

For \(U=\varnothing\), the \(A,B\) rows share
\(\mathcal C_{2,V}\), while the \(DD\) row lies in
\(\mathcal C_{0,DV}\). Since

\[
 \left\lfloor\frac22\right\rfloor
 \not\equiv
 \left\lfloor\frac02\right\rfloor\pmod2,
\]

these two components have opposite colours. For \(U=10\), the corresponding
components are \(\mathcal C_{3,V}\) and \(\mathcal C_{1,DV}\), again of
opposite colours. Thus every seed triple is nonmonochromatic.

Switch every interaction component with \(\chi=1\). The result is an exact
factor. No seed triple survives entirely on the canonical side, because no
triple has all component colours zero. No fully transposed copy survives
entirely on the right side either, because no triple has all component
colours one.

This defeats the most direct compensating-seed potential. In general, for
any component-switch child with switch indicator \(\chi\), the disjoint
global seed matching gives

\[
 \vartheta(F_\chi,\beta)
 \ge
 \#\{e\in\mathcal M_*:e\text{ has all component colours }0\}
 +
 \#\{e\in\mathcal M_*:e\text{ has all component colours }1\},
 \tag{8.2}
\]

where \(\mathcal M_*\) is the recursively refined disjoint matching from
Section 7. The first term uses intact canonical packets; the second uses their
\(\tau\)-transposed packets. Old and new rows lie in disjoint component
sides, so all these packets remain disjoint. The colouring (8.1) makes the
right side of (8.2) zero for the entire local-seed hypergraph.

Nor do the immediate two-owner remnants force packets after quotas are
chosen. There are at most \(\operatorname{Cat}_{m-3}\) old seed targets
and the same number of transposed targets. Since

\[
 2\operatorname{Cat}_{m-3}
 <2\operatorname{Cat}_m
 <\rho_1=\frac{2(2m+1)}{m+2}\operatorname{Cat}_m
\]

for \(m>1\), one may assign depth-one quota two to all of them. A surviving
pair then has size only two, below the required packet size three.

This does not prove that the coloured child has small packet-cover value:
mixed old/new owner sets, additional owners, and unrelated collision seeds
remain uncontrolled. It proves that legal component support alone cannot
upgrade the global edit barrier by simply adding intact-left and
intact-right copies of the same seed family.

### 8.1 A compensating mixed-seed theorem

The mixed owner sets can in fact be controlled on a positive-density
subfamily. If a suspended target \(S\) is fixed by
\(\tau=(2\ 3)\), then replacing any canonical owner row \(E\) by its right
side \(\tau E\) preserves ownership of \(S\), because \(\tau E\) owns
\(\tau S=S\). Consequently a three-owner packet survives every independent
choice of component sides, even when its components are nonmonochromatic.

For \(P=10\), the upper-core word is

\[
 \overline P T_0V=01\,T_0V.
\]

Its bits in positions two and three are both one. Hence its complementary
lower target is \(\tau\)-invariant.

More generally, take the prefix-free code

\[
 \mathscr P_{\mathrm{inv}}
 =
 \{10\}\cup
 \{P:P\text{ primitive Dyck and begins }111\}.
 \tag{8.3}
\]

For a primitive prefix of semilength at least three, positions two and
three lie in \(P\). Beginning \(111\) makes the corresponding bits of
\(\overline P\) both zero, so the suspended target is again
\(\tau\)-invariant.

The number of primitive Dyck words of semilength \(p\ge3\) beginning
\(111\) is

\[
 \operatorname{Cat}_{p-1}-\operatorname{Cat}_{p-2}.
 \tag{8.4}
\]

Indeed, writing \(P=1U0\), the word fails to begin \(111\) exactly when the
Dyck word \(U\) begins with the primitive block \(10\), leaving an arbitrary
Dyck suffix of semilength \(p-2\).

The invariant packet count is therefore, for \(m\ge6\),

\[
 \begin{aligned}
 J_m
 &=
 \operatorname{Cat}_{m-5}
 +\sum_{p=3}^{m-4}
 \bigl(\operatorname{Cat}_{p-1}-\operatorname{Cat}_{p-2}\bigr)
 \operatorname{Cat}_{m-p-4}\\
 &=
 \operatorname{Cat}_{m-4}-\operatorname{Cat}_{m-5}.
 \end{aligned}
 \tag{8.5}
\]

The last identity is Catalan convolution: with \(N=m-5\), subtract the
shifted convolution from the tail beginning at index two.

The owner triples are disjoint by primitive-prefix decoding. In every
exact child \(F_\chi\) of the canonical \((2\ 3)\) interaction cube, each
owner is present either as \(E\) or \(\tau E\), and in both cases owns the
same invariant target. Thus

\[
 \boxed{
 \vartheta(F_\chi,\beta)
 \ge
 J_m
 =
 \operatorname{Cat}_{m-4}-\operatorname{Cat}_{m-5}
 }
 \tag{8.6}
\]

for every balanced quota system containing depth one and for every
component-side choice \(\chi\). Since

\[
 \frac{J_m}{\operatorname{Cat}_m}\longrightarrow
 \frac1{256}-\frac1{1024}
 =\frac3{1024},
\]

the entire native interaction cube fails \((\mathrm{FSP}_A)\). At further
row distance \(e\) from a cube child, the right side of (8.6) decreases by
at most \(e\).

This is the requested compensating new-seed inequality. The NAE colouring
eliminates full-left and full-right copies, but it cannot eliminate these
\(\tau\)-invariant mixed triples.

The invariant construction can itself use the full recursive matching
after an invariant first primitive component. Let

\[
 H(z)
 =
 \sum_{p\ge3}
 \bigl(\operatorname{Cat}_{p-1}-\operatorname{Cat}_{p-2}\bigr)z^p
 =
 z(1-z)(C(z)-1)-z^2.
 \tag{8.7}
\]

For every primitive \(P\) counted by \(H\), prefix an independent copy of
the recursively refined matching \(M_*\) in the suffix after \(P\).
Different \(P\)'s are decoded by the first return to zero, and each suffix
copy is internally disjoint. Every resulting target remains
\(\tau\)-invariant because its second and third coordinates lie in \(P\).

The prefix \(P=10\) contributes only the immediate family \(z^5C(z)\):
if a nonempty Dyck context follows \(10\), its first bit occupies coordinate
three and destroys equality with coordinate two. Thus the improved
cube-invariant matching has generating function

\[
 J_*(z)=z^5C(z)+H(z)M_*(z).
 \tag{8.8}
\]

At \(z=1/4\),

\[
 H(1/4)=\frac18,\qquad
 [\sqrt{1-4z}]\,H=-\frac38,
\]

while

\[
 M_*(1/4)=\frac2{139},\qquad
 \frac{[\sqrt{1-4z}]\,M_*}
      {[\sqrt{1-4z}]\,C}
 =\frac{275}{19321}.
\]

Consequently

\[
 \boxed{
 \frac{[z^m]J_*(z)}{\operatorname{Cat}_m}
 \longrightarrow
 \delta_{\mathrm{inv}}
 =
 \frac1{1024}
 +\frac18\frac{275}{19321}
 +\frac3{1112}
 =
 \frac{107897}{19784704}
 \approx0.00545.
 }
 \tag{8.9}
\]

Replacing \(J_m\) by \([z^m]J_*\) in (8.6) gives the strongest audited
cube-universal packet bound.

Let \(\mathfrak Q_\tau\) be the full canonical
\((2\ 3)\)-interaction cube. The disjointness also gives the robust
potential

\[
 \boxed{
 \vartheta(F,\beta)
 +d(F,\mathfrak Q_\tau)
 \ge [z^m]J_*(z).
 }
 \tag{8.10}
\]

Indeed, take a nearest cube child. It has all invariant packets, and one
row removed from that child can hit at most one of their disjoint owner
triples. Thus an \((\mathrm{FSP}_A)\) candidate must lie a positive
\(\delta_{\mathrm{inv}}\)-density away from the entire native cube.

Coordinate relabelling gives the same inequality for every conjugate cube
\(\sigma\mathfrak Q_\tau\). Balanced depth-one quotas are arbitrary, so
the relabelled packet proof does not require the quota assignment itself to
be symmetric. Hence a successful factor must be
\(\delta_{\mathrm{inv}}\)-far from every relabelled one-transposition MSW
switch cube.

## 9. A strict native-component cover lower bound

Although the NAE colouring defeats the monochromatic-copy potential, legal
component switching is more expensive than arbitrary row deletion for the
recursive matching.

Let \(V\) be marker-free in the primitive alphabet: it contains no
\(A,B,DD\). Also require that \(V\) does not begin with \(D\). Consider the
top-level matching edge

\[
 e_V=\{AV,BV,DDV\}.
 \tag{9.1}
\]

The \(A,B\) owners lie in \(\mathcal C_{2,V}\), of size

\[
 \operatorname{Cat}_2+\operatorname{Cat}_3=7.
\]

The other five rows of this component have prefix either an ordinary
primitive component of semilength four, or \(10\) followed by a primitive
component of semilength three. None contains an active marker, and the
marker-free suffix \(V\) creates none. Thus these five rows are inactive
and belong to no edge of the recursive matching.

The \(DD\) owner lies in \(\mathcal C_{0,DV}\), of size two. Its other row
has primitive decomposition

\[
 10,\ 10,\ D,\ V.
\]

Because \(V\) is marker-free and does not begin with \(D\), this row is
also inactive. Therefore each of the two components incident with \(e_V\)
meets no other recursive-matching edge.

Let \(\mathcal S_m\) be this special edge family. Give dual weight two to
every \(e\in\mathcal S_m\) and weight one to every other edge in the
recursive matching \(\mathcal M_*\). For a component meeting a special
edge, the total incident dual weight is exactly two, at most its component
cost, and it meets no other matching edge. Every other component meets at
most one matching edge per selected row, so its incident unit weights sum
to at most its number of rows. This is a feasible dual for the weighted
component-cover problem.

It follows that every set of native \((2\ 3)\)-components whose switched
left rows hit all recursive seed triples has total row cost at least

\[
 \boxed{L_m+|\mathcal S_m|.}
 \tag{9.2}
\]

The generating function for marker-free words not beginning with \(D\) is
\(U_0(z)\). Indeed, if \(F_0=(1+z^2)U_0\) counts all marker-free words,
then a word not beginning in \(D\) is empty or begins with an
\(E\)-component, giving

\[
 1+E F_0=U_0
\]

by the defining equation for \(U_0\). Hence

\[
 |\mathcal S_m|=[z^{m-4}]U_0(z).
 \tag{9.3}
\]

Using

\[
 U_0(z)
 =d^{-1}-\frac{17}{32}d^{-2}\sqrt{1-4z}
 +O(1-4z),
 \qquad d=\frac{1113}{2048},
\]

gives

\[
 \frac{|\mathcal S_m|}{\operatorname{Cat}_m}
 \longrightarrow
 \frac1{256}\cdot
 \frac{17}{64}d^{-2}
 =
 \frac{4352}{1238769}
 \approx0.003513.
 \tag{9.4}
\]

Combining (9.2) with the recursive matching density proves the strict
native-component cover bound

\[
 \boxed{
 \liminf
 \frac{\text{minimum switched-row cost}}{\operatorname{Cat}_m}
 \ge
 \frac{275}{19321}
 +\frac{4352}{1238769}
 \approx0.017746.
 }
 \tag{9.5}
\]

This answers the component-support question in one direction: exact legal
switch support forces a strictly larger deletion density than the
\(275/19321\) arbitrary-row barrier. The exact native component-cover
constant remains open.

There is a second disjoint exceptional family which strengthens (9.5).
For marker-free \(V\) not beginning in \(D\), consider

\[
 e_{10,V}=\{10AV,10BV,10DDV\}.
\]

Its \(A,B\) owners lie in \(\mathcal C_{3,V}\), of cost
\(\operatorname{Cat}_3+\operatorname{Cat}_4=19\). The other seventeen
prefix alternatives contain no active marker, so this component meets no
other recursive-matching edge. Its \(DD\) owner lies in
\(\mathcal C_{1,DV}\), of cost
\(\operatorname{Cat}_1+\operatorname{Cat}_2=3\). The other two rows begin
with a primitive component of semilength three followed by \(D,V\);
because \(V\) is marker-free and does not begin in \(D\), they are
inactive. Thus this component also meets no other matching edge.

We may assign dual weight three to every \(e_{10,V}\), simultaneously with
weight two on the family (9.1) and weight one elsewhere. The two exceptional
families use different component indices and hence do not interfere.
Their count is

\[
 [z^{m-5}]U_0(z),
\]

whose normalized limit is one quarter of (9.4):

\[
 \frac{1088}{1238769}.
\]

Since raising these weights from one to three adds twice this amount, the
exact finite component-cover bound is

\[
 \boxed{
 \text{minimum switched-row cost}
 \ge
 L_m+[z^{m-4}]U_0(z)+2[z^{m-5}]U_0(z).
 }
 \tag{9.5a}
\]

Consequently the strongest audited asymptotic component-cover bound is

\[
 \boxed{
 \liminf
 \frac{\text{minimum switched-row cost}}{\operatorname{Cat}_m}
 \ge
 \frac{275}{19321}
 +\frac{6528}{1238769}
 \approx0.019503.
 }
 \tag{9.6}
\]

## 10. Multistep bounded-support obstruction

The invariant-target argument persists through an arbitrary sequence of
legal transposition component switches.

### 10.1 Exact row lineage

Let \(F\) be any exact factor and \(\tau\) any coordinate transposition.
For every row \(E\in F\), the left vertex \(E\) and right vertex \(\tau E\)
belong to the same overlap component.

Indeed, among the \(n=2m+1\) cyclic \(m\)-windows of \(E\), the two swapped
coordinates have total incidence \(2m=n-1\). They cannot occur exactly one
at a time in every window, which would give total incidence \(n\). Hence
some window contains both or neither and is fixed by \(\tau\). That middle
set directly joins \(E\) on the left to \(\tau E\) on the right.

Consequently every component choice gives a bijective row genealogy

\[
 E\longmapsto E\quad\text{or}\quad E\longmapsto\tau E.
 \tag{10.1}
\]

After any sequence of switches using transpositions supported on a fixed
coordinate set \(B\), each original row has one final descendant
\(g_EE\), where \(g_E\in\operatorname{Sym}(B)\).

### 10.2 Invariant packet matching

Assume first that \(B\) is the aligned set of the first \(b\) finite
positions of the canonical model. More generally, one may start from
\(\sigma F_m^{\mathrm{MSW}}\) and take
\(B=\sigma(\{1,\ldots,b\})\). Let \(\mathcal H_b\) be the class of
primitive Dyck prefixes whose first \(b\) bits are all one.
Its generating function is

\[
 H_b(z)=(zC(z))^b.
 \tag{10.2}
\]

This is the nested first-return decomposition: a primitive Dyck word
beginning with \(b\) rises is counted by \(z^bC(z)^b\).

For every \(P\in\mathcal H_b\), prefix an independent copy of the
recursively refined matching \(M_*\). The first return to zero identifies
\(P\), so all owner triples are disjoint. Their upper-core words begin
with \(b\) zeroes, because the completed prefix is complemented. Hence
their lower targets contain all of \(B\), and are fixed by
\(\operatorname{Sym}(B)\).

Under every switch sequence supported on \(B\), the three descendants of
an owner triple are \(g_1E_1,g_2E_2,g_3E_3\). Each still owns the same
target, since every \(g_i\) fixes it. Thus every final exact factor contains
the full packet matching with generating function

\[
 J_b(z)=(zC(z))^bM_*(z).
 \tag{10.3}
\]

### 10.3 Exact density and support threshold

With \(s=\sqrt{1-4z}\),

\[
 (zC(z))^b=2^{-b}(1-s)^b
 =2^{-b}(1-bs+O(s^2)).
\]

Also \(M_*(1/4)=2/139\), and its square-root coefficient ratio to \(C\)
is \(275/19321\). Therefore

\[
 \boxed{
 \frac{[z^m]J_b(z)}{\operatorname{Cat}_m}
 \longrightarrow
 \delta_b
 =
 2^{-b}
 \left(
 \frac{275}{19321}+\frac b{139}
 \right)
 }
 \tag{10.4}
\]

for fixed \(b\). Direct uniform singular estimates give the same order in
the logarithmic range used next.

Thus every **aligned** bounded-support multistep switch path fails
\((\mathrm{FSP}_A)\). Quantitatively, even allowing \(b=b(m)\), the packet
bound can be \(o(\operatorname{Cat}_m/\sqrt m)\) only if

\[
 \frac{2^b}{b}\gg\sqrt m.
 \tag{10.5}
\]

Equivalently,

\[
 b-\frac12\log_2m-\log_2b\longrightarrow+\infty.
\]

At the rough scale, a successful transposition-switch route must therefore
involve at least

\[
 \frac12\log_2m+\log_2\log m+\omega(1)
\]

coordinates. This is a genuine nonlocal-support lower bound, not merely a
one-cube distance statement, for aligned support.

The alignment qualifier is essential. Simultaneously relabelling an
arbitrary support set \(B\) to the first \(b\) coordinates also relabels
the canonical factor; it does not preserve the relative position of \(B\)
inside the canonical root words. Extending (10.4) to an arbitrary
\(b\)-subset relative to one fixed canonical factor requires a separate
forced-bit Dyck-prefix theorem and is not proved here.

If \(\mathfrak R_b\) denotes the set of all exact factors reachable from
the aligned canonical factor by any finite sequence of transposition
switches supported on \(B\), disjointness gives the robust form

\[
 \vartheta(F,\beta)+d(F,\mathfrak R_b)
 \ge [z^m]J_b(z).
 \tag{10.6}
\]

Thus the obstruction applies to a positive-radius neighbourhood of the
entire multistep reachable set, not only to factors lying exactly on a
switch path.

## 11. Geometry of conjugate native cubes

Pairwise cube separation cannot by itself amplify the packet potential.
For any exact factor \(F\) and transpositions \(\tau,\tau'\),

\[
 F\in\mathfrak Q(F,\tau)\cap\mathfrak Q(F,\tau').
 \tag{11.1}
\]

Thus all one-transposition cubes based at the same factor have pairwise
distance zero. Coordinate conjugation gives

\[
 \sigma\mathfrak Q(F,\tau)
 =
 \mathfrak Q(\sigma F,\sigma\tau\sigma^{-1}),
\]

so the same statement holds around every relabelled canonical factor.

At the opposite extreme, every transposition cube has row-distance
diameter \(t=\operatorname{Cat}_m\). In fact

\[
 F\cap\tau F=\varnothing.
 \tag{11.2}
\]

To prove this for an arbitrary exact factor, suppose
\(E=\tau E'\) with \(E,E'\in F\). A cyclic row \(E'\) has a
\(\tau\)-fixed middle window by the incidence argument in Section 10.
That window belongs to both \(E'\) and \(\tau E'=E\), so exact middle
ownership forces \(E=E'\). But a single transposition cannot stabilize an
unoriented cyclic order of odd length: its induced permutation is not
dihedral. This contradiction proves (11.2).

Consequently

\[
 d(F,\tau F)=t.
\]

The cube contains both endpoints, so its diameter is exactly \(t\), the
maximum possible distance between two \(t\)-row factors.

The conclusion is two-sided:

* there is no useful positive pairwise separation among cubes sharing a
  base factor;
* nevertheless, the invariant packet potential forces an
  \((\mathrm{FSP}_A)\) candidate to be a positive distance from each
  aligned cube individually.

Whether one exact factor can simultaneously stay beyond all conjugate-cube
neighbourhoods is not resolved by this geometry.
