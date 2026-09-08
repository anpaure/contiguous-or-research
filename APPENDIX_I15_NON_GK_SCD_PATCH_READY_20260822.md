### I.15 A non-GK central factor with Hamilton projections and two near-tours

Fix odd \(b\ge3\), put \(n=2b\), and let
\[
 \Omega=\{0,\ldots,n-1\},\quad W={2b\choose b},\quad
 N={2b\choose b-1}={b\over b+1}W,\quad
 h={b-1\over2},\quad q=b(b-1).                            \tag{I.119}
\]
A full symmetric-chain decomposition (SCD) partitions \(2^\Omega\) into
saturated chains whose endpoint ranks sum to \(2b\). Every rank-\((b-1)\)
set lies on a chain crossing ranks \(b-1,b,b+1\), so every full SCD has
exactly \(N\) central flags
\[
 f=(L,C,U),\quad L\subset C\subset U,\quad
 (|L|,|C|,|U|)=(b-1,b,b+1),
\]
with directed coordinate arc
\[
                 p(f)=C\setminus L\longrightarrow q(f)=U\setminus C.
                                                                    \tag{I.120}
\]
A coherent \(b\)-packet tour chooses a cyclically ordered perfect pairing
\(P_j=\{a_j^0,a_j^1\}\) and one selected member of every pair. In packet
\(j\), retain the selected member of the special pair \(P_j\), replace the
selected members of all other pairs once in cyclic FIFO order, and advance
the special pair. Every pair flips \(b-1\) times, so the process closes;
the \(b-1\) internal windows of each packet supply its \(q\) central flags.

Let \(\mathfrak F\) be the set of all three-rank flags. A lower or upper target
lies in \(b(b+1)\) flags, a middle target lies in \(b^2\), and
\[
 |\mathfrak F|=Nb(b+1),\qquad w={1\over b(b+1)}.           \tag{I.121}
\]
Thus weight \(w\) on every flag gives load one on ranks \(b\pm1\) and
load \(b/(b+1)\) on rank \(b\). It is fractionally SCD-realizable: average
all coordinate permutations of any full SCD. The symmetric group is
transitive on \(\mathfrak F\), so the common average weight is
\(N/|\mathfrak F|=w\).

This weighting also has the exact Hamilton arc marginal. Each ordered arc
\(x\to y\) supports \(A={2b-2\choose b-1}\) flags. There are \((2b-1)!\)
directed Hamilton cycles and \((2b-2)!\) contain a fixed arc. Assign
\[
 z(H,f)={w\over(2b-2)!}\mathbf1_{\{p(f)\to q(f)\in H\}}.  \tag{I.122}
\]
Then \(\sum_Hz(H,f)=w\), and for fixed \(H\) every arc has mass
\(Aw/(2b-2)!\). This is only an arc-marginal decomposition: flags assigned
to one \(H\) need not be disjoint in any rank.

We next give an exact integral switch criterion. Let \(\mathscr D\) be a
full SCD, let \(M\) be its \(N\) middle members on three-rank chains, and
let \(Z={\Omega\choose b}\setminus M\) be its \(N/b\) singleton middle
chains. Write the flag through \(C\in M\) as
\(L_C\subset C\subset U_C\), and put
\[
                     \phi(C)=L_C\cup(U_C\setminus C).     \tag{I.123}
\]
Replacing \(C\) by \(\phi(C)\) preserves \(L_C,U_C\) and reverses its arc.
For \(S\subseteq M\), these simultaneous replacements extend to another
full SCD, changing no other rank, if and only if
\[
 \boxed{\phi|_S\hbox{ is injective},\qquad
        \phi(S)\cap(M\setminus S)=\varnothing.}           \tag{I.124}
\]
Necessity follows because changed chains cannot share a middle member or
use one owned by an unchanged chain. Conversely, under (I.124) replace the
selected middles, delete the singleton chains in \(Z\cap\phi(S)\), and add
singleton chains on \(S\setminus\phi(S)\). Injectivity gives
\[
 |Z\cap\phi(S)|=|\phi(S)\setminus S|
                =|S\setminus\phi(S)|,
\]
and the two conditions say that every middle set is again used exactly
once. Each changed three-rank segment remains saturated and symmetric, so
the result is a full SCD.

Apply this to the ordered Greene--Kleitman SCD. Encode sets by binary words
and greedily pair each zero with the latest unpaired one to its left.
Fixing all paired bits and changing the unpaired zeros from right to left
into ones gives one saturated symmetric chain; these classes partition
the lattice. A balanced middle word is a singleton exactly when it is
Dyck (all prefix heights, with \(1=+1,0=-1\), are nonnegative). Otherwise
its central arc is \(p\to q\), where \(p\) is its leftmost unpaired one and
\(q\) its rightmost unpaired zero; hence \(q<p\).

Put
\[
 K=\operatorname {Cat}_{b-1}={1\over b}{2b-2\choose b-1}. \tag{I.125}
\]
For every primitive Dyck word \(D=1D'0\), switch the middle word
\(C_D=0D'1\). Its only unpaired symbols are the first zero and last one,
so its arc is \((2b-1)\to0\) and \(\phi(C_D)=D\). The \(K\) targets \(D\)
are distinct singleton chains. Thus (I.124) permits all \(K\) switches
simultaneously, producing a genuine full non-GK SCD \(\mathscr D^*\) with
\(K\) flags of arc \(0\to2b-1\).

For every \(1\le j\le2b-1\), the original GK factor has exactly \(K\)
flags of arc \(j\to j-1\). Indeed, unpaired zeros are record-minimum
down-steps, while the leftmost surviving one leaves the last global
minimum; the two prescribed adjacent symbols therefore form the down-up
valley at a unique global minimum. Write the word
\(A01B\), with \(|A|=j-1\). Starting after the minimum gives the primitive
Dyck word \(1BA0\), hence \(BA\) is Dyck of length \(2b-2\). Conversely,
split any such Dyck word uniquely as \(BA\), with
\(|B|=2b-j-1\), and form \(A01B\); the cyclic word \(1BA0\) is primitive,
so the displayed valley is the unique minimum. This is a bijection and
proves the count.

None of the \(K\) switches changes a consecutive descending arc. Therefore
\(\mathscr D^*\) contains every edge of
\[
                  H_*:0\to2b-1\to2b-2\to\cdots\to1\to0 \tag{I.126}
\]
with multiplicity exactly \(K\). Group \(h\) flags on each edge, aligning
the groups around \(H_*\). Using
\(\lfloor K/h\rfloor\ge K/h-1\) and
\(2bK/N=(b+1)/(2b-1)\), this gives
\[
 T_*=\left\lfloor{K\over h}\right\rfloor,\quad
 R_*=qT_*,\quad
 {R_*\over N}\ge {b+1\over2b-1}-{b(b-1)\over N}
 ={1\over2}+\Theta(b^{-1}).                              \tag{I.127}
\]
All these flags lie in one SCD factor, so they are jointly disjoint in
each of the three ranks. This is an integral Hamilton-projection subsystem,
not yet a grouping into coherent FIFO tours.

There are nevertheless two explicit near-tours inside this factor. All
coordinates below are modulo \(2b\). For \(\delta\in\{0,1\}\), define
\[
 I(r)=\{r,r+1,\ldots,r+b\},\quad
 a_s^\delta=\delta+(s+1)(b-1),\quad
 W_{s,t}^\delta=I(a_s^\delta-t+1)\setminus\{a_s^\delta+1\}
                                                               \tag{I.128}
\]
for \(0\le s<b,\ 0\le t\le b\). Since
\(a_{s+1}^\delta=a_s^\delta+b-1\), also at the cyclic wrap,
\(W_{s,b}^\delta=W_{s+1,0}^\delta\). Pair \(j\) with \(j+b\).
The boundary windows are transversals. For \(1\le t<b\), the internal
window doubles the pair of \(a_s^\delta-t+1\), empties the pair of
\(a_s^\delta+1\), and splits all others. Its empty/double labels are
\(\delta-s,\delta-s-t\pmod b\), so all \(b(b-1)\) internal windows are
distinct. Consecutive windows differ by one FIFO replacement; hence each
\(\delta\) defines a closed coherent \(b\)-packet tour.

Put \(r=r_{s,t}^\delta=a_s^\delta-t+1\). Its internal flag is
\[
 C_{s,t}^\delta=I(r)\setminus\{r+t\},\quad
 L_{s,t}^\delta=C_{s,t}^\delta\setminus\{r\},\quad
 U_{s,t}^\delta=C_{s,t}^\delta\cup\{r-1\}.               \tag{I.129}
\]
Thus its arc is \(r\to r-1\). Since
\(\gcd((b-1)/2,b)=1\), the \(a_s^\delta\) run through one parity class;
among \(t-1=0,\ldots,b-2\) exactly \(h\) have either parity. Every arc of
\(H_*\) consequently occurs \(h\) times.

Read \(C_{s,t}^\delta\) cyclically from coordinate \(r\). Its word is
\[
                       1^t\,0\,1^{b-t}\,0^{b-1}.          \tag{I.130}
\]
For \(t\ge2\) this is primitive Dyck. If \(r\ne0\), the ordinary walk has
its unique minimum between \(r-1,r\), so its unchanged GK flag is exactly
(I.129). If \(r=0\), then \(C_{s,t}^\delta=1D'0\) is a primitive singleton,
and the switched source \(0D'1\) has precisely the lower and upper members
in (I.129). For \(t=1\), (I.130) returns to height zero after two symbols.
If \(r\ne0\), the proposed boundary is not the unique minimum and the GK
flag differs; if \(r=0\), it is a nonprimitive singleton and was not
switched. Hence, writing \(\mathfrak F^*\) for the central factor,
\[
 (L_{s,t}^\delta,C_{s,t}^\delta,U_{s,t}^\delta)\in\mathfrak F^*
 \iff 2\le t\le b-1,\qquad
 |\mathcal T_*^\delta\cap\mathfrak F^*|=b(b-2)=q-b.       \tag{I.131}
\]

The two retained systems are jointly rankwise-disjoint. A retained flag
determines its arc start \(r\) and the unique omitted coordinate \(r+t\)
inside \(I(r)\), hence \(a_s^\delta=r+t-1\), whose parity is \(\delta\).
Thus the two systems share no flag; since both lie in one SCD factor,
their lower, used-middle, and upper targets are all distinct.

The loss \(b/q=1/(b-1)=o(1)\) is locally acceptable: if
\((1+o(1))N/q\) such partial tours could be packed and repaired at
\(O(b)\) cost each, the total repair would be \(O(N/b)=o(N)\). The fixed
cycle does not provide that packing. For an ordered pairing
\(P_j=\{a_j^0,a_j^1\}\), the \(b\) packet-ending FIFO queues contain each
arc of \(a_0^0,\ldots,a_{b-1}^0,a_0^1,\ldots,a_{b-1}^1\) exactly \(h\)
times: each pair-order adjacency is omitted by one queue, and the other
\(b-1\) occurrences split equally between the two bit states. Hence a
directed Hamilton cycle \((h_0,\ldots,h_{2b-1})\) forces the antipodal
pairs \(\{h_j,h_{j+b}\}\). Even rotations of its listing only move the
packet origin; odd rotations give the other phase. Thus it has exactly two
coherent supports, and \(H_*\) contributes only \(2b(b-2)=O(b^2)=o(N)\)
retained flags.

More generally, average both phase supports over all \((2b-1)!\) directed
Hamilton cycles. Symmetry is transitive on \(\mathfrak F\), every support
has \(q\) flags, and every central factor has \(N\). Therefore, for every
central factor \(\mathfrak A\),
\[
 {1\over2(2b-1)!}\sum_{H,\delta}
 |\mathcal T^\delta(H)\cap\mathfrak A|
 ={Nq\over|\mathfrak F|}={b-1\over b+1}<1.               \tag{I.132}
\]
The two overlaps (I.131) are exceptional, not a large family. The remaining
Gate C is to pack \((1-o(1))N/q\) distinct coherent supports (or
\(q-O(b)\) partial supports) inside one extendable non-GK factor across
many Hamilton cycles, and to repair their packet and deeper-chain defects
with total \(o(N)\) cost.
