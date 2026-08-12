# Audit of the PBBS lag-two \(B+2\) packet, fixed-core collar, cache model, and protected two-factor

**Date:** 2026-08-07  
**Audited notes:**

* MATH_AUDIT_PBBS_LAG2_BPLUS2_ZERO_SIDECAR_ORBIT_AND_DYNAMIC_CACHE_GATE_20260807.md;
* MATH_THEOREM_PBBS_LAG2_FIXED_CORE_RAIL_COLLAR_20260807.md;
* MATH_THEOREM_PBBS_BPLUS2_PUNCTURED_BOUNDARY_BANK_PROTECTED_TWO_FACTOR_20260807.md.

## 1. Verdict

The clean lag-two construction is a valid local \(B(k)+2\) promotion
packet.  Its indexing, three rank-\(m\) owner values, two native
rank-\((m-1)\) intersections, two native rank-\((m+1)\) unions, terminal
flag \(M\subset U\), and lag-two forced coatom all pass.

One qualification is important.  For arbitrary nonempty covering letters
\(K_1,\ldots,K_{d-1}\), the packet proves the terminal unions \(M\) and
\(U\), but not by itself a saturated one-rank-at-a-time suffix flag.  A
prescribed strict chain requires the \(K_i\) to be its disjoint nonempty
successive differences.  The fixed-core specialization below does have
the complete saturated suffix flag.

The every-position fixed-core toggle rail correctly extends the specialized
packet to a simple biresident owner cycle.  Its current endpoint
enrichments are essential: without \(C_0\) in the first exceptional letter,
the entering length-\((L-1)\) seam omits part of the core; for \(d=2\),
the outgoing seam analogously needs \(Q\cup\{a_0\}\) in the last letter.
With the enrichments now stated in the collar note, all lower seams pass.

The collar note should additionally say that **every** toggle in the cyclic
stream lies outside the fixed core \(G\).  Distinctness alone is
insufficient.  On the ground set \([2m+1]\), a stream of \(\rho\) distinct
noncore toggles necessarily satisfies

\[
 2L\le \rho\le (2m+1)-|G|=m+d+3.
\tag{1.1}
\]

If the stream does not exhaust \([2m+1]\setminus G\), the unused noncore
coordinates are permanently zero; they do not have the one-run profile
claimed literally in the collar note.  Residence still passes.  To make
every noncore coordinate a toggle with one positive run, take
\(\rho=m+d+3\).

The symmetric packet-orbit degrees, cover multipliers, and four elementary
forbidden start differences pass.  The owner-capacity bound should be

\[
 H\le\left\lfloor\frac W3\right\rfloor
\tag{1.2}
\]

when all \(3H\) owner target values are distinct, rather than
\(\lfloor(W+1)/3\rfloor\).

The dynamic-cache conditions in the source note are exact for the local
set-valued window identities.  They are not an if-and-only-if
characterization of a complete global PBBS realization unless the
prescribed task identities, full chain data, named multiplicities,
residence, common cap, and compiler conditions are added.

The protected punctured boundary-bank theorem passes.  Its menu counts,
collision bounds, greedy estimate, middle-levels parameter, and protected
two-factor threshold are correct.  It preserves the selected lower
intersection set-theoretically, but it does not put the separate literal
source blocks into one common word.

## 2. Clean lag-two packet

Put

\[
 n=2m+1,\qquad
 L=d+2,\qquad
 |M|=m-d-2,\qquad
 |C|=d,\qquad
 R=M\mathbin{\dot\cup}C.
\tag{2.1}
\]

Let \(x,u,y,v\) be distinct and disjoint from \(R\), and choose nonempty
letters

\[
 K_1,\ldots,K_{d-1}\subseteq M,
 \qquad
 \bigcup_{i=1}^{d-1}K_i=M.
\tag{2.2}
\]

On positions \(0,\ldots,L+1\), take

\[
 x,\ u,\ K_1,\ldots,K_{d-1},\ C,\ y,\ v.
\tag{2.3}
\]

The \(K_i\)'s occupy positions \(2,\ldots,d=L-2\), \(C\) occupies
position \(L-1\), and \(y,v\) occupy positions \(L,L+1\).

### Proposition 2.1 (exact interval table)

The three consecutive length-\(L\) windows are

\[
 \begin{aligned}
 [0,L-1]&:T_-=R\cup\{x,u\},\\
 [1,L]&:T_0=R\cup\{u,y\},\\
 [2,L+1]&:T_+=R\cup\{y,v\}.
 \end{aligned}
\tag{2.4}
\]

Their ranks are \(m\), and the path exchanges \(x\mapsto y\), then
\(u\mapsto v\).  All three owner values are distinct.

The positional overlaps are

\[
 \begin{aligned}
 [1,L-1]&:I_-=R\cup\{u\}=T_-\cap T_0,\\
 [2,L]&:I_+=R\cup\{y\}=T_0\cap T_+,
 \end{aligned}
\tag{2.5}
\]

each of length \(L-1=d+1\) and rank \(m-1\).  The spans are

\[
 \begin{aligned}
 [0,L]&:J_-=R\cup\{x,u,y\}=T_-\cup T_0,\\
 [1,L+1]&:J_+=R\cup\{u,y,v\}=T_0\cup T_+,
 \end{aligned}
\tag{2.6}
\]

each of length \(L+1=d+3\) and rank \(m+1\).

At endpoint \(L-2=d\), the final \(d-1\) and \(d\) suffix unions are

\[
 M,\qquad U=M\cup\{u\}.
\tag{2.7}
\]

At endpoint \(L\), the interval \([2,L]\) has value

\[
 Y=M\cup C\cup\{y\}=I_+,
\tag{2.8}
\]

and \(T_0=Y\cup\{u\}\).  Thus the forced coatom follows the flag endpoint
with lag two.

All identities follow by direct union.  A source word of length \(W+d+2\)
allows selected rank-\(m\) and rank-\((m+1)\) witnesses of lengths at most
\(d+3=L+1\).  Hence every interval in (2.4)--(2.6) is admissible at
\(B+2\), with no local immediate-palette sidecar.

The equality \(Y=I_+\) is intentional: one rank-\((m-1)\) occurrence
serves simultaneously as the forced successor coatom and the native
successor lower colour.  It is not a collision between distinct required
targets.

For clarity, (2.2) alone does not make all shorter suffix unions a
saturated flag.  That stronger conclusion holds when the \(K_i\) are the
ordered disjoint differences of a prescribed strict chain.  It also holds
in the fixed-core realization of Section 3.

## 3. Exact fixed-core rail

Assume \(d\ge2\).  Choose pairwise disjoint data

\[
 Q,\ C_0,\ \{a_0\},\
 A_1=\{a_1,\ldots,a_{d-1}\},\
 \{b^-,u,z,b,v\},
\tag{3.1}
\]

where

\[
 |Q|=m-2d-2,\qquad |C_0|=|A_1|=d-1,
\tag{3.2}
\]

and put

\[
 \begin{aligned}
 G&=Q\mathbin{\dot\cup}C_0\mathbin{\dot\cup}\{a_0\},\\
 M&=Q\mathbin{\dot\cup}\{a_0\}\mathbin{\dot\cup}A_1,\\
 C&=C_0\mathbin{\dot\cup}\{z\}.
 \end{aligned}
\tag{3.3}
\]

Then

\[
 |G|=|M|=m-d-2=m-L.
\tag{3.4}
\]

The construction requires \(m\ge 2d+2\) so that \(Q\) exists; this holds
for the intended sufficiently large optimal parameters.

Take a cyclic stream

\[
 \tau_0,\ldots,\tau_{\rho-1}
\tag{3.5}
\]

of distinct labels such that

\[
 \boxed{\tau_i\notin G\quad\text{for every }i,}
\qquad
 2L\le \rho\le m+d+3,
\tag{3.6}
\]

and suppose one consecutive substring is

\[
 b^-,u,a_1,\ldots,a_{d-1},z,b,v.
\tag{3.7}
\]

At an ordinary position with toggle \(\tau_i\), use
\(G\cup\{\tau_i\}\).  On the displayed substring, use

\[
 C_0\cup\{b^-\},\ \{u\},\
 Q\cup\{a_0,a_1\},\ldots,Q\cup\{a_0,a_{d-1}\},\
 C_0\cup\{z\},\ \{b\},\ \{v\}.
\tag{3.8}
\]

When \(d=2\), replace the final \(\{v\}\) by
\(Q\cup\{a_0,v\}\).  Equivalently, one may use that enriched final
letter for every \(d\ge2\); the extra core coordinates are harmless for
all local owner, palette, flag, and residence rows.  This optional uniform
enrichment is not overlap-neutral: for \(d\ge3\) it changes the
core-fragment suffix from \(C_0,\varnothing,\varnothing\) to
\(C_0,\varnothing,Q\cup\{a_0\}\), creating a possible length-three
collar border at shift \(L-1\).  The minimal endpoint convention in the
source note avoids that border.  In either convention the owner triples
at shift \(L-1\) are disjoint, so this does not help the bundled-owner
train problem.

### Theorem 3.1 (window identity)

Every length-\(L\) source window has union

\[
 \boxed{
 G\cup\{\text{the corresponding \(L\) consecutive toggles}\}.}
\tag{3.9}
\]

#### Proof

A window meeting an ordinary position contains \(G\).  Every exceptional
letter contains no coordinate outside \(G\) other than its designated
toggle.  There are exactly three wholly exceptional length-\(L\) windows.
Each contains a \(Q\cup\{a_0,a_i\}\) letter and the
\(C_0\cup\{z\}\) letter, whose core parts have union \(G\).  Thus no core
coordinate is lost and no undesignated toggle is gained.  \(\square\)

It follows that all owners have rank \(m\), consecutive owners are
Johnson neighbours, and the owner cycle is simple.  Indeed, the owner
after \(T_+\) deletes the outgoing toggle from its cyclic \(L\)-interval
and inserts the next distinct toggle; it does not repeat \(T_+\).

Likewise, the lower and upper palettes are \(G\) plus cyclic toggle
intervals of lengths \(L-1\) and \(L+1\).  These are proper intervals,
and distinct starts give distinct sets because \(\rho\ge2L\).  Thus both
immediate palettes are simple.

Every noncore toggle has one positive owner run of length \(L\) and a zero
run of length \(\rho-L\ge L\).  Every coordinate of \(G\) is permanent.
Any ground coordinate outside \(G\) that is not used as a toggle is
permanently zero.
Thus the owner row is biresident at depth \(L=d+2\), stronger than the
required \(d+1\) floor.

The three central owner windows and the identities (2.5)--(2.8) are
exactly the clean lag-two packet under

\[
 x=b^-,\qquad y=b.
\tag{3.10}
\]

### Proposition 3.2 (saturated specialized suffix)

At the endpoint \(L-2=d\), the suffix of \(j\) exceptional letters has,
for \(1\le j\le d-1\), the value

\[
 Q\cup\{a_0\}\cup
   \{a_{d-j},a_{d-j+1},\ldots,a_{d-1}\},
\tag{3.11}
\]

of rank \(m-2d-1+j\).  For \(j=d\), adjoining the preceding singleton
\(\{u\}\) gives \(U=M\cup\{u\}\), of rank \(m-d-1\).  Hence these suffixes
realize every rank from \(m-2d\) through \(m-d-1\), one at a time.

## 4. Seam check and endpoint enrichments

The length-\(L\) identity does not alone imply that a fragmented
length-\((L-1)\) source overlap contains all of \(G\).

If the first exceptional letter were the bare singleton \(\{b^-\}\), the
overlap immediately entering \(T_-\), on exceptional positions
\(0,\ldots,L-2\), would have union

\[
 Q\cup\{a_0\}\cup A_1\cup\{b^-,u\},
\tag{4.1}
\]

which omits \(C_0\subset G\).  The set-theoretic intersection of the
adjacent owners is \(G\) plus the shared toggles, so this bare version
would not make the entering lower colour literal.

The collar note's current first letter \(C_0\cup\{b^-\}\) exactly repairs
that seam.  For \(d=2\), the exceptional overlap on positions
\(3,\ldots,L+1\) immediately leaving \(T_+\) contains
\(C_0\cup\{z,b,v\}\) but, with a bare last letter, omits
\(Q\cup\{a_0\}\).  The note's \(d=2\) replacement
\(Q\cup\{a_0,v\}\) repairs this second seam.  For \(d\ge3\), that overlap
already contains a remaining \(Q\cup\{a_0,a_i\}\) letter, so no final
enrichment is needed.

The two packet-internal overlaps, on positions \(1,\ldots,L-1\) and
\(2,\ldots,L\), contain both complementary core pieces and pass for every
\(d\ge2\).  Every length-\((L+1)\) span also contains either an ordinary
full-core letter or, when wholly exceptional, both core pieces.  Hence all
upper colours are native.

There are exactly four wholly exceptional length-\((L-1)\) windows.  With
the current endpoint enrichments:

1. the first obtains \(C_0\) from the first letter and
   \(Q\cup\{a_0\}\) from an internal letter;
2. the middle two already contain both pieces; and
3. the last either contains an internal \(Q\cup\{a_0,a_i\}\) letter
   when \(d\ge3\), or obtains \(Q\cup\{a_0\}\) from the enriched last
   letter when \(d=2\).

Thus every one contains \(G\), and every other overlap contains an
ordinary \(G\)-letter.  All native lower seams therefore pass.

These enrichments are zero-cost: they add only coordinates of \(G\).
Consequently they preserve every length-\(L\) owner, the specialized
suffix flag, \(M,U,Y\), both central palettes, owner simplicity, and
residence.

## 5. Orbit and cover-multiplier audit

Suppress the internal \(K_i\)-cover and regard a packet as the labelled
data \((M,C,x,u,y,v)\).  Put

\[
 a=m-d-2,\qquad
 c_0=\binom{m-2}{d},\qquad
 N=m+d+2.
\tag{5.1}
\]

The total packet count is

\[
 \binom n{m-2}c_0(m+3)_4
 =\frac{n!}{a!\,d!\,(m-1)!}.
\tag{5.2}
\]

For a fixed flag \((M,M\cup\{u\})\), the degree is

\[
 D_F=\binom Nd(m+2)_3.
\tag{5.3}
\]

For a fixed resource in a specified role, direct reconstruction gives

\[
 \begin{aligned}
 D_O&=c_0(m)_2(m+1)_2,\\
 D_L&=c_0(m-1)(m+2)_3,\\
 D_U&=D_O.
 \end{aligned}
\tag{5.4}
\]

The nested lower--owner pair has codegree

\[
 \lambda=c_0(m-1)(m+1)_2,
\tag{5.5}
\]

and hence normalized ratios \(1/(m+2)\) and \(1/m\) against the lower and
owner degrees.  These formulas pass.

For \(r=d-1\), the number of ordered nonempty covers of an \(a\)-set by
\(r\) labelled subsets is

\[
 \kappa_{\mathrm{cov}}(a,r)
 =\sum_{j=0}^{r}(-1)^j\binom rj(2^{r-j}-1)^a.
\tag{5.6}
\]

Each ground element first chooses a nonempty subset of the \(r\) cover
labels, and inclusion--exclusion forces every labelled part to be used.
If the parts must instead be the disjoint nonempty differences of a strict
chain, the count is

\[
 \kappa_{\mathrm{part}}(a,r)=r!\,S(a,r).
\tag{5.7}
\]

Both are common multipliers for the displayed resource degrees only when
the individual \(K_i\)-values are not themselves named task resources.

## 6. Start conflicts, owner capacity, and cache conditions

A packet beginning at source position \(s\) forces singleton letters at

\[
 s,\quad s+1,\quad s+L,\quad s+L+1,
\tag{6.1}
\]

and a rank-\(d\) letter at \(s+L-1\).  Comparing the latter position of
one packet with the singleton positions of another gives the forbidden
positive start differences

\[
 1,\quad 2,\quad L-2,\quad L-1.
\tag{6.2}
\]

This calculation passes.  The undirected difference graph has maximum
degree at most eight, so its raw positional independence number is at
least one ninth of the available starts.

Each clean packet has three distinct owner target values.  If owner values
are also distinct across packets, \(H\) packets use \(3H\) of the exactly
\(W\) rank-\(m\) targets.  Therefore

\[
 \boxed{H\le\lfloor W/3\rfloor.}
\tag{6.3}
\]

A \(W+1\) numerator would require an explicitly permitted repeated closure
owner occurrence; it is not a bound for \(3H\) globally distinct owner
target values.

For an ambient word \((A_t)\) and start set \(S\), define

\[
 M_s=\bigcup_{t=s+2}^{s+L-2}A_t,
 \qquad
 C_s=A_{s+L-1}.
\tag{6.4}
\]

The four singleton conditions, the ranks of \(M_s,C_s\), and pairwise
disjointness are sufficient for the local set-valued identities in
Section 2, provided source letters are nonempty by convention.  A global
task/factor equivalence must additionally require:

1. \((M_s,M_s\cup A_{s+1})\) is the prescribed promotion task assigned
   to start \(s\);
2. if a complete lower chain is prescribed, the individual internal
   letters realize that chain, not merely a cover with union \(M_s\);
3. the named flag targets and forced coatoms have their required global
   multiplicities, in addition to owners and the two immediate palettes;
4. residence and common-cap constraints hold; and
5. the remaining lower targets admit the required common compiler.

Thus the source cache statement is exact as a local-union test, not as a
complete global PBBS if-and-only-if theorem without these extra rows.

## 7. Punctured boundary bank and protected two-factor

For one fixed flag \(U=M\cup\{u\}\), the projected two-owner menu chooses
a \(d\)-set

\[
 C\subseteq[n]\setminus U
\tag{7.1}
\]

and ordered distinct \(x,y\notin U\cup C\), then puts

\[
 I=U\cup C,\qquad
 T_-=I\cup\{x\},\qquad
 T_0=I\cup\{y\},\qquad
 J=I\cup\{x,y\}.
\tag{7.2}
\]

The menu size

\[
 D=\binom{m+d+2}{d}(m+2)_2
\tag{7.3}
\]

is exact.  Its punctured source realization assumes \(d\ge2\) and also
needs a \(d\)-subset of \(M\), equivalently
\(m-d-2\ge d\), or \(m\ge2d+2\).  These conditions hold for the intended
sufficiently large optimal parameters.

For one prescribed resource in the next task's menu, the collision counts
are

\[
 \begin{array}{c|c}
 \text{resource}&\text{number of menu items}\\ \hline
 I&(m+2)_2\\
 T\text{ in either owner slot}&2(d+1)(m+1)\\
 J&(d+2)_2.
 \end{array}
\tag{7.4}
\]

For \(I\), the difference \(I\setminus U\) fixes \(C\).  For an owner in a
specified slot, choose the distinguished exterior member from the
\((d+1)\)-set \(T\setminus U\), then choose the other label outside
\(T\); the factor two accounts for the two slots.  For \(J\), choosing
the ordered pair \(x,y\) in \(J\setminus U\) fixes the remaining set
\(C\).  The greedy forbidden-menu inequality in the source note follows.

For the triangular bank,

\[
 h\le\binom{d+1}{2}=O(d^2)=O(m).
\tag{7.5}
\]

The menu in (7.3) is \(\Omega(m^4)\), while the total greedy exclusion is
\(O(m^3)\).  Thus mutually distinct owners, lower colours, and upper
colours can be selected for all sufficiently large optimal parameters.

The graph \(ML_{m+1}\) on ground size \(2m+1\) is the incidence graph
between ranks \(m\) and \(m+1\).  Its protected-small-bank theorem has
threshold

\[
 (m+1)-2=m-1
\tag{7.6}
\]

edges.  The selected paths contain

\[
 |E(P)|=2h\le d(d+1)\le m-1
\tag{7.7}
\]

for all sufficiently large optimal parameters, because
\(d^2/m\to\pi/4<1\).  The protected two-factor extension is therefore
used with the correct parameter and bound.

At each protected upper vertex \(J\), the two incident protected edges

\[
 T_-\subset J\supset T_0
\tag{7.8}
\]

already give degree two.  Every extending two-factor must retain both, so
it retains the two owners and their set-theoretic lower intersection

\[
 I=T_-\cap T_0.
\tag{7.9}
\]

This theorem is deliberately abstract.  The separate punctured source
realizations do not automatically combine into one antecedent word, and
the punctured realization exports its authoritative successor-coatom
ticket rather than furnishing a common literal history.

## 8. Global conclusion

After the necessary endpoint enrichments, no obstruction remains in one
clean specialized lag-two packet or its fixed-core resident collar.  The
actual Ferrers boundary bank has only \(O(d^2)=O(m)\) tasks, and its
projected middle/upper paths can be planted together in a protected
two-factor.

The surviving gate is the common-history lift: place the selected packet
or collar fragments in one source word, connect potentially different
fixed cores, preserve the prescribed promotion tasks and lower chains,
and realize the background owner and palette factor with one compiler.
None of the three audited notes proves that global cache trajectory.
