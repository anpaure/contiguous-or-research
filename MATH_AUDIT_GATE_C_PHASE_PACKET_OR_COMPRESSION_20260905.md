# Gate C audit: exact OR compression of phase packets

**Status (2026-09-05).** The phase-packet compression asserted below is
valid. It removes ordered queue joining, packet-boundary repair, and
cross-join cleanliness from the live phase-packet route. It does not solve
the remaining correlated all-band selector.

Let

\[
 |\Omega|=2b,\qquad W={2b\choose b},\qquad
 1\le H\le b-2,\qquad \ell=b-H,                       \tag{0.1}
\]

where \(b\ge5\) is odd. In the asymptotic application,

\[
 H=\left\lceil\sqrt{2b\log(2b)}\right\rceil=o(b),     \tag{0.2}
\]

and (0.1) holds for all sufficiently large \(b\). Subscripts on cyclic
words are read modulo their lengths.

## 1. Exact starts and cleanliness

A labelled phase packet consists of distinct \(u,v\in\Omega\) and ordered
tuples

\[
 X=(x_1,\ldots,x_{b-1}),\qquad
 Y=(y_1,\ldots,y_{b-1})                               \tag{1.1}
\]

whose entries partition \(\Omega\setminus\{u,v\}\). Put

\[
 z=(u,x_1,\ldots,x_{b-1},y_1,\ldots,y_{b-1}),
 \qquad |z|=2b-1.                                     \tag{1.2}
\]

Use zero-based positions:

\[
 z_0=u,\qquad z_i=x_i\ (1\le i\le b-1),\qquad
 z_{b-1+i}=y_i\ (1\le i\le b-1).                     \tag{1.3}
\]

For a cyclic word \(w\), write

\[
 I_s^w(i)=\{w_i,w_{i+1},\ldots,w_{i+s-1}\}.           \tag{1.4}
\]

The designated starts are exactly \(i=0,1,\ldots,b\). Their middle targets
are

\[
\begin{aligned}
 I_b^z(0)&=\{u\}\cup X=:C_0,\\
 I_b^z(i)&=\{x_i,\ldots,x_{b-1}\}
             \cup\{y_1,\ldots,y_i\}=:C_i
             &&(1\le i\le b-1),\\
 I_b^z(b)&=\{y_1,\ldots,y_{b-1},u\}
             =\{u\}\cup Y=:C_b.                      \tag{1.5}
\end{aligned}
\]

Thus the internal starts are \(1,\ldots,b-1\), exactly \(b-1\) of them;
\(0,b\) are the two endpoint starts.

The \(C_i\) are distinct. Indeed, for \(1\le i<j\le b-1\), the element
\(y_j\) lies in \(C_j\setminus C_i\); \(C_0\) contains no \(y_j\), while
every internal \(C_i\) contains \(y_i\); and \(C_b\) contains no \(x_i\),
while every internal \(C_i\) contains \(x_i\). Finally \(C_0\ne C_b\)
because \(X\) and \(Y\) are nonempty and disjoint.

### Lemma 1.1 (packet cleanliness)

Every cyclic window in \(z\) of length at most \(2b-1\), hence every
window of length at most \(2b-2\), is clean.

#### Proof

The \(2b-1\) entries of \(z\) are distinct. A cyclic window using at most
one full period therefore contains no repeated entry. \(\square\)

In particular all designated windows at ranks \(b-H,\ldots,b+H\) are
clean, since \(b+H\le2b-2\).

## 2. Exact set-valued block

For one packet define

\[
 A_j=I_\ell^z(j),\qquad 0\le j\le b+2H,              \tag{2.1}
\]

and emit the linear set-valued word

\[
 \mathsf B(z)=(A_0,A_1,\ldots,A_{b+2H}).              \tag{2.2}
\]

It has exactly

\[
                         b+2H+1=b+1+2H               \tag{2.3}
\]

nonempty letters. Formula (2.1) remains meaningful if its integer indices
pass one period, because \(z\) is cyclic.

### Lemma 2.1 (consecutive-OR identity)

For every designated start \(0\le i\le b\) and every
\(s\in[b-H,b+H]\), the interval

\[
 A_i,A_{i+1},\ldots,A_{i+s-\ell}                     \tag{2.4}
\]

lies in \(\mathsf B(z)\) and has union \(I_s^z(i)\).

#### Proof

Put \(q=s-\ell\), so \(0\le q\le2H\). The last index in (2.4) is at most
\(b+2H\), and

\[
 \bigcup_{r=0}^{q}A_{i+r}
 =\bigcup_{r=0}^{q}\{z_{i+r},\ldots,z_{i+r+\ell-1}\}
 =\{z_i,\ldots,z_{i+\ell+q-1}\}
 =I_s^z(i).                                           \tag{2.5}
\]

The final set has \(s\) elements by Lemma 1.1. \(\square\)

Thus one packet, without any join, realizes all of its \(b+1\) designated
targets at every band rank. Witnesses are kept inside their emitted blocks.

## 3. Exact compiler and remaining selector

Let \(\mathscr P\) be any family of \(t\) labelled phase packets. For
\(s\in[b-H,b+H]\), put

\[
 \mathcal I_s=\bigcup_{P\in\mathscr P}
     \{I_s^{z_P}(i):0\le i\le b\},\qquad
 h_s={2b\choose s}-|\mathcal I_s|.                    \tag{3.1}
\]

Concatenate the words \(\mathsf B(z_P)\), append one set-valued letter for
each missing band target, and append one for each nonempty far-rank target.
Then

\[
\boxed{
 \nu(2b)\le (b+1+2H)t
 +\sum_{s=b-H}^{b+H}h_s
 +\sum_{\substack{1\le s\le2b\\ |s-b|>H}}{2b\choose s}.}
                                                               \tag{3.2}
\]

Every packet has \(b+1\) distinct middle targets. Define the aggregate
middle collision excess

\[
 R_b=(b+1)t-|\mathcal I_b|\ge0.                       \tag{3.3}
\]

Since \(h_b=W-|\mathcal I_b|\), (3.2) becomes

\[
\boxed{
 \nu(2b)\le W+2Ht+R_b
 +\sum_{\substack{b-H\le s\le b+H\\s\ne b}}h_s
 +\sum_{\substack{1\le s\le2b\\ |s-b|>H}}{2b\choose s}.}
                                                               \tag{3.4}
\]

For (0.2), the last sum is \(o(W)\). The exact sufficient selector
condition for this compiler is therefore

\[
 2Ht+R_b+
 \sum_{\substack{b-H\le s\le b+H\\s\ne b}}h_s=o(W).   \tag{3.5}
\]

This is more permissive than global middle disjointness: it permits any
selection with only \(o(W)\) total middle occurrence excess.

### Corollary 3.1 (internal-core form)

Suppose

\[
 \{C_i(P):P\in\mathscr P,\ 1\le i\le b-1\}           \tag{3.6}
\]

is globally distinct. Then

\[
 (b-1)t\le W,\qquad R_b\le2t,                         \tag{3.7}
\]

and hence, because \(H=o(b)\),

\[
 2Ht+R_b\le(2H+2){W\over b-1}=o(W).                  \tag{3.8}
\]

Consequently it is enough to prove only

\[
\boxed{
 \sum_{\substack{b-H\le s\le b+H\\s\ne b}}
 \left[{2b\choose s}-
 \left|\bigcup_{P\in\mathscr P}
       \{I_s^{z_P}(i):0\le i\le b\}\right|\right]
 =o(W).}                                              \tag{3.9}
\]

This is the live phase-packet selection gate. Existing exact middle
codegrees, fixed-pairing cube banks, adjacent-rank loads, set-level Euler
components, and balanced coset banks do not prove (3.9): they control
selected marginal ranks or local banks, not every nonzero band offset for
one common selected family.

For scale, \(h_{b+1}=o(W)\) alone forces

\[
 (b+1)t\ge {2b\choose b+1}-o(W)
 ={b\over b+1}W-o(W),                                \tag{3.10}
\]

so \(t\ge(1-o(1))W/b\). Together with (3.7), any successful internal-core
selector necessarily has \(t=(1+o(1))W/b\).

## 4. Relation to the existing high OR-derivative compiler

This is exactly the existing high OR-derivative compiler in Master
Section 3.4, specialized to phase packets with
\(L=b+1\), \(\ell=b-H\), and \(u=b+H\). The same compression applies to
every clean singleton physical fragment.
If a fragment has \(L\) consecutive designated starts and is clean through
ranks \(b-H,\ldots,b+H\), emit its length-\(\ell\) source windows whose
starts are

\[
                         0,1,\ldots,L+2H-1.           \tag{4.1}
\]

These are \(L+2H\) set-valued letters. Lemma 2.1's proof preserves every
designated band target. For \(t\) fragments of total core length \(M\),
the direct-hole compiler can therefore be sharpened from

\[
 M+(b+H-1)t\qquad\hbox{to}\qquad M+2Ht.               \tag{4.2}
\]

With globally distinct middle targets, the sufficient overhead condition
is \(2Ht=o(W)\), equivalently \(t=o(W/H)\), instead of
\((b+H)t=o(W)\), equivalently \(t=o(W/b)\). More generally, if
\(\mathcal I_b\) is the union of the \(M\) middle occurrences, the exact
middle penalty is

\[
                         2Ht+(M-|\mathcal I_b|).       \tag{4.3}
\]

For completeness, normalize the core starts to \(0,\ldots,L-1\). A
rank-\((\ell+q)\) target at core start \(i\), \(0\le q\le2H\), is the
union of the emitted length-\(\ell\) source windows at starts
\(i,\ldots,i+q\). The largest required emitted index is
\((L-1)+2H=L+2H-1\), exactly the last index in (4.1). Its source letters
exist because the rank-\((b+H)=\ell+2H\) window at the final core start
exists. This proves the general claim without any cyclic or joining
assumption.

## 5. Consequences for the master gates

1. **Gate \(C_{\rm Q}\).** Ordered FIFO trails, queue balance, endpoint
   switching, packet-boundary repair, triangular cross-join cleanliness,
   and an \(o(W/b)\) trail bound are no longer coefficient-one premises.
   Replace the gate by (3.9), or by the more permissive (3.5).

2. **Phase-packet status.** “Ordered lift is open” should become
   “set-valued serialization and cleanliness are closed; correlated
   all-band packet selection is open.” The set-level Euler and fixed-order
   queue results may remain as true structural facts, but are not live
   serialization gates. The fixed-order Hamming-code bound remains relevant
   only as a restriction on internally disjoint selection from one order.

3. **Ordered-port/cross-join note.** Its mathematical statements need not
   be retracted, but its claim to identify the exact remaining
   \(C_{\rm Q}\) obstruction is obsolete. Mark it as a superseded
   singleton-joining route or archive it.

4. **Former Gate \(C_{\rm P}\) and the duplicate compiler.** The current
   master front matter correctly says that Section 3.4 makes the former
   product-lift gate \(C_{\rm P}\) unnecessary. Later rows that still list
   \(C_{\rm P}\) as live, or require \(A+B+C_{\rm P}\), are stale and should
   be removed or archived. Section 4.4 and Appendix I.1's singleton
   linearization theorem remain true, but are strictly weaker duplicates:
   their \(gt=o(W)\) barrier is replaced by \(2Ht=o(W)\), equivalently
   \(t=o(W/H)\), or by the collision form (4.3).

5. **Scope, architecture, and completion ledgers.** Replace claims that
   \(C_{\rm Q}\) requires ordered physical trails or cross-join repair by
   (3.9). Point both the punctured \(A\to B\) route and the independent
   fragment routes to Section 3.4, not to a product lift. Remove stale
   invocations of (I.6)/(4.13), or restate them with the Section 3.4
   \(2Ht\) compiler condition. Statements that two- or three-rank banks do
   not control all band offsets remain valid and essential.

The coefficient-one theorem remains open: the compression proves the word
construction conditional on (3.5) or (3.9), but does not construct the
required correlated packet family.
