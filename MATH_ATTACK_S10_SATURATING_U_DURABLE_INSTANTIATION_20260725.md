# S10: saturating-cycle and fresh-carrier instantiation of the durable-forest theorem

Date: 2026-07-25

## 0. Exact outcome

Put

\[
n=2m,\qquad
W=\binom{2m}{m},\qquad
N_q=\binom{2m}{m-q},\qquad
H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed. This report attempts to instantiate the positive
durable-forest theorems of S9 using:

1. a \(q=1\) saturating Boolean cycle projected to a Johnson cycle; and
2. the freshly rematched lower-carrier strips of lane U.

The attempt yields a genuine partial multidepth forest, a maximal
Hamilton packet which fuses exponentially many strips into one component,
and exact obstructions to both maximal-packet tiling and black-box
saturating-cycle fusion.

### Positive part

Every matched U strip gives a directed cycle of \(2\ell\) middle owners
whose arcs are jointly lower/upper durable through all symmetric depths
\(0,\ldots,R-1\). Cutting once per strip gives

\[
p=\frac{W-u_0}{2\ell}
\]

actual durable paths on the selected owners. At U's native depth,

\[
\frac{p+u_0}{W/R}=o(1).
\]

Thus the component arithmetic is genuinely adequate for a depth-\(R\)
truncated band. What is missing there is exact completion of the partial
chain packing to one band SCD; U's literal append-repair does not provide
such a completion.

There is also a stronger integral packet. Freeze \(2\ell-1\) rotor slots
and run a \(q=1\) middle-level Hamilton cycle on the remaining
\(2(m-\ell)+1\) coordinates. The resulting

\[
M=2\ell\binom{2(m-\ell)+1}{m-\ell}
=(1+o(1))\,4\ell\,4^{-\ell}W
\]

owners have pairwise disjoint U targets and form one durable directed
cycle; one cut makes one path. This packet is the largest possible within
its fixed-slot standard-strip family.

### Gaussian-depth failure of the present instantiations

At \(H=A\sqrt m\), the current sources do not construct a forest with
\(o(W/H)\) components.

1. The \(q=1\) saturating cycle has perfect lower colours, but no proved
   near-rainbow upper-union ledger. Its exact two-sided component count is
   controlled by an upper collision deletion plus a boundary Hall matching,
   neither bounded by the saturating theorem.
2. U's certified strip arcs have depth only \(R=o(\sqrt{\log m})\) under
   the proved matching regime. They cannot be credited as depth-\(H\)
   durable arcs.
3. Even allowing arbitrary deeper flag extensions, the frozen internal
   \(+1\) arcs of the U strips break into at least
   \[
   (1-o(1))\frac W\ell
   \]
   deep path segments. Achieving \(o(W/H)\) components requires
   \[
   (1-o(1))\frac W\ell
   \]
   full-lifetime external durable arcs leaving the selected strips
   (possibly through residual owners).

The one-way bridge is locally feasible and has an exact
\((2r-1)\)-coordinate collar criterion. It can be iterated throughout the
Hamilton packet above. It still does not give a global factorization:
minimal-length maximal packets collide pairwise at their deepest row when
\(3\ell\le m+1\). More generally, when \(g=\ell-r\ge1\) and
\(3\ell-g\le m\), their number is at
most

\[
\frac1g\binom{2m}{g-1}.
\]

In particular maximal packets need
\(g\ge(4\log2+o(1))H/\log m\) before the trace count even permits enough
Gaussian top-class packets. Separately, a relative relabelling argument
shows that the two marginal existence theorems can coexist while sharing
only \(O(W/m)=o(W/\ell)\) first-level compatible arcs.

There is also a universal correction to S9's switch route:

\[
\boxed{\text{the split graph of every positive-radius Boolean durable
system is }C_4\text{-free}.}
\]

Hence no two distinct durable cycles can be fused by a reciprocal two-edge
switch. Only direct one-way path splicing or alternating trades of length
at least six remain.

Within the U/Hamilton packet architecture, the unresolved construction is
not another support or histogram statement. It is a joint selection of:

* one nested integral Gaussian-depth flag system;
* target-disjoint \(k(m)\)-strip Hamilton prefixes with \(k(m)\to\infty\)
  across all exact lifetime classes;
* one-port-per-module, full-collar path fusion;
* and an exact residual-owner band completion.

If the prefix factorization existed, its total component count would be
\(O_A(W/(Hk))+O(H^2)+W/(m+1)=o(W/H)\). No such factorization is
proved here.
The two black-box instantiations and the maximal-packet tiling are
exhausted. Truncated cross-skeleton prefixes are the surviving route
identified inside this architecture. Different flag systems,
non-Hamilton modules, jointly designed saturation, and alternating trades
of length at least six are not ruled out.

---

## 1. The \(q=1\) saturating Johnson cycle

Apply the saturating-cycle theorem in \(B_{2m}\) to ranks \(m-1,m\). Write
the resulting alternating cycle as

\[
S_i\subset X_i\supset S_{i+1}
\qquad(i\in\mathbb Z/N_1\mathbb Z),
\tag{1.1}
\]

where the \(S_i\)'s exhaust
\(\binom{[2m]}{m-1}\) and the \(X_i\)'s are \(N_1\) distinct middle sets.
Projecting away the lower vertices gives the directed Johnson cycle

\[
e_i:X_i\longrightarrow X_{i+1}.
\tag{1.2}
\]

Its lower and upper colours are

\[
X_i\cap X_{i+1}=S_{i+1},
\tag{1.3}
\]

\[
U_i=X_i\cup X_{i+1}\in\binom{[2m]}{m+1}.
\tag{1.4}
\]

Thus the lower colours are exactly rainbow; the upper colours need not be.

Let \(J\) be a nonempty set of deleted cycle edges. The retained graph is
a spanning directed path forest on the \(N_1\) used owners with exactly
\(|J|\) components.

### Theorem 1.1 (exact two-sided depth-one criterion)

For every nonempty \(J\), the lower boundary-Hall system passes
canonically. The retained forest extends to a two-sided depth-one band SCD
if and only if:

1. the retained upper colours
   \[
   \{U_i:i\notin J\}
   \tag{1.5}
   \]
   are pairwise distinct; and
2. the balanced graph
   \[
   \{X_{i+1}:i\in J\}
   \longleftrightarrow
   Y^+(J):=
   \binom{[2m]}{m+1}\setminus\{U_i:i\notin J\},
   \tag{1.6}
   \]
   with adjacency \(X\subset U\), has a perfect matching.

#### Proof

Every retained tail \(X_i\) is forced to take the lower facet \(S_{i+1}\).
These targets are distinct. If \(e_i\) is deleted, the corresponding
terminal \(X_i\) contains the omitted target \(S_{i+1}\). Assigning it
there gives a bijection onto the full lower rank, so the lower boundary
test passes.

On the upper side, every retained edge forces its head \(X_{i+1}\) to the
cofacet \(U_i\). Injectivity of these forced targets is necessary. When it
holds, the unforced owners are exactly the sources indexed by \(J\), and
the unused cofacets are exactly \(Y^+(J)\); both shores have size \(|J|\).
The recursive boundary-Hall theorem now gives condition 2, with necessity
and sufficiency. \(\square\)

Define

\[
a_U=|\{i:U_i=U\}|,
\qquad
d^+=\sum_U(a_U-1)_+
    =N_1-|\{U_i:i\in\mathbb Z/N_1\mathbb Z\}|.
\tag{1.7}
\]

Collision removal alone requires exactly

\[
\max\{1,d^+\}
\tag{1.8}
\]

edge deletions: all but one occurrence of every repeated colour must be
deleted, and a rainbow cycle must still be cut once. Let

\[
k^+(C)=
\min\{|J|:J\ne\varnothing\text{ satisfies Theorem 1.1}\}.
\tag{1.9}
\]

The exact full component count, leaving the

\[
W-N_1=\frac{W}{m+1}
\]

omitted middle owners as radius-zero singletons, is

\[
\boxed{
\frac{W}{m+1}+k^+(C).}
\tag{1.10}
\]

If the saturating cycle is union-rainbow, then deleting one edge and using
its cofacet at the unique source gives \(k^+(C)=1\), hence

\[
\frac{W}{m+1}+1=o(W/H).
\tag{1.11}
\]

This ideal case would solve the entire depth-one durable component gate.

### What saturation actually proves

For a fixed cofacet \(U\), the \(U\)-coloured edges lie on the \(m+1\)
middle facets of \(U\). Since the projected graph is one simple cycle and
is much longer than \(m+1\), those edges form disjoint paths rather than a
closed component. Therefore

\[
a_U\le m.
\tag{1.12}
\]

This yields only

\[
|\{U_i\}|\ge\left\lceil\frac{N_1}{m}\right\rceil,
\tag{1.13}
\]

which permits

\[
d^+=\Theta(W).
\]

Even an independently proved estimate \(d^+=o(W/H)\) would not finish the
argument without the boundary matching (1.6). Thus the first black-box
instantiation stops at an exact two-sided near-rainbow-plus-Hall theorem
which is absent from the saturating-cycle result.

---

## 2. Fresh lower-carrier strips are genuinely durable

Use the notation of
MATH_ATTACK_U_TWO_SIDED_LOWER_CARRIER_GROWING_BAND_20260725.md:

\[
L=\log m,\qquad \lambda=\log L,
\]

\[
R\to\infty,
\qquad
\frac{R^2\lambda}{L}\to0,
\qquad
\ell=\left\lfloor\frac{L}{64R\lambda}\right\rfloor,
\qquad
s=2\ell.
\tag{2.1}
\]

For one selected strip
\(\alpha=(C_\alpha,D_\alpha,\gamma_\alpha)\), write its active cyclic
order as \((z_t^\alpha)_{t\in\mathbb Z_s}\) and put

\[
v_{\alpha,i}
=C_\alpha\cup I_{\gamma_\alpha}(i,\ell).
\tag{2.2}
\]

For \(0\le q\le R\), define

\[
L_q(v_{\alpha,i})
=C_\alpha\cup I_{\gamma_\alpha}(i+q,\ell-q),
\tag{2.3}
\]

\[
U_q(v_{\alpha,i})
=C_\alpha\cup I_{\gamma_\alpha}(i-q,\ell+q),
\tag{2.4}
\]

\[
R_q(v_{\alpha,i})=[2m]\setminus U_q(v_{\alpha,i}).
\tag{2.5}
\]

The U matching makes every displayed lower target and every displayed
upper target distinct across all selected strips. Hence (2.3)--(2.5) are
integral symmetric radius-\(R\) flags on the \(sp\) selected owners. The
additional U lower rows \(R<q\le2R\) have no upper partners and are not part
of this symmetric flag system.

### Theorem 2.1 (exact strip durability)

For every strip, every \(i\), and every \(0\le h<R\),

\[
L_h(v_{\alpha,i})\cap L_h(v_{\alpha,i+1})
=L_{h+1}(v_{\alpha,i}),
\tag{2.6}
\]

\[
R_h(v_{\alpha,i})\cap R_h(v_{\alpha,i+1})
=R_{h+1}(v_{\alpha,i+1}).
\tag{2.7}
\]

Thus the cyclic \(+1\) arcs form a fully durable directed cycle through all
certified symmetric depths.

#### Proof

Two consecutive active intervals of length \(\ell-h\) have intersection
the interval beginning one step later and having length \(\ell-h-1\),
which is (2.6). Dually,

\[
U_h(v_{\alpha,i})\cup U_h(v_{\alpha,i+1})
=U_{h+1}(v_{\alpha,i+1});
\]

complementation gives (2.7). \(\square\)

Cutting one arc per selected strip gives exactly

\[
\boxed{
p=\frac{W-u_0}{2\ell}
  =(1-o(1))\frac{W}{2\ell}}
\tag{2.8}
\]

durable path components on the selected owners.

### Corollary 2.2 (the native component ledger is small)

If every unselected middle owner is provisionally made a singleton, the
number of components is \(p+u_0\), and

\[
\boxed{p+u_0=o(W/R).}
\tag{2.9}
\]

#### Proof

From (2.1),

\[
\frac{pR}{W}
\le \frac{R}{2\ell}
\sim 32\frac{R^2\lambda}{L}=o(1).
\tag{2.10}
\]

The exact U leave identity is

\[
u_0=W-N_{2R}+\delta,
\qquad
0\le\delta\le \frac{WL^{-9}}{3R+1}.
\tag{2.11}
\]

Uniform expansion of the central binomial ratio gives

\[
W-N_{2R}=(4+o(1))\frac{R^2}{m}W.
\tag{2.12}
\]

Consequently

\[
\frac{Ru_0}{W}
=(4+o(1))\frac{R^3}{m}+O(L^{-9})=o(1),
\tag{2.13}
\]
because (2.1) implies \(R=o(\sqrt{L/\lambda})\). Combining
(2.10) and (2.13) proves (2.9). \(\square\)

This corollary is component arithmetic, not an exact SCD completion.
At depth \(q\), the selected flags use only \(sp\) of the \(N_q\) lower
targets and \(sp\) of the \(N_q\) upper targets. The literal U repair
appends every uncovered mask to a word, but does not match the residual
targets to residual owners in nested chains. Rank counts and injectivity
of the selected flags do not imply that completion. Therefore Theorem
2.1 is a genuine integral partial durable forest, but not yet an
instantiation of S9 inside one full exact factor.

---

## 3. Why the same strips do not reach Gaussian depth

### 3.1 The certified-depth mismatch

At \(H=\lceil A\sqrt m\rceil\), the same number \(p\) of native strip
components satisfies

\[
\frac{p}{W/H}
=(1-o(1))\frac{H}{2\ell}
\sim 32A\frac{R\sqrt m\,\lambda}{L}
\longrightarrow\infty.
\tag{3.1}
\]

More importantly, Theorem 2.1 certifies its arcs only through depth \(R\).
In an exact Gaussian band, the number of owners whose lifetime is at most
\(R\) is

\[
W-N_{R+1}=O\!\left(\frac{R^2}{m}W\right)=o(W).
\tag{3.2}
\]

Thus almost all owners have common lifetime beyond the certified collar.
No internal arc between two such owners can be counted in the S9 durable
forest until all deeper lower and upper identities have actually been
supplied. Repetition of a depth-\(R\) target occurrence is not such a
supply.

### 3.2 The leading-order ceiling for the one-shot full-row matching proof

Consider rerunning the literal U hypergraph with \(R\) replaced by a
desired radius \(h\). Its exact uniformity is

\[
\kappa=2\ell(3h+1)=(6+o(1))\ell h.
\tag{3.3}
\]

For every middle target \(X\), each strip through \(X\) contains exactly
two immediate upper cofacets of \(X\). The stabilizer of \(X\) is
transitive on its \(m\) cofacets. Hence some pair consisting of \(X\) and
an immediate cofacet has codegree at least

\[
\Gamma\ge \frac{2D_0}{m}.
\tag{3.4}
\]

For \(h=O(\sqrt m)\), the maximum degree \(D\) and \(D_0\) differ by at
most a constant depending on the fixed Gaussian window. Therefore the
ABKV hypothesis used by U,

\[
e^{2\kappa}\Gamma\log D=o(D),
\tag{3.5}
\]

forces the finite necessary relation

\[
2\kappa
\le
\log m-\log\log D+\log\frac D{D_0}-\log2-\omega(1).
\tag{3.5a}
\]

Since \(D/D_0=\Theta_A(1)\), this yields

\[
\boxed{12\ell h+4\ell\le(1+o(1))\log m.}
\tag{3.6}
\]

If the extra lower rows \(h<q\le2h\) are discarded and only the symmetric
rows are put in the matching hypergraph, then

\[
\kappa=2\ell(2h+1)=(4+o(1))\ell h
\]

and the same argument gives the slightly weaker but still decisive bound

\[
\boxed{8\ell h+4\ell\le(1+o(1))\log m.}
\tag{3.7}
\]

If a one-shot strip matching covers \(W-o(W)\) middle owners, its initial
component count is \((1-o(1))W/(2\ell)\). Making this
\(o(W/h)\) requires

\[
\frac{\ell}{h}\longrightarrow\infty.
\tag{3.8}
\]

Equations (3.7) and (3.8) imply

\[
\boxed{h=o(\sqrt{\log m}).}
\tag{3.9}
\]

This is a theorem about the full-row ABKV certification used in U, not a
theorem that no other matching or deterministic construction exists.

There is a separate, purely integral capacity obstruction at Gaussian
depth. Assume \(\ell>2H\), as required for the literal asymmetric rows.
A literal asymmetric U strip consumes \(2\ell\) distinct targets
in rank \(m-2H\). Hence every target-disjoint strip matching obeys

\[
2\ell p\le N_{2H}
=(e^{-4A^2}+o(1))W.
\tag{3.10}
\]

If only symmetric rows are retained, assume \(\ell>H\). That version
obeys

\[
2\ell p\le N_H
=(e^{-A^2}+o(1))W.
\tag{3.11}
\]

Thus a one-shot equal-row Gaussian strip matching necessarily leaves a
middle fraction at least \(1-e^{-4A^2}+o(1)\) in the asymmetric case and
at least \(1-e^{-A^2}+o(1)\) in the symmetric case. A different
residual flag construction would be required even if the matching itself
could be certified.

### 3.3 Frozen-rotor deep-run obstruction

The next statement does not assume that the unknown deeper flags continue
canonically. It allows arbitrary integral extensions and uses only the
fixed internal \(+1\) rotor arcs.

### Theorem 3.1 (deep internal runs force shallow separators)

Let the \(2\ell\) owners of a U strip be

\[
v_i=C\cup\{z_i,z_{i+1},\ldots,z_{i+\ell-1}\}
\qquad(i\bmod 2\ell).
\tag{3.12}
\]

Suppose they are assigned arbitrary nested integral lower flags. No block

\[
v_i\to v_{i+1}\to\cdots\to v_{i+\ell+1}
\tag{3.13}
\]

of retained internal arcs can have all its vertices of lifetime at least
\(\ell+1\) and all its arcs fully durable.

#### Proof

Write

\[
\alpha_h(v)=L_h(v)\setminus L_{h+1}(v).
\]

Durability of \(v_j\to v_{j+1}\) gives

\[
\alpha_h(v_j)=\alpha_{h-1}(v_{j+1})
\qquad(1\le h\le\ell).
\tag{3.14}
\]

At level zero, the fixed rotor edge gives

\[
\alpha_0(v_j)=v_j\setminus v_{j+1}=\{z_j\}.
\tag{3.15}
\]

Iterating (3.14) along (3.13) forces

\[
\alpha_h(v_i)=z_{i+h}
\qquad(0\le h\le\ell).
\tag{3.16}
\]

After the first \(\ell\) deletions one has \(L_\ell(v_i)=C\), while
(3.16) demands that the next deleted element be
\(z_{i+\ell}\notin C\). This contradicts
\(\alpha_\ell(v_i)\subseteq L_\ell(v_i)\). \(\square\)

Now place selected U-strip owners inside any exact Gaussian band SCD, and
let \(S\) and \(M\) be respectively the numbers of selected owners with
lifetime at most \(\ell\) and at least \(\ell+1\). Delete every
forest arc outside the frozen internal \(+1\) set and let
\(k_{\rm int}\) be the number of remaining internal path components.
Theorem 3.1 says that a run
of deep vertices has length at most \(\ell+1\). Therefore, exactly,

\[
\boxed{M\le(\ell+1)(S+k_{\rm int}),}
\qquad
\boxed{k_{\rm int}\ge\frac{M}{\ell+1}-S.}
\tag{3.17}
\]

For the U parameters, \(\ell=o(m^{1/3})\), and exact SCD lifetime counts
give

\[
S\le W-N_{\ell+1}
=O\!\left(\frac{\ell^2}{m}W\right)
=o(W/\ell).
\tag{3.18}
\]

Since the selected U owners number \(W-u_0=(1-o(1))W\), it follows that

\[
\boxed{k_{\rm int}\ge(1-o(1))\frac W\ell.}
\tag{3.19}
\]

Within one strip, two distinct owners are Johnson adjacent only when their
cyclic phases differ by \(+1\) or \(-1\). The canonical first deletion at
\(v_i\) is \(z_i\). The \(-1\) neighbor would instead require deletion of
\(z_{i+\ell-1}\), and so cannot be a durable successor. Consequently every
durable forest arc outside the frozen internal \(+1\) arc set leaves that
strip (possibly for a residual owner).

Let \(b\) count all such external arcs. Deleting them leaves the internal
components counted above, and each external arc can reduce the number of
components by at most one. Thus every fully durable forest with
\(c(D)=o(W/H)\), where \(H/\ell\to\infty\), must have

\[
\boxed{b\ge(1-o(1))\frac W\ell=(2-o(1))p.}
\tag{3.20}
\]

This is a genuine multidepth obstruction: merely cutting and joining the
original strip cycles once each is short by a factor asymptotic to two.

---

## 4. Exact one-way port geometry

The obstruction (3.20) does not say that the required bridges are locally
impossible. Their exact collar can be written explicitly.

For a radius-\(r\) flag at owner \(v\), put

\[
\alpha_h(v)=L_h(v)\setminus L_{h+1}(v),
\qquad
\beta_h(v)=R_h(v)\setminus R_{h+1}(v)
\quad(0\le h<r),
\tag{4.1}
\]

where \(R_h(v)\) is the descending upper-complement flag.

### Lemma 4.1 (deletion-symbol collar)

A Johnson cover \(v\to w\) is durable through radius \(r\) if and only if

\[
\alpha_0(v)=\beta_0(w)=v\setminus w,
\tag{4.2}
\]

and, for every \(1\le h<r\),

\[
\alpha_h(v)=\alpha_{h-1}(w),
\qquad
\beta_h(w)=\beta_{h-1}(v).
\tag{4.3}
\]

#### Proof

The level-zero lower intersection removes \(v\setminus w\) from \(v\),
and the upper-complement intersection removes the same coordinate from
\(R_0(w)\), giving (4.2). At level \(h\), two equal-sized sets whose
intersection has codimension one differ in one element. Comparing the
level-\(h\) identity with the level-\((h-1)\) identity gives (4.3).

Conversely, (4.2) gives both level-zero intersection identities.
Inductively, if the identities hold through level \(h-1\), then the two
level-\(h\) flags lie in the preceding common set; (4.3) deletes exactly
the one element by which they differ. Their intersection is therefore the
specified level-\((h+1)\) flag, on both sides. \(\square\)

For canonical U strips, let \(A=(\alpha,i)\), \(B=(\beta,j)\), and write

\[
a_t=z^\alpha_{i+t},
\qquad
b_t=z^\beta_{j+t}.
\tag{4.4}
\]

### Corollary 4.2 (exact strip-to-strip collar)

For \(1\le r<\ell\), the arc \(A\to B\) is durable through radius \(r\)
if and only if

\[
v_A\setminus v_B=\{a_0\},
\qquad |v_B\setminus v_A|=1,
\tag{4.5}
\]

and

\[
\boxed{
(b_{-r},\ldots,b_{r-2})
=(a_{-r+1},\ldots,a_{r-1}).}
\tag{4.6}
\]

Indeed, the canonical symbols are

\[
\alpha_h(A)=a_h,qquad \beta_h(A)=a_{-h-1},
\]

and similarly for \(B\); Lemma 4.1 gives (4.6) term by term.

If the old ports \(A_i\to A_{i+1}\) and \(B_j\to B_{j+1}\) are cut, the
one-way bridge \(A_i\to B_{j+1}\) therefore requires, in addition to
oriented Johnson adjacency,

\[
\boxed{
z^\alpha_{i+t}=z^\beta_{j+t}
\quad(-r+1\le t\le r-1).}
\tag{4.7}
\]

Thus the port collar is an identical centered window of length \(2r-1\).

### Proposition 4.3 (an explicit target-disjoint bridge)

Let \(A=(C,D,(a_t)_{t\bmod2\ell})\), choose \(c\in C\) and \(x\in D\),
and fix \(1\le r<\ell\). Define a second strip by

\[
C'=(C\setminus\{c\})\cup\{x\},
\qquad
D'=(D\setminus\{x\})\cup\{a_\ell\},
\tag{4.8}
\]

and by the active cyclic order

\[
b_t=a_t\quad(t\ne\ell),
\qquad b_\ell=c.
\tag{4.9}
\]

Then

\[
B_1=A_0\setminus\{a_0\}\cup\{x\},
\tag{4.10}
\]

and \(A_0\to B_1\) is durable through radius \(r\). Moreover every
canonical target of the A strip omits \(x\), whereas every canonical
target of the B strip contains \(x\); hence the complete target sets of
the two strips are disjoint.

#### Proof

The new active ground set is

\[
[2m]\setminus(C'\cup D')
=\bigl(\{a_t:t\bmod2\ell\}\setminus\{a_\ell\}\bigr)
 \cup\{c\},
\]

so (4.9) is a valid cyclic order. Equation (4.10) follows directly from
the active interval at phase \(1\). Since \(r<\ell\), the centered window
in (4.7) does not meet position \(\ell\), and (4.9) supplies the entire
collar. Equation (4.10) supplies the oriented Johnson adjacency.

Finally \(x\in D\), so every A target omits \(x\); while \(x\in C'\), so
every B target contains \(x\). \(\square\)

Thus there is no local bridge nonexistence theorem. The obstruction is to
selecting approximately \(W/\ell\) such bridges simultaneously inside one
exact target-disjoint nested system.

### Theorem 4.4 (universal no-two-switch theorem)

For every positive-radius integral Boolean flag system, its durable split
graph is \(C_4\)-free. Equivalently, if \(a\to a'\) and \(b\to b'\) are
vertex-disjoint durable arcs, the two cross arcs

\[
a\to b',\qquad b\to a'
\tag{4.11}
\]

cannot both be durable.

#### Proof

Put \(d(x)=\alpha_0(x)\) and \(u(y)=\beta_0(y)\). Every durable arc
\(x\to y\) satisfies

\[
d(x)=u(y)=x\setminus y.
\tag{4.12}
\]

If all four arcs in the alleged rectangle existed, (4.12) would make

\[
d(a)=d(b)=u(a')=u(b')=:c.
\]

Put \(S=a\setminus\{c\}\) and \(T=b\setminus\{c\}\). Both targets
\(a'\) and \(b'\) would contain both \(S\) and \(T\). If \(S=T\), then
\(a=b\). If \(S\ne T\), their union has size at least \(m\); existence of
an \(m\)-set containing it forces \(|S\cup T|=m\), and that containing
\(m\)-set is unique. Hence \(a'=b'\). Both conclusions contradict vertex
disjointness. \(\square\)

Consequently the reciprocal two-edge cycle switch in the abstract S9
digraph theorem has no Boolean positive-radius instance. Direct one-way
splicing remains possible, as Proposition 4.3 shows. Alternating trades,
if useful, must have length at least six.

---

## 5. A maximal fixed-skeleton Hamilton packet

Proposition 4.3 can be iterated for exponentially many strips without one
target collision. This is the positive construction in this report.

Put

\[
s=m-\ell.
\tag{5.1}
\]

Fix a set \(Q\) of \(2\ell-1\) coordinates, assign its coordinates in a
fixed order to all cyclic slots \(t\ne\ell\), and put

\[
P=[2m]\setminus Q,\qquad |P|=2s+1.
\tag{5.2}
\]

For an inclusion

\[
C\subset E\subset P,\qquad |C|=s,\quad |E|=s+1,
\tag{5.3}
\]

define the standard strip \(\mathcal S(C,E)\) to have core \(C\),
exterior \(D=P\setminus E\), and active slot \(\ell\) occupied by the
unique coordinate \(E\setminus C\). All other active slots use the fixed
ordered set \(Q\).

Invoke the \(q=1\) middle-level saturating-cycle theorem on \(P\). Write
its alternating Hamilton cycle as

\[
E_0,C_0,E_1,C_1,\ldots,E_{K-1},C_{K-1},E_0,
\tag{5.4}
\]

where

\[
K=\binom{2s+1}{s},
\qquad
C_j\subset E_j,\ E_{j+1}
\quad(j\bmod K).
\tag{5.5}
\]

Let \(\mathcal S_j=\mathcal S(C_j,E_j)\), and define

\[
y_j=E_j\setminus C_j,\qquad
x_j=E_{j+1}\setminus C_j,\qquad
c_j=E_{j+1}\setminus C_{j+1}.
\tag{5.6}
\]

The simplicity of the Hamilton cycle gives

\[
x_j\in D_j,\qquad c_j\in C_j,
\tag{5.7}
\]

and the next strip is obtained by the exact core swap

\[
C_{j+1}=C_j\setminus\{c_j\}\cup\{x_j\},
\]

\[
D_{j+1}=D_j\setminus\{x_j\}\cup\{y_j\},
\qquad
y_{j+1}=c_j.
\tag{5.8}
\]

Write \(V_{j,i}\) for phase \(i\) of strip \(\mathcal S_j\).

### Theorem 5.1 (maximal fixed-skeleton durable packet)

Assume \(2r<\ell\). The \(K\) strips \(\mathcal S_j\) have pairwise
disjoint middle targets, all lower targets through depth \(2r\), and all
upper targets through depth \(r\). If, for every \(j\), the internal port

\[
V_{j,0}\longrightarrow V_{j,1}
\tag{5.9}
\]

is deleted and the one-way bridge

\[
V_{j,0}\longrightarrow V_{j+1,1}
\tag{5.10}
\]

is inserted, the result is one directed cycle on

\[
\boxed{
M=2\ell K
=2\ell\binom{2(m-\ell)+1}{m-\ell}}
\tag{5.11}
\]

owners, and every arc is durable through radius \(r\). Deleting one
bridge gives one integral durable path component on all \(M\) owners.

Moreover, \(K\) is the largest possible number of pairwise
target-disjoint standard strips with this fixed ordered \(Q\)-skeleton and
special slot.

#### Proof

The transformation (5.8) is exactly Proposition 4.3, with the coordinate
\(y_j\) occupying slot \(\ell\). More explicitly,

\[
V_{j+1,1}
=V_{j,0}\setminus\{q_0\}\cup\{x_j\},
\tag{5.12}
\]

where \(q_0\) is the fixed coordinate in slot zero. The lower deletion
symbols on the bridge obey

\[
\alpha_0(V_{j,0})=\beta_0(V_{j+1,1})=q_0,
\]

\[
\alpha_h(V_{j,0})
=\alpha_{h-1}(V_{j+1,1})=q_h
\qquad(1\le h<r),
\]

and the upper-complement symbols obey

\[
\beta_h(V_{j+1,1})
=\beta_{h-1}(V_{j,0})=q_{-h}
\qquad(1\le h<r).
\tag{5.13}
\]

The special slot \(\ell\) is outside every displayed collar. Lemma 4.1
therefore proves durability of (5.10). The undeleted internal arcs are
durable by Theorem 2.1. Deleting (5.9) turns each strip cycle into the path
from \(V_{j,1}\) to \(V_{j,0}\), and (5.10) joins these paths cyclically in
Hamilton order.

For target disjointness, intersect any strip target with \(P\). If its
active interval avoids slot \(\ell\), the intersection is \(C_j\); if it
contains that slot, the intersection is \(E_j\). Equality between targets
from two different strips would therefore force either

\[
C_j=C_k
\quad\text{or}\quad
E_j=E_k.
\tag{5.14}
\]

The Hamilton cycle visits every \(s\)-set and every \((s+1)\)-set of
\(P\) exactly once, so (5.14) forces \(j=k\). Within one strip, the
cyclic-interval targets in all stated U rows are distinct. This proves
target disjointness.

Finally, phase zero has an active interval avoiding slot \(\ell\), so the
\(P\)-intersection of \(V_{j,0}\) is its core \(C_j\). Any
target-disjoint family with the fixed skeleton must therefore have
distinct cores. There are only \(K\) possible cores, and the construction
uses all of them. \(\square\)

### Corollary 5.1A (symmetric-only packet)

If the extra asymmetric lower rows \(r<q\le2r\) are discarded, every
conclusion of Theorem 5.1 for the symmetric rows \(0\le q\le r\) holds
under the weaker hypothesis \(r<\ell\).

#### Proof

The packet collar uses only positions \(-r+1,\ldots,r-1\), and every
symmetric lower or upper interval has length between \(1\) and
\(2\ell-1\). Thus the collar and trace proofs above remain valid. The
stronger condition \(2r<\ell\) served only to define the extra lower rows
through \(2r\). \(\square\)

For \(\ell=o(m)\), Stirling's central-binomial asymptotic gives

\[
\boxed{
\frac{M}{W}
=(1+o(1))\,4\ell\,4^{-\ell}.}
\tag{5.15}
\]

Thus one maximal packet covers a vanishing fraction of the middle layer,
but it has one component rather than \(K\) strip components. A
hypothetical exact target-disjoint factorization into such packets would
use

\[
(1+o(1))\frac{4^\ell}{4\ell}
=\exp(o(m))
=o(W/H)
\tag{5.16}
\]

components for every fixed Gaussian \(H=A\sqrt m\). The within-packet
bridge and component gates are therefore quantitatively closed.

### 5.2 Exact obstruction to the obvious fixed-split completion

There is no automatic product factorization behind Theorem 5.1. Consider
all middle masks in the two fixed-split slices

\[
\binom{P}{s}\times\binom{Q}{\ell},
\qquad
\binom{P}{s+1}\times\binom{Q}{\ell-1}.
\tag{5.17}
\]

Their total capacity is

\[
B_0
=K\binom{2\ell}{\ell}.
\tag{5.18}
\]

Every lower depth-\(q\) target of a fixed-split packet remains in the two
corresponding product slices, whose combined capacity is

\[
B_q
=K\binom{2\ell}{\ell-q}.
\tag{5.19}
\]

In particular,

\[
\frac{B_1}{B_0}=\frac{\ell}{\ell+1}.
\tag{5.20}
\]

Consequently, any target-disjoint family of fixed-split packets which
covers \(B_0-o(B_0)\) middle masks can keep at most \(B_1\) of those owners
alive at depth one. It forces at least

\[
\frac{B_0}{\ell+1}-o(B_0)
\tag{5.21}
\]

radius-zero owners. The global exact SCD fraction is only

\[
\frac{W-N_1}{W}=\frac1{m+1}.
\tag{5.22}
\]

Since \(\ell<m\), a decomposition of the whole middle layer into complete
fixed-split blocks would force at least

\[
\left(
\frac1{\ell+1}-\frac1{m+1}
\right)W
=\frac{m-\ell}{(\ell+1)(m+1)}W
\]

more radius-zero owners than the exact SCD ledger permits. More
generally,

\[
\frac{B_q}{B_0}
=\frac{\binom{2\ell}{\ell-q}}{\binom{2\ell}{\ell}}
<
\frac{\binom{2m}{m-q}}{\binom{2m}{m}}
=\frac{N_q}{W}
\quad(1\le q\le\ell),
\tag{5.23}
\]

so variable radii confined independently inside complete fixed-split
blocks do not repair the rank deficit.

This does not obstruct mixing incomplete packets across different
\(P/Q\) splits. It rules out the most direct product completion and shows
that cross-skeleton mixing is mathematically necessary. Also, no exact
even-dimensional wreath factor on the \(2\ell\)-set \(Q\cup\{*\}\) is
being assumed here; such a factor need not exist.

### 5.3 Maximal minimal-length packets collide pairwise

The obstruction becomes stronger at the natural smallest strip length.

### Theorem 5.2 (deepest-collar intersection)

For the literal asymmetric U packet, take

\[
\ell=2r+1.
\tag{5.24}
\]

At its deepest lower row \(q=2r=\ell-1\), the complete target support of
the maximal packet based on \(P\) is

\[
\boxed{
\mathcal L(P)
=\left\{
X\in\binom{[2m]}{m-\ell+1}:
|X\setminus P|\le1
\right\}.}
\tag{5.25}
\]

If \(P\) and \(P'\) are two skeleton grounds of size
\(2(m-\ell)+1\) and

\[
3\ell\le m+1,
\tag{5.26}
\]

then

\[
\mathcal L(P)\cap\mathcal L(P')\ne\varnothing.
\tag{5.27}
\]

Hence no two maximal minimal-length packets can occur in one
target-disjoint band under (5.26).

The same conclusion holds for symmetric-only packets with
\(\ell=r+1\), using their deepest required row \(q=r=\ell-1\).

#### Proof

At \(q=\ell-1\), a lower active interval is a singleton. When it is the
variable slot, the targets run through every
\((m-\ell+1)\)-subset \(E\) of \(P\). When it is a fixed slot
\(a\in[2m]\setminus P\), the targets run through every

\[
C\cup\{a\},
\qquad
C\in\binom{P}{m-\ell}.
\]

This is exactly (5.25).

For two skeleton grounds,

\[
|P\cap P'|
\ge 2\bigl(2(m-\ell)+1\bigr)-2m
=2m-4\ell+2.
\tag{5.28}
\]

Condition (5.26) makes the last quantity at least
\(m-\ell+1\). Choose an \((m-\ell+1)\)-set
\(X\subseteq P\cap P'\). Then \(X\) belongs to both supports in (5.27).
The symmetric-only statement has the identical deepest-row support.
\(\square\)

The collision persists with a quantified amount of slack.

### Theorem 5.3 (trace bound for maximal packets)

Use symmetric depth \(r\), put

\[
\ell=r+g,\qquad g\ge1,
\tag{5.29}
\]

and assume \(3\ell-g\le m\). Any target-disjoint family of maximal
fixed-skeleton packets has size at most

\[
\boxed{
B_{\max}(g)
\le \frac1g\binom{2m}{g-1}.}
\tag{5.30}
\]

#### Proof

At lower depth \(r\), an active interval has length \(g\). Exactly \(g\)
cyclic intervals contain the variable slot. After removing that slot,
they give \(g\) distinct \((g-1)\)-coordinate traces; call their family
\(\mathcal G(P)\). For every \(G\in\mathcal G(P)\), maximality of the
Hamilton packet means that its targets include

\[
E\cup G
\qquad\text{for every}\qquad
E\in\binom{P}{m-\ell+1}.
\]

If packets based on \(P,P'\) shared a trace \(G\), then
\(G\cap(P\cup P')=\varnothing\). Both skeleton grounds lie in the
\((2m-g+1)\)-set \([2m]\setminus G\), so

\[
|P\cap P'|
\ge2m-4\ell+g+1.
\]

The hypothesis \(3\ell-g\le m\) makes this at least
\(m-\ell+1\), and therefore permits an \((m-\ell+1)\)-set
\(E\subseteq P\cap P'\). The target \(E\cup G\)
would occur in both packets. Hence the \(g\)-element trace families
\(\mathcal G(P)\) are pairwise disjoint. There are only
\(\binom{2m}{g-1}\) possible traces, proving (5.30). \(\square\)

In the Gaussian top-class application, put \(r=H\) and assume
\(\ell=H+g=o(m)\). Covering that class by such packets would require

\[
B_{\rm need}
=(1+o(1))\frac{e^{-A^2}4^{H+g}}{4(H+g)}.
\tag{5.31}
\]

Therefore maximal packets are impossible whenever

\[
\frac1g\binom{2m}{g-1}
=o\!\left(\frac{4^{H+g}}{H+g}\right).
\tag{5.32}
\]

In particular this holds for \(g=o(H/\log m)\). The first scale not
excluded by this trace count must satisfy

\[
g\log\frac{2em}{g}
\ge(1+o(1))H\log4,
\]

and hence, for \(H=A\sqrt m+O(1)\),

\[
\boxed{
g\ge(4\log2+o(1))\frac{H}{\log m}.}
\tag{5.33}
\]

This is a necessary slack for maximal Hamilton packets, not a sufficient
packing theorem.

For Gaussian \(r=A\sqrt m+O(1)\), condition (5.26) holds eventually.
Thus at the minimal slack \(g=1\), the maximal packet cannot be the tiling
unit of a Gaussian exact factor: target disjointness permits at most one,
although a scalar lifetime count would require exponentially many.

For comparison, let

\[
V_r=N_r-N_{r+1}\quad(0\le r<H),
\qquad
V_H=N_H
\tag{5.34}
\]

be the exact lifetime-class sizes. For symmetric packets, the minimal
choice \(\ell_r=r+1\) has

\[
M(\ell_r)
=(1+o(1))(r+1)4^{-r}W.
\tag{5.35}
\]

Ignoring collisions, the clipped top class would need only

\[
\frac{V_H}{M(\ell_H)}
=(1+o(1))\frac{e^{-A^2}4^H}{H}
=\exp\bigl((2A\log2+o(1))\sqrt m\bigr)
=o(W/H)
\tag{5.36}
\]

packets. The sum over the smaller positive radii \(1\le r<H\) is \(o\) of
this top contribution, so the positive-radius total has the top order.
The radius-zero class instead contributes \(W/(m+1)\) singleton
components; it is larger than this packet count but still \(o(W/H)\).
Therefore the scalar component ledger has enormous slack; Theorem 5.2
shows that exact target packing, not the number of packets, is the
decisive failure.

For literal asymmetric U packets one cannot even assign the whole top
lifetime class: those packets require distinct lower targets at depth
\(2H\), so they cover at most \(N_{2H}<N_H\) of its owners. A full SCD
must prune to symmetric rows or use a different construction.

Maximal packets are therefore exhausted. Long maximal packets are also
unnecessary for the component ledger. A consecutive \(k\)-strip segment
of the Hamilton packet has \(2\ell k\) owners, pairwise disjoint targets,
and one durable path component. If, for a common \(k=k(m)\to\infty\), the
exact radius classes could be partitioned into such symmetric prefixes
with \(\ell_r=\Theta(r)\), allow the final group in each class to be one shorter
\((<k)\)-strip Hamilton prefix, and fewer than \(2\ell_r\) unmatched
owners may remain as singletons. Under this convention the component
count is

\[
\sum_{r=1}^{H-1}
O\!\left(\frac{V_r}{r k}+r\right)
+O\!\left(\frac{V_H}{Hk}+H\right).
\tag{5.37}
\]

Uniformly for \(1\le r\le H=O(\sqrt m)\),

\[
V_r
=N_r-N_{r+1}
=\frac{2r+1}{m+r+1}N_r,
\]

and therefore

\[
V_r
=O\!\left(\frac{r+1}{m}W e^{-r^2/m}\right),
\]

so (5.37) is

\[
\boxed{
O_A\!\left(\frac{W}{Hk}\right)+O(H^2)
=o(W/H).}
\tag{5.38}
\]

The radius-zero class itself has \(W/(m+1)=o(W/H)\) owners. Thus slowly
growing prefixes would already meet the total component target.

They also meet the stronger weighted rotor statistic used in RSCD. With the conservative
choice of leaving fewer than \(2\ell_r\) unmatched owners as singletons
in each positive radius class,

\[
p_r\le\frac{V_r}{2\ell_r k}+O(\ell_r).
\tag{5.39}
\]

For \(\ell_r=\Theta(r)\),

\[
\sum_{r=0}^H(2r+1)p_r
\le \frac{W}{m+1}
+O\!\left(\frac1k\sum_{r=1}^H V_r\right)
+O(H^3)
=o(W).
\tag{5.40}
\]

Thus the literal toll, not merely an unweighted proxy, is quantitatively
adequate once the integral prefix factorization exists. In particular
(5.40) bounds both
\(\Phi=\sum_r(2r+1)p_r\) and the S9 reset term
\(2\sum_r r p_r\).

What is not proved is the required prefix factorization. A surviving
packet route must pack target-disjoint \(k\)-strip prefixes across
different skeleton grounds, fuse their rows into the exact cross-radius
bijections, and absorb all rounding residues inside one band SCD.

### 5.4 U's matching theorem does not certify the prefix factorization

One might try to rematch whole \(k\)-strip prefixes instead of single
strips. This fails at the hypotheses of the existing near-regular theorem.

For symmetric radius \(r\), one prefix atom uses

\[
a=2\ell k
\]

targets in each of the middle, \(r\) lower, and \(r\) upper parts. Its
uniformity is exactly

\[
\kappa_{\rm sym}=2\ell k(2r+1).
\tag{5.41}
\]

In the full permutation-symmetric catalogue, double counting gives the
degree in a rank-\(q\) part as

\[
D_q=\frac{a|\mathcal E|}{N_q}.
\tag{5.42}
\]

At \(r=A\sqrt m+O(1)\),

\[
\frac{D_0}{D_r}=\frac{N_r}{W}=e^{-A^2}+o(1).
\tag{5.43}
\]

Thus the minimum degree has a fixed relative defect, whereas U's theorem
requires minimum degree at least \(D-f(D)\) with \(f(D)/D=o(1)\).
This is the first failed hypothesis. Restricting every larger rank part
to a specially chosen \(N_r\)-set would remove the numerical defect, but
choosing those parts with nested regular incidence is precisely the
unproved common-owner lifetime construction.

Even granting such a regularization, let \(D\) be its maximum degree and
suppose its minimum degree is \(D-f(D)\), as required by U's theorem.
Every atom through a retained middle owner \(X\) contains at least the two
immediate upper cofacets supplied by the constituent strip containing
\(X\). Therefore, without using transitivity,

\[
\sum_{\substack{Y\supset X\\|Y|=m+1}}d(X,Y)\ge2d(X),
\qquad
\Gamma\ge\frac{2(D-f(D))}{m}
=(2-o(1))\frac Dm.
\tag{5.44}
\]

The U hypothesis \(e^{2\kappa}\Gamma\log D=o(D)\) would then force the
following leading-order necessary bound; the left side is the exact
quantity \(2\kappa_{\rm sym}\):

\[
\boxed{
8\ell k r+4\ell k
\le(1+o(1))\log m.}
\tag{5.45}
\]

For literal asymmetric atoms, whose uniformity is
\(2\ell k(3r+1)\), the bound becomes

\[
\boxed{
12\ell k r+4\ell k
\le(1+o(1))\log m.}
\tag{5.46}
\]

Since \(\ell\ge r+1\), even (5.45) requires

\[
kr^2=O(\log m).
\tag{5.47}
\]

It fails at Gaussian \(r=A\sqrt m\) already for \(k=1\), and a fortiori
for \(k\to\infty\). In addition, U's single-strip pair-codegree upper
bound does not automatically extend to prefix atoms because their
Hamilton bridge constraints correlate all \(k\) strips.

There is also an ordinaryness gap. The unlabelled union of the targets of
\(k\) strips need not uniquely recover its partition into strips, their
order, or the chosen prefix bridges. U's theorem is stated for an ordinary
hypergraph. One would have to prove unique atom reconstruction, quotient
parallel presentations and recompute all degrees/codegrees, or add
port-order labels as extra vertices and audit the new disjointness
constraints. In the last option the added label vertices increase
\(\kappa\), so the finite exponents (5.45)--(5.46) do not apply unchanged.

Finally, the leave estimate produced by that theorem has characteristic
fraction at best on the scale

\[
\exp\!\left(-\Theta\!\left(\frac{\log m}{\kappa_{\rm sym}}\right)\right),
\tag{5.48}
\]

which, in a hypothetically balanced equal-part restriction, does not
certify the per-part \(o(m^{-1/2})\) residual fraction needed for
singleton repair at Gaussian depth when \(\kappa_{\rm sym}\to\infty\).
In the original unbalanced \(2r+1\)-part universe, a total-leave fraction
would need to be \(o(1/(Hr))=o(1/m)\).
This is a limitation of the theorem's guarantee, not a lower bound on the
best possible matching.

Therefore the existing U theorem does not certify the positive prefix
route. A specially restricted near-regular nested catalogue, a
quota-prescribed packing theorem, or a deterministic exact factorization
could still suffice. Recursive independent applications of U's theorem
do not by themselves certify one common flag system.

The quota mismatch is exact. After all lifetime classes above \(r\) have
been placed, the unused portion of every rank-\(q\) part, \(q\le r\),
must have size

\[
N_q-N_{r+1}.
\tag{5.49}
\]

Class \(r\) must consume exactly \(V_r=N_r-N_{r+1}\) targets from every
one of those prescribed residual parts and saturate the rank-\(r\)
boundary. U's theorem seeks an approximately maximum matching in nearly
equal full parts; it neither accepts these quotas nor preserves the
chosen residual sets for the next radius.

---

## 6. Why the two marginal sources do not compose as black boxes

Fix a U flag system and let \(\Pi_1\) be the set of directed Johnson arcs
which pass its depth-one collar. For a fixed source \(X\), its first lower
deletion symbol is fixed. A compatible successor has the form

\[
X\setminus\{d(X)\}\cup\{y\},
\qquad y\notin X.
\]

Therefore

\[
\deg^+_{\Pi_1}(X)\le m,
\qquad
|\Pi_1|\le mW.
\tag{6.1}
\]

The complete directed Johnson graph has exactly \(Wm^2\) arcs, and the
coordinate-permutation group is transitive on them. Let \(C\) be any
projected \(q=1\) saturating cycle, with \(N_1\) arcs, and let \(\pi\) be
a uniformly random coordinate permutation applied to the U system. Then

\[
\mathbb E_\pi|E(C)\cap\pi(\Pi_1)|
=\frac{N_1|\Pi_1|}{Wm^2}
\le\frac{N_1}{m}
\le\frac Wm.
\tag{6.2}
\]

Hence some relative relabelling has at most \(W/m\) common compatible
arcs. Coordinate relabelling preserves both the saturating-cycle theorem
and every U target-disjointness statement. Since \(\ell=o(m)\),

\[
\frac Wm=o(W/\ell).
\tag{6.3}
\]

### Theorem 6.1 (bad relative alignment)

For every fixed projected saturating cycle and every fixed U flag system,
some relative coordinate relabelling of the U system leaves at most
\(W/m\) common depth-one compatible arcs. Consequently the separate
assertions

1. “there exists a \(q=1\) saturating cycle,” and
2. “there exists a U target-disjoint strip matching”

cannot imply \(\Omega(W/\ell)\) common depth-one bridge arcs uniformly
over relative coordinate identifications.

This is not a claim that no specially coordinated favorable pair exists.

There is also an exact component demand. Cutting one edge of each of the
\(p\) native strip cycles and adding \(z\) acyclic one-way bridges leaves
at least

\[
p-z
\tag{6.4}
\]

components. Thus even before the deep-run obstruction, one needs
\(z\ge p-o(W/H)\). After arbitrary Gaussian-depth extension, Theorem 3.1
raises the necessary bridge supply to (3.20), asymptotically \(2p\).
The \(O(W/m)\) overlap certified by neither marginal theorem is negligible
on both scales.

### 6.2 A fixed saturating cycle can avoid an injective owner ledger

The preceding averaging statement has a deterministic strengthening in
the actual even dimension.

### Theorem 6.2 (forbidden-owner matching)

Let \(C\) be any \(q=1\) lower-saturating Johnson cycle in \(B_{2m}\).
For every lower colour

\[
S\in\mathcal L:=\binom{[2m]}{m-1},
\]

write \(e_C(S)\) for the unique edge of \(C\) having meet \(S\). There is
a set \(\mathcal L'\subseteq\mathcal L\) and an injection

\[
f:\mathcal L'\longrightarrow\binom{[2m]}m
\tag{6.5}
\]

such that

\[
|\mathcal L'|
\ge N_1-\frac{W}{m+1},
\qquad
S\subset f(S),
\qquad
f(S)\notin e_C(S)
\tag{6.6}
\]

for every \(S\in\mathcal L'\).

#### Proof

Join \(S\) to its middle supersets except for the two endpoints of
\(e_C(S)\). Every left vertex has degree \(m-1\), while every middle
owner has degree at most \(m\), since it has \(m\) lower facets. For
\(\mathcal A\subseteq\mathcal L\), incidence counting gives

\[
(m-1)|\mathcal A|
\le m|N(\mathcal A)|.
\tag{6.7}
\]

Hence

\[
|\mathcal A|-|N(\mathcal A)|
\le\frac{|\mathcal A|}{m}
\le\frac{N_1}{m}
=\frac{W}{m+1}.
\tag{6.8}
\]

The deficiency form of Hall's theorem supplies a matching missing at most
\(W/(m+1)\) left vertices. Its matched edges define \(f\). \(\square\)

Thus a single exact saturating cycle can coexist with an almost complete
injective lower-owner ledger which avoids both endpoints of the cycle
representative for every assigned colour. Since

\[
\frac{W}{m+1}=o(W/\ell),
\tag{6.9}
\]

cycle saturation and owner injectivity alone do not force the
\(\Theta(W/\ell)\) aligned ports needed by (3.20). Theorem 6.2 does not
construct a two-sided U flag system; precisely for that reason it is a
black-box nonimplication, not a counterexample to a future jointly
designed packet construction.

### 6.3 The exact one-port fusion law

For completeness, the remaining global selection problem has a sharper
form than separate source and head matchings. Let the strip modules be
indexed by \(\alpha\), and let \(\mathcal P_\alpha\) be the set of internal
cut ports \(t(p)\to h(p)\) in module \(\alpha\). A transversal \(\tau\)
chooses one port \(p_\alpha\in\mathcal P_\alpha\) for each module. Define
the full-lifetime bridge digraph \(G_\tau\) on modules by

\[
\alpha\longrightarrow\beta
\quad\Longleftrightarrow\quad
t(p_\alpha)\longrightarrow h(p_\beta)
\text{ is fully durable.}
\tag{6.10}
\]

For a total order \(\prec\), retain only forward arcs and put

\[
\delta(\tau,\prec)
=\max_{\mathcal A}
\left(
|\mathcal A|-|N^+_{G_\tau,\prec}(\mathcal A)|
\right).
\tag{6.11}
\]

### Theorem 6.3 (one-port transversal min--max)

Among fusions obtained by deleting exactly one internal arc per module
and inserting vertex-disjoint one-way bridges whose module quotient is
acyclic (hence a directed path forest), the minimum number of components
is

\[
\boxed{
\min_\tau\min_\prec\delta(\tau,\prec).}
\tag{6.12}
\]

#### Proof

For fixed \((\tau,\prec)\), Hall deficiency gives a forward split matching
of size \(p-\delta(\tau,\prec)\). The chosen cut turns every module into
one directed path; the split matching joins distinct path tails to
distinct path heads. Forwardness makes the module quotient acyclic, so
the result has exactly \(\delta(\tau,\prec)\) components.

Conversely, every one-cut fusion exposes the head and tail of the same
port in each module. Its quotient is a directed path forest. Order each
quotient path forward and extend to a total order. Its \(p-c\) bridges
then form a forward split matching, so
\(\delta(\tau,\prec)\le c\). Minimize. \(\square\)

Using different incoming and outgoing ports in one module would cut that
module twice and invalidates the component ledger. At depth one, every
bridge in a one-port chain also obeys the exact square identities

\[
t_i\cap h_i=t_i\cap h_{i+1}=L_1(t_i),
\tag{6.13}
\]

\[
t_i\cup h_{i+1}
=t_{i+1}\cup h_{i+1}
=U_1(h_{i+1}).
\tag{6.14}
\]

Thus the required object is a long two-sided durable square ladder with
all deeper collars, not a collection of independently aligned
saturating edges. The Hamilton packet of Theorem 5.1 is an exact finite
instance of this ladder; Theorems 5.2 and 6.2 show why neither maximal
packet tiling nor black-box saturation supplies the global one.

---

## 7. Final proved boundary

### 7.1 What has been constructed

The following objects are fully integral.

1. The projected \(q=1\) saturating cycle has a canonical lower
   depth-one completion. Its exact two-sided completion criterion is
   Theorem 1.1; upper rainbow collision and boundary Hall remain
   independent requirements.
2. U's matched strips give a target-disjoint symmetric radius-\(R\)
   partial flag system. Their native durable forest has
   \(p+u_0=o(W/R)\) components.
3. Theorem 5.1 fuses
   \[
   2\ell\binom{2(m-\ell)+1}{m-\ell}
   \]
   owners into one target-disjoint durable path. This is an actual
   multistrip, multidepth forest, not a histogram certificate.
4. Every consecutive \(k\)-strip prefix of that packet is likewise one
   target-disjoint durable path. If such prefixes could be packed across
   exact lifetime classes with \(k\to\infty\), their total component
   ledger would be \(o(W/H)\) by (5.38).

None of items 1--4 alone is one full band SCD.

### 7.2 What has been ruled out

The following failures are theorems, with their scopes explicit.

1. U's single-strip matching proof cannot be pushed to Gaussian depth:
   the full-row ABKV exponent forces (3.6) or (3.7), and equal-row
   capacity leaves a fixed fraction of middle owners.
2. Any Gaussian extension which retains the frozen native \(+1\) arcs
   needs \((1-o(1))W/\ell\) external fully durable arcs by Theorem 3.1.
3. Reciprocal two-edge switches are universally impossible in a
   positive-radius Boolean flag system by Theorem 4.4.
4. Complete fixed-split product packing has the exact small-rank deficit
   (5.23).
5. Minimal-length maximal packets collide pairwise; with slack \(g\),
   maximal packet count is bounded by Theorem 5.3.
6. Applying U's matching theorem to \(k\)-prefix atoms fails first at
   Gaussian cross-part near-regularity, and even a hypothetical
   regularization violates (5.45).
7. A fixed saturating cycle can avoid almost every assigned injective
   lower owner by Theorem 6.2. Thus saturation is not a required-owner
   port theorem.

These statements rule out the present black-box and maximal-packet
architectures. They do not rule out truncated prefixes mixed across
different skeleton grounds, nor do they rule out non-U flag systems,
non-Hamilton modules, jointly designed saturation, or alternating trades
of length at least six.

### 7.3 The precise unproved construction

For fixed \(A>0\), the surviving packet route must construct, for
\(H=\lceil A\sqrt m\rceil\), one exact symmetric band SCD together with a
single durable path forest such that:

1. for every exact lifetime class \(V_r\), all but a globally admissible
   residual are partitioned into target-disjoint Hamilton/core-swap
   prefixes;
2. the prefix lengths tend to infinity on enough mass to make the sum of
   packet counts \(o(W/H)\);
3. lower and upper targets from different radii and different skeletons
   are bijective in every rank, not merely collision-free within each
   packet;
4. each module uses one common cut port for its incoming and outgoing
   bridge, as required by Theorem 6.3; and
5. the residual owners and targets are completed in nested chains whose
   own durable component count is \(o(W/H)\).

No item in the current literature package proves this prefix
factorization, and no histogram cancellation is being promoted to it.
If it were constructed, the weighted estimate (5.40), Theorem 6.3, and
the exact S9 durable-forest-to-word theorem would give an integral literal
central-band word with \(o(W)\) transition toll for this fixed \(A\).
Constructing it for every fixed \(A\), and then applying the accepted
\(A\to\infty\) diagonalization and outer-tail step, would yield the
constant-one theorem. This implication is conditional; constant one is
not claimed here.

### 7.4 Independent audit corrections

The packet phase was independently checked:

\[
V_{j+1,1}=V_{j,0}\setminus\{q_0\}\cup\{x_j\},
\]

and both deletion-symbol collars in (5.13) agree through every
\(r<\ell\). The \(C_j/E_j\) trace proof of all-row target disjointness,
the exact maximum \(K\), and the asymptotic
\(M/W=(1+o(1))4\ell4^{-\ell}\) also passed.

Two corrections from audit have been incorporated:

* the finite ABKV exponents contain the terms \(+4\ell\) in
  (3.6)--(3.7) and \(+4\ell k\) in (5.45)--(5.46);
* the quantity \(b\) in (3.20) counts every forest arc outside the frozen
  internal \(+1\) set. The same-strip adjacency lemma then shows that all
  such durable arcs really leave the selected strip.
* the maximal-packet trace theorem uses the sharp hypothesis
  \(3\ell-g\le m\), and (5.32) compares against
  \(4^{H+g}/(H+g)\);
* after a hypothetical part restriction, the codegree bound (5.44) is
  obtained directly from \(d(X)\ge D-f(D)\), without importing the
  transitivity degrees of the unrestricted catalogue.

The universal \(C_4\)-free proof and the \(\ell+1\) deep-run
off-by-one were independently audited and passed.
